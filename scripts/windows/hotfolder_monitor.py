"""
hotfolder_monitor.py — Surveillance automatique des dossiers NAS
Projet: PrintFlow SaaS — PrimeCenter Integration
Version: 1.0 — Fév 2026

Surveille le dossier 01_INPUT_FILES sur le NAS.
Quand un nouveau fichier arrive:
  1. Valide la nomenclature
  2. Crée le ticket XML d'entrée (pour MAX futur)
  3. Log l'événement
  4. Surveille le dossier OUTPUT pour confirmer le traitement

Usage:
    python hotfolder_monitor.py                    # Surveille en continu
    python hotfolder_monitor.py --once             # Vérifie une seule fois
    python hotfolder_monitor.py --watch-output     # Surveille aussi les outputs

Installation prérequis:
    pip install watchdog
"""

import os
import sys
import json
import time
import logging
import shutil
from pathlib import Path
from datetime import datetime
from typing import Optional

# Watchdog pour surveiller les dossiers
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler, FileCreatedEvent
    WATCHDOG_OK = True
except ImportError:
    WATCHDOG_OK = False
    print("[ATTENTION] watchdog non installé. Installer avec: pip install watchdog")
    print("[INFO] Mode polling (vérification toutes les 30 secondes) activé à la place")

# Import des modules locaux
sys.path.insert(0, str(Path(__file__).parent))
from parse_nomenclature import parse_filename, valider_dossier_input, EXTENSIONS_AUTORISEES
from create_xml_ticket import creer_ticket_xml_entree, DOSSIERS_NAS


# ============================================================
# CONFIGURATION LOGGING
# ============================================================

def configurer_logging(log_dir: Optional[str] = None):
    """Configure le système de logs."""
    handlers = [logging.StreamHandler(sys.stdout)]

    if log_dir:
        log_path = Path(log_dir) / f"hotfolder_{datetime.now().strftime('%Y%m%d')}.log"
        handlers.append(logging.FileHandler(str(log_path), encoding="utf-8"))

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=handlers
    )


logger = logging.getLogger("HotfolderMonitor")


# ============================================================
# ÉTAT DES FICHIERS EN COURS DE TRAITEMENT
# ============================================================

class TrackingState:
    """Suit l'état de traitement des fichiers."""

    def __init__(self):
        self.en_cours: dict = {}   # filename → {start_time, metadata, status}
        self.termines: list = []   # Liste des fichiers traités avec succès
        self.erreurs: list = []    # Liste des fichiers en erreur

    def marquer_debut(self, filename: str, metadata: dict):
        self.en_cours[filename] = {
            "start_time": datetime.now().isoformat(),
            "metadata": metadata,
            "status": "en_cours"
        }
        logger.info(f"[DEBUT] {filename} → Recette: {metadata.get('recette', '?')}")

    def marquer_succes(self, filename: str, print_file: str = "", cut_file: str = ""):
        if filename in self.en_cours:
            entry = self.en_cours.pop(filename)
            entry["status"] = "succes"
            entry["end_time"] = datetime.now().isoformat()
            entry["print_file"] = print_file
            entry["cut_file"] = cut_file
            self.termines.append(entry)
            logger.info(f"[OK] {filename} → {print_file}")

    def marquer_erreur(self, filename: str, erreur: str):
        if filename in self.en_cours:
            entry = self.en_cours.pop(filename)
        else:
            entry = {"filename": filename}
        entry["status"] = "erreur"
        entry["erreur"] = erreur
        entry["end_time"] = datetime.now().isoformat()
        self.erreurs.append(entry)
        logger.error(f"[ERREUR] {filename}: {erreur}")

    def rapport(self) -> dict:
        return {
            "en_cours": len(self.en_cours),
            "succes": len(self.termines),
            "erreurs": len(self.erreurs),
            "detail_erreurs": [e.get("erreur", "") for e in self.erreurs[-5:]]
        }


STATE = TrackingState()


# ============================================================
# TRAITEMENT D'UN FICHIER ENTRANT
# ============================================================

def traiter_fichier_entrant(filepath: str):
    """
    Traite un nouveau fichier détecté dans le hotfolder INPUT.

    Args:
        filepath: Chemin complet du fichier
    """
    filename = Path(filepath).name
    ext = Path(filepath).suffix.lower()

    # Ignorer les fichiers XML et autres non-images
    if ext not in EXTENSIONS_AUTORISEES:
        logger.debug(f"[IGNORE] {filename} (extension ignorée: {ext})")
        return

    logger.info(f"[DETECTE] Nouveau fichier: {filename}")

    # Attendre que le fichier soit complètement copié
    time.sleep(1)

    # 1. Valider la nomenclature
    meta = parse_filename(filename)
    if not meta.valide:
        STATE.marquer_erreur(filename, meta.erreur)
        # Déplacer vers un dossier d'erreur si nécessaire
        logger.error(f"[NOMENCLATURE INVALIDE] {filename}")
        logger.error(f"  {meta.erreur}")
        return

    # 2. Logger les métadonnées extraites
    logger.info(f"[METADATA] OrderId={meta.order_id}, JobId={meta.job_id}, "
                f"JobName={meta.job_name}, GangName={meta.gang_name}, "
                f"Format={meta.width_mm}x{meta.height_mm}mm, "
                f"Copies={meta.copies}ex, Recette={meta.recette}")

    STATE.marquer_debut(filename, {
        "order_id": meta.order_id,
        "job_id": meta.job_id,
        "job_name": meta.job_name,
        "gang_name": meta.gang_name,
        "recette": meta.recette
    })

    # 3. Créer le ticket XML d'entrée (pour MAX futur + archivage)
    try:
        xml_content = creer_ticket_xml_entree(meta, mode="bat")

        # Sauvegarder le XML dans les rapports
        date_str = datetime.now().strftime("%Y-%m-%d")
        xml_filename = filename.replace(meta.extension, "_ENTREE.xml")
        rapport_dir = Path(DOSSIERS_NAS["rapports"]) / date_str

        try:
            rapport_dir.mkdir(parents=True, exist_ok=True)
            xml_path = rapport_dir / xml_filename
            with open(str(xml_path), "w", encoding="utf-8") as f:
                f.write(xml_content)
            logger.info(f"[XML] Ticket d'entrée créé: {xml_path.name}")
        except Exception as e:
            logger.warning(f"[XML] Impossible de sauvegarder ticket XML: {e}")

    except Exception as e:
        logger.error(f"[XML] Erreur génération ticket: {e}")

    # 4. PrimeCenter traite automatiquement via hotfolder
    # (PrimeCenter surveille le dossier 01_INPUT_FILES et traite les fichiers)
    logger.info(f"[PRIM] Fichier soumis à PrimeCenter pour recette: {meta.recette}")
    logger.info(f"[PRIM] En attente de traitement automatique...")


# ============================================================
# SURVEILLANCE DES OUTPUTS (résultats PrimeCenter)
# ============================================================

def traiter_output_print(filepath: str):
    """Détecte un nouveau fichier de sortie impression."""
    filename = Path(filepath).name
    if "_PRINT." in filename.upper() or "_BAT." in filename.upper():
        logger.info(f"[OUTPUT PRINT] {filename}")
        # Trouver le job correspondant
        base = filename.replace("_PRINT.pdf", "").replace("_BAT.pdf", "")
        STATE.marquer_succes(
            base + ".pdf",
            print_file=filename
        )


def traiter_output_cut(filepath: str):
    """Détecte un nouveau fichier de sortie découpe."""
    filename = Path(filepath).name
    if "_CUT." in filename.upper():
        logger.info(f"[OUTPUT CUT] {filename}")


# ============================================================
# WATCHDOG HANDLERS
# ============================================================

class InputHandler(FileSystemEventHandler):
    """Surveille le dossier INPUT."""
    def on_created(self, event):
        if not event.is_directory:
            traiter_fichier_entrant(event.src_path)


class PrintOutputHandler(FileSystemEventHandler):
    """Surveille le dossier OUTPUT PRINTFILES."""
    def on_created(self, event):
        if not event.is_directory:
            traiter_output_print(event.src_path)


class CutOutputHandler(FileSystemEventHandler):
    """Surveille le dossier OUTPUT CUTFILES."""
    def on_created(self, event):
        if not event.is_directory:
            traiter_output_cut(event.src_path)


# ============================================================
# MODE POLLING (sans watchdog)
# ============================================================

def surveillance_polling(
    input_dir: str,
    interval_sec: int = 30,
    max_iterations: int = 0
):
    """
    Surveille le dossier INPUT par polling (sans watchdog).
    Plus simple mais moins réactif (vérification toutes les N secondes).

    Args:
        input_dir:       Dossier à surveiller
        interval_sec:    Secondes entre chaque vérification
        max_iterations:  0 = infini
    """
    logger.info(f"[POLLING] Démarrage surveillance: {input_dir}")
    logger.info(f"[POLLING] Intervalle: {interval_sec}s")

    fichiers_vus = set()
    iteration = 0

    while True:
        iteration += 1
        if max_iterations > 0 and iteration > max_iterations:
            break

        try:
            dossier = Path(input_dir)
            if not dossier.exists():
                logger.warning(f"[POLLING] Dossier inaccessible: {input_dir}")
                time.sleep(interval_sec)
                continue

            # Lister les fichiers actuels
            fichiers_actuels = set()
            for f in dossier.iterdir():
                if f.is_file() and f.suffix.lower() in EXTENSIONS_AUTORISEES:
                    fichiers_actuels.add(f.name)

            # Détecter les nouveaux fichiers
            nouveaux = fichiers_actuels - fichiers_vus
            for nouveau in sorted(nouveaux):
                traiter_fichier_entrant(str(dossier / nouveau))

            fichiers_vus = fichiers_actuels

            # Afficher rapport toutes les 10 minutes
            if iteration % (600 // interval_sec) == 0:
                rapport = STATE.rapport()
                logger.info(f"[RAPPORT] {rapport}")

        except Exception as e:
            logger.error(f"[POLLING] Erreur: {e}")

        time.sleep(interval_sec)


# ============================================================
# MODE WATCHDOG (temps réel)
# ============================================================

def surveillance_watchdog(
    input_dir: str,
    watch_output: bool = False
):
    """
    Surveille les dossiers en temps réel avec watchdog.

    Args:
        input_dir:    Dossier INPUT à surveiller
        watch_output: Surveiller aussi les dossiers OUTPUT?
    """
    logger.info(f"[WATCHDOG] Démarrage surveillance temps réel: {input_dir}")

    observer = Observer()
    observer.schedule(InputHandler(), input_dir, recursive=False)

    if watch_output:
        print_dir = DOSSIERS_NAS["print_files"]
        cut_dir = DOSSIERS_NAS["cut_files"]
        observer.schedule(PrintOutputHandler(), print_dir, recursive=False)
        observer.schedule(CutOutputHandler(), cut_dir, recursive=False)
        logger.info(f"[WATCHDOG] Surveillance OUTPUT PRINT: {print_dir}")
        logger.info(f"[WATCHDOG] Surveillance OUTPUT CUT: {cut_dir}")

    observer.start()
    logger.info("[WATCHDOG] Surveillance active. Ctrl+C pour arrêter.")

    try:
        while True:
            time.sleep(1)
            # Rapport toutes les 10 minutes
            if int(time.time()) % 600 == 0:
                logger.info(f"[RAPPORT] {STATE.rapport()}")
    except KeyboardInterrupt:
        observer.stop()
        logger.info("[WATCHDOG] Arrêt de la surveillance.")

    observer.join()


# ============================================================
# MODE ONE-SHOT (vérification unique)
# ============================================================

def verification_unique(input_dir: str):
    """
    Vérifie tous les fichiers présents dans le dossier INPUT (une seule fois).
    Utile pour traiter un backlog ou tester.

    Args:
        input_dir: Dossier INPUT à analyser
    """
    logger.info(f"[ONE-SHOT] Analyse du dossier: {input_dir}")

    valides, invalides = valider_dossier_input(input_dir)

    logger.info(f"[ONE-SHOT] {len(valides)} fichiers valides, {len(invalides)} invalides")

    for meta in valides:
        logger.info(f"  [OK] {meta.filename} → {meta.recette}")

    for meta in invalides:
        logger.error(f"  [ERR] {meta.filename}: {meta.erreur}")

    if invalides:
        print(f"\n⚠️  {len(invalides)} fichiers avec nomenclature incorrecte!")
        print("Renommez-les selon le format:")
        print("  012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf")


# ============================================================
# ENTRÉE PRINCIPALE
# ============================================================

if __name__ == "__main__":
    # Configurer les logs
    configurer_logging()

    input_dir = DOSSIERS_NAS["input"]
    watch_output = "--watch-output" in sys.argv

    logger.info("=" * 60)
    logger.info("PrintFlow — HotFolder Monitor v1.0")
    logger.info(f"Dossier INPUT:  {input_dir}")
    logger.info(f"Watch OUTPUT:   {watch_output}")
    logger.info("=" * 60)

    # Mode one-shot
    if "--once" in sys.argv:
        verification_unique(input_dir)
        sys.exit(0)

    # Mode surveillance continue
    if WATCHDOG_OK:
        surveillance_watchdog(input_dir, watch_output=watch_output)
    else:
        logger.warning("watchdog non disponible → mode polling (30s)")
        surveillance_polling(input_dir, interval_sec=30)
