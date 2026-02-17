# Guide d'Installation — Scripts Windows PrintFlow
**Système:** Windows 10/11
**Prérequis:** PC avec accès au NAS \\obelix_nascp\...
**Durée:** ~15 minutes

---

## 1️⃣ Installer Python (si pas déjà installé)

1. Aller sur: https://python.org/downloads
2. Télécharger **Python 3.11** ou plus récent
3. ⚠️ **IMPORTANT** — Lors de l'installation, cocher:
   - [x] **"Add Python to PATH"** ← OBLIGATOIRE
4. Cliquer "Install Now"

**Vérifier l'installation:**
```cmd
python --version
# Doit afficher: Python 3.11.x ou plus
```

---

## 2️⃣ Télécharger les Scripts

**Option A — Via git:**
```cmd
git clone https://github.com/votre-repo/PrimeCenter.git C:\PrintFlow
```

**Option B — Manuellement:**
- Copier le dossier `scripts\windows\` vers `C:\PrintFlow\scripts\windows\`

---

## 3️⃣ Installer les Dépendances

Ouvrir **PowerShell** ou **CMD**:
```cmd
cd C:\PrintFlow\scripts\windows
pip install -r requirements.txt
```

Cela installe:
- `watchdog` → surveillance dossiers en temps réel
- `pyautogui` → automatisation PC (si besoin)
- `Pillow` → traitement images
- `pywin32` → intégration Windows
- `requests` → appels HTTP (future API)
- `openpyxl` → exports Excel

---

## 4️⃣ Configurer l'Accès NAS

Vérifier que le NAS est accessible:
```cmd
ping obelix_nascp
dir "\\obelix_nascp\Boite de transferts\KARIM\PRIMECENTER"
```

Si accès refusé → mapper le réseau:
```cmd
net use Z: "\\obelix_nascp\Boite de transferts" /user:VOTRE_USER VOTRE_MOT_DE_PASSE /persistent:yes
```

---

## 5️⃣ Tester les Scripts

### Test 1: Parser une nomenclature
```cmd
python parse_nomenclature.py 012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf
```

**Résultat attendu:**
```
[OK] 012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf
  OrderId:   012345  (Dossier LPF)
  JobId:     001     (Unité prod)
  JobName:   Vitrine  (Catégorie)
  GangName:  Orange02 (Matière)
  Format:    1210x650mm
  Copies:    20ex
  Recette:   IMPRESSION_VITRINE_BAT
```

### Test 2: Générer un ticket XML
```cmd
python create_xml_ticket.py 012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf
```

### Test 3: Vérifier le dossier INPUT
```cmd
python hotfolder_monitor.py --once
```

### Test 4: Lancer la surveillance continue
```cmd
python hotfolder_monitor.py
```
*(Ctrl+C pour arrêter)*

---

## 6️⃣ Lancer la Surveillance au Démarrage (optionnel)

Pour que la surveillance se lance automatiquement au démarrage de Windows:

**Option A — Planificateur de tâches Windows:**
1. Ouvrir "Planificateur de tâches"
2. Créer une tâche → Déclencheur: "Au démarrage"
3. Action: `python C:\PrintFlow\scripts\windows\hotfolder_monitor.py`

**Option B — Fichier .bat:**
Créer `START_MONITOR.bat`:
```batch
@echo off
cd C:\PrintFlow\scripts\windows
python hotfolder_monitor.py >> C:\PrintFlow\logs\monitor.log 2>&1
```

---

## 7️⃣ Structure Finale

```
C:\PrintFlow\
├── scripts\
│   └── windows\
│       ├── parse_nomenclature.py   ← Parser nomenclature
│       ├── create_xml_ticket.py    ← Créer tickets XML
│       ├── hotfolder_monitor.py    ← Surveillance dossiers
│       ├── requirements.txt        ← Dépendances
│       └── INSTALLATION_GUIDE.md  ← Ce fichier
└── logs\                           ← Logs de surveillance
```

---

## 🔧 Dépannage

| Problème | Solution |
|----------|----------|
| `python` introuvable | Réinstaller Python avec "Add to PATH" coché |
| Accès NAS refusé | Vérifier credentials: `net use` |
| `watchdog` non trouvé | `pip install watchdog` |
| XML non généré | Vérifier permissions dossier RAPPORTS |
| Surveillance lente | Normal si polling mode (watchdog non installé) |

---

**Support:** Consulter la documentation dans `docs/` ou contacter l'équipe.
