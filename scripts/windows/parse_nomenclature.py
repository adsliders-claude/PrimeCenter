"""
parse_nomenclature.py — Extraction des métadonnées depuis le nom de fichier
Projet: PrintFlow SaaS — PrimeCenter Integration
Version: 1.0 — Fév 2026

Format attendu:
    OrderId_jobId_jobName_gangName_formatWidthxformatHeightmm_copie_ex.ext
    Exemple: 012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf

Usage:
    python parse_nomenclature.py 012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf
    python parse_nomenclature.py --batch "\\\\nas\\dossier\\01_INPUT_FILES"
"""

import re
import os
import sys
import json
import csv
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import Optional


# ============================================================
# STRUCTURE DES MÉTADONNÉES D'UN JOB
# ============================================================

@dataclass
class JobMetadata:
    """Métadonnées extraites du nom de fichier."""
    filename: str           # Nom du fichier original
    order_id: str           # N° dossier LPF (ex: 012345)
    job_id: str             # Unité de production (ex: 001)
    job_name: str           # Catégorie produit (ex: Vitrine)
    gang_name: str          # Référence matière (ex: Orange02)
    width_mm: int           # Largeur en mm (ex: 1210)
    height_mm: int          # Hauteur en mm (ex: 650)
    copies: int             # Nombre d'exemplaires (ex: 20)
    extension: str          # Extension fichier (ex: .pdf)
    recette: str = ""       # Recette choisie (calculée après)
    valide: bool = True     # Nomenclature valide?
    erreur: str = ""        # Message d'erreur si invalide


# ============================================================
# REGEX PATTERN POUR EXTRACTION
# ============================================================

PATTERN = re.compile(
    r"""^
    (?P<order_id>\d{6})          # OrderId: 6 chiffres (ex: 012345)
    _
    (?P<job_id>\d{3})            # jobId: 3 chiffres (ex: 001)
    _
    (?P<job_name>[A-Za-z0-9_]+)  # jobName: alphanumérique + underscore
    _
    (?P<gang_name>[A-Za-z0-9]+)  # gangName: référence matière
    _
    (?P<width>\d+)               # Width: chiffres seulement
    x                            # séparateur dimensions
    (?P<height>\d+)              # Height: chiffres seulement
    mm                           # unité (obligatoire)
    _
    (?P<copies>\d+)              # copies: nombre
    ex                           # suffixe (obligatoire)
    (?P<ext>\.[a-zA-Z]+)?        # extension: optionnelle ici, extraite séparément
    $""",
    re.VERBOSE | re.IGNORECASE
)


# ============================================================
# LOGIQUE DE SÉLECTION DES RECETTES
# ============================================================

JOB_NAME_TO_RECETTE = {
    # Vitrine et dérivés
    "vitrine":          "IMPRESSION_VITRINE",
    "vitrine_noel":     "IMPRESSION_VITRINE",
    "vitrine_noel":     "IMPRESSION_VITRINE",

    # Stickers et vitrophanie
    "sticker":          "VITROPHANIE_STICKERS",
    "stickers":         "VITROPHANIE_STICKERS",
    "vitrophanie":      "VITROPHANIE_STICKERS",
    "autocollant":      "VITROPHANIE_STICKERS",

    # Bâche
    "bache":            "IMPRESSION_BACHE",
    "bâche":            "IMPRESSION_BACHE",
    "banderole":        "IMPRESSION_BACHE",

    # Impression directe
    "imprimdirect":     "IMPRESSION_DIRECTE",
    "impressiondirect": "IMPRESSION_DIRECTE",
    "directe":          "IMPRESSION_DIRECTE",
    "kakemono":         "IMPRESSION_DIRECTE",
    "rollup":           "IMPRESSION_DIRECTE",
    "roll_up":          "IMPRESSION_DIRECTE",
    "plv":              "IMPRESSION_DIRECTE",
    "toile":            "IMPRESSION_DIRECTE",
    "enseigne":         "IMPRESSION_DIRECTE",
}


def choisir_recette(job_name: str, mode: str = "bat") -> str:
    """
    Choisit la recette PrimeCenter selon le jobName et le mode.

    Args:
        job_name: Catégorie produit (ex: 'Vitrine', 'Sticker')
        mode: 'bat' pour validation client, 'prod' pour production

    Returns:
        Nom de la recette PrimeCenter
    """
    recette_base = JOB_NAME_TO_RECETTE.get(
        job_name.lower(),
        "PREFLIGHT_PAO"  # Défaut si inconnu
    )
    suffixe = "_BAT" if mode == "bat" else "_PROD"
    return f"{recette_base}{suffixe}"


# ============================================================
# FONCTIONS D'EXTRACTION
# ============================================================

def parse_filename(filename: str) -> JobMetadata:
    """
    Parse le nom de fichier et extrait les métadonnées.

    Args:
        filename: Nom du fichier (avec ou sans extension)
                  Ex: '012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf'

    Returns:
        JobMetadata avec toutes les données extraites
    """
    # Séparer l'extension du nom de base
    name = Path(filename).stem          # Sans extension
    ext = Path(filename).suffix.lower() # Extension (.pdf, .psd, etc.)

    # Appliquer le regex
    match = PATTERN.match(name)

    if not match:
        return JobMetadata(
            filename=filename,
            order_id="", job_id="", job_name="", gang_name="",
            width_mm=0, height_mm=0, copies=0, extension=ext,
            valide=False,
            erreur=(
                f"Format invalide: '{filename}'\n"
                f"Attendu: OrderId_jobId_jobName_gangName_WxHmm_Nex{ext}\n"
                f"Exemple: 012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf"
            )
        )

    g = match.groupdict()

    metadata = JobMetadata(
        filename=filename,
        order_id=g['order_id'],
        job_id=g['job_id'],
        job_name=g['job_name'],
        gang_name=g['gang_name'],
        width_mm=int(g['width']),
        height_mm=int(g['height']),
        copies=int(g['copies']),
        extension=ext,
        valide=True,
        erreur=""
    )

    # Calculer la recette automatiquement
    metadata.recette = choisir_recette(metadata.job_name, mode="bat")

    return metadata


def generer_nomenclature(
    order_id: str,
    job_id: str,
    job_name: str,
    gang_name: str,
    width_mm: int,
    height_mm: int,
    copies: int,
    ext: str = ".pdf"
) -> str:
    """
    Génère le nom de fichier standard depuis les métadonnées.
    Utilisé par l'Agent LLM pour créer la nomenclature.

    Args:
        order_id:  N° dossier LPF (ex: '012345')
        job_id:    Unité de production (ex: '001')
        job_name:  Catégorie (ex: 'Vitrine')
        gang_name: Référence matière (ex: 'Orange02')
        width_mm:  Largeur en mm (ex: 1210)
        height_mm: Hauteur en mm (ex: 650)
        copies:    Nombre d'exemplaires (ex: 20)
        ext:       Extension fichier (défaut: '.pdf')

    Returns:
        Nom de fichier normalisé
        Ex: '012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf'
    """
    # Normalisation
    order_id = str(order_id).zfill(6)    # Toujours 6 chiffres
    job_id = str(job_id).zfill(3)        # Toujours 3 chiffres
    job_name = job_name.replace(" ", "_") # Pas d'espaces
    ext = ext if ext.startswith(".") else f".{ext}"

    return f"{order_id}_{job_id}_{job_name}_{gang_name}_{width_mm}x{height_mm}mm_{copies}ex{ext}"


# ============================================================
# VALIDATION DES FICHIERS EN BATCH
# ============================================================

EXTENSIONS_AUTORISEES = {".pdf", ".psd", ".jpg", ".jpeg", ".png"}


def valider_dossier_input(dossier: str) -> tuple[list, list]:
    """
    Vérifie tous les fichiers dans le dossier INPUT_FILES.

    Args:
        dossier: Chemin NAS vers 01_INPUT_FILES

    Returns:
        (valides: list[JobMetadata], invalides: list[JobMetadata])
    """
    valides = []
    invalides = []

    dossier_path = Path(dossier)

    if not dossier_path.exists():
        print(f"[ERREUR] Dossier introuvable: {dossier}")
        return [], []

    for fichier in dossier_path.iterdir():
        if not fichier.is_file():
            continue

        ext = fichier.suffix.lower()
        if ext not in EXTENSIONS_AUTORISEES:
            continue  # Ignorer les .xml, .txt, etc.

        meta = parse_filename(fichier.name)

        if meta.valide:
            valides.append(meta)
        else:
            invalides.append(meta)

    return valides, invalides


def exporter_csv(jobs: list, chemin_csv: str):
    """
    Exporte les métadonnées en CSV pour l'Agent LLM et le dashboard.

    Args:
        jobs: Liste de JobMetadata
        chemin_csv: Chemin du fichier CSV de sortie
    """
    if not jobs:
        return

    fields = ["filename", "order_id", "job_id", "job_name", "gang_name",
              "width_mm", "height_mm", "copies", "extension", "recette",
              "valide", "erreur"]

    with open(chemin_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for job in jobs:
            row = asdict(job)
            writer.writerow({k: row[k] for k in fields})

    print(f"[OK] CSV exporté: {chemin_csv} ({len(jobs)} lignes)")


# ============================================================
# CLI — UTILISATION EN LIGNE DE COMMANDE
# ============================================================

def afficher_metadata(meta: JobMetadata):
    """Affiche les métadonnées d'un job en format lisible."""
    if not meta.valide:
        print(f"\n[INVALIDE] {meta.filename}")
        print(f"  Erreur: {meta.erreur}")
        return

    print(f"\n[OK] {meta.filename}")
    print(f"  OrderId:   {meta.order_id}  (Dossier LPF)")
    print(f"  JobId:     {meta.job_id}    (Unité prod)")
    print(f"  JobName:   {meta.job_name}  (Catégorie)")
    print(f"  GangName:  {meta.gang_name} (Matière)")
    print(f"  Format:    {meta.width_mm}x{meta.height_mm}mm")
    print(f"  Copies:    {meta.copies}ex")
    print(f"  Extension: {meta.extension}")
    print(f"  Recette:   {meta.recette}")
    print(f"  JSON:      {json.dumps(asdict(meta), ensure_ascii=False)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nUsage:")
        print("  1 fichier:  python parse_nomenclature.py 012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf")
        print("  Dossier:    python parse_nomenclature.py --batch \"\\\\\\\\nas\\\\dossier\\\\01_INPUT_FILES\"")
        print("\nTest interne (sans argument):")

        # Tests automatiques
        tests = [
            "012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf",
            "012345_002_Sticker_Vitro200_500x500mm_50ex.pdf",
            "012345_003_Bache_Bache550_3000x1500mm_1ex.pdf",
            "012345_004_Kakemono_Satin100_850x2000mm_2ex.pdf",
            "BAD_FILE_NAME.pdf",
            "012345_001_Vitrine_Orange02_1210x650mm_20ex",  # Sans extension
        ]

        print("\n--- TESTS ---")
        for t in tests:
            meta = parse_filename(t)
            afficher_metadata(meta)

        print("\n--- TEST génerer_nomenclature ---")
        nom = generer_nomenclature("12345", "1", "Vitrine", "Orange02", 1210, 650, 20)
        print(f"  Généré: {nom}")

        sys.exit(0)

    # Mode batch
    if sys.argv[1] == "--batch":
        if len(sys.argv) < 3:
            print("Erreur: Spécifier le dossier après --batch")
            sys.exit(1)

        dossier = sys.argv[2]
        print(f"Analyse du dossier: {dossier}")

        valides, invalides = valider_dossier_input(dossier)

        print(f"\n✅ Fichiers valides: {len(valides)}")
        for v in valides:
            print(f"  {v.filename}")

        print(f"\n❌ Fichiers invalides: {len(invalides)}")
        for i in invalides:
            print(f"  {i.filename}: {i.erreur}")

        # Export CSV dans le même dossier
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_path = str(Path(dossier).parent / f"rapport_nomenclature_{ts}.csv")
        exporter_csv(valides + invalides, csv_path)

    else:
        # Mode fichier unique
        meta = parse_filename(sys.argv[1])
        afficher_metadata(meta)
        sys.exit(0 if meta.valide else 1)
