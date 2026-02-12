# Structure des Hotfolders — PREFLIGHT_PAO_PRO

**Utilisation:** Automatisation V2 (après test manuel V1)
**Paquet:** PrimeCenter PRO
**Mode:** Semi-automatisé (import auto, export manuel)

---

## 📁 Structure des Dossiers

```
/data/hotfolder_pao/                   ← Dossier racine
│
├── INPUT/                              ← Fichiers d'entrée
│   ├── BAT001_ACME_3_Poster.pdf
│   ├── BAT002_TECHCO_1_Banner.psd
│   ├── BAT003_DESIGN_2_Brochure.jpg
│   └── ...
│
├── DONE/                               ← Fichiers traités avec succès
│   ├── BAT001_ACME_3_Poster.pdf       (déplacé après import)
│   ├── BAT002_TECHCO_1_Banner.psd
│   └── ...
│
├── FAILED/                             ← Fichiers avec erreurs
│   ├── BAT999_BADFILE_1_Error.pdf     (déplacé après erreur)
│   └── ...
│
├── OUTPUT/
│   ├── PRINT/                          ← Fichiers d'impression (PDF)
│   │   ├── BAT001_ACME_3_PRINT.pdf
│   │   ├── BAT002_TECHCO_1_PRINT.pdf
│   │   └── ...
│   │
│   └── CUT/                            ← Fichiers de découpe (DXF/PDF/etc)
│       ├── BAT001_ACME_3_CUT.dxf
│       ├── BAT002_TECHCO_1_CUT.dxf
│       └── ...
│
└── ARCHIVE/                            ← Archive (optionnel)
    ├── 2025-02/
    │   ├── BAT001_ACME_3_Poster.pdf
    │   └── ...
    └── 2025-03/
        └── ...
```

---

## 🚀 Configuration du Hotfolder dans PrimeCenter

### Étape 1: Créer les Dossiers Physiques

```bash
# Linux / macOS
mkdir -p /data/hotfolder_pao/{INPUT,DONE,FAILED,OUTPUT/{PRINT,CUT},ARCHIVE}

# Windows
mkdir "C:\hotfolder_pao\INPUT"
mkdir "C:\hotfolder_pao\DONE"
mkdir "C:\hotfolder_pao\FAILED"
mkdir "C:\hotfolder_pao\OUTPUT\PRINT"
mkdir "C:\hotfolder_pao\OUTPUT\CUT"
mkdir "C:\hotfolder_pao\ARCHIVE"
```

### Étape 2: Configurer dans PrimeCenter

```
Recette: PREFLIGHT_PAO_PRO
│
├── Onglet "Fichiers"
│   ├── Paramètres d'import
│   │   ├── ☑️ Enable Hotfolder
│   │   ├── Hotfolder path: /data/hotfolder_pao/INPUT/
│   │   ├── Action si succès: Déplacer vers /data/hotfolder_pao/DONE/
│   │   ├── Action si échec: Déplacer vers /data/hotfolder_pao/FAILED/
│   │   └── Modèle extraction: {JobID}_{CustomerID}_{Copies}_{JobName}
│   │
│   └── Profils preflight:
│       ├── Profil 1 (Check)
│       └── Profil 2 (Fix)
│
├── Onglet "Layout"
│   ├── Bleeding: Canvas Extend 5mm (tous côtés)
│   ├── Nesting: True Shape
│   └── Output folder:
│       ├── Print: /data/hotfolder_pao/OUTPUT/PRINT/
│       └── Cut: /data/hotfolder_pao/OUTPUT/CUT/
│
└── Recette en mode: Semi-auto (Pro)
```

---

## 📤 Flux d'Automatisation (V2)

### Processus Complet

```
1. UTILISATEUR PLACE FICHIER
   ↓
   Dossier: /data/hotfolder_pao/INPUT/
   Fichier: BAT001_ACME_3_Poster.pdf

2. PRIMECENTER DÉTECTE (hotwatcher)
   ↓
   Import automatique du fichier

3. EXTRACTION MÉTADONNÉES
   ↓
   JobID: BAT001
   CustomerID: ACME
   Copies: 3
   JobName: Poster

4. PROFILS PREFLIGHT AUTO
   ↓
   Check (vérification)
   Fix (correction)

5. BLEED APPLIQUÉ AUTO
   ↓
   5mm extension sur tous côtés

6. NESTING AUTO
   ↓
   Layout généré (True Shape)

7. NOTIF UTILISATEUR
   ↓
   "Layout prêt pour export"
   OU
   "Erreur — vérifier FAILED/"

8. EXPORT MANUEL (PRO ne permet pas l'auto)
   ↓
   Clic "Print & Cut" dans PrimeCenter

9. FICHIERS GÉNÉRÉS
   ├── /data/hotfolder_pao/OUTPUT/PRINT/BAT001_ACME_3_PRINT.pdf
   └── /data/hotfolder_pao/OUTPUT/CUT/BAT001_ACME_3_CUT.dxf

10. FICHIER SOURCE ARCHIVÉ
    ↓
    /data/hotfolder_pao/DONE/BAT001_ACME_3_Poster.pdf
```

---

## ⚙️ Configuration Détaillée (V2)

### Hotfolder Input
**Path:** `/data/hotfolder_pao/INPUT/`
**Role:** Point d'entrée unique
**Action:** Import automatique continu

**Configuration PrimeCenter:**
```
Recette > Onglet Fichiers > Import Settings
├── Hotfolder actif: ✅ Oui
├── Chemin: /data/hotfolder_pao/INPUT/
├── Modèle extraction: {JobID}_{CustomerID}_{Copies}_{JobName}
├── Profils preflight:
│   ├── Check_PDFStandard (Check)
│   └── Fix_ColorConversion (Fix)
├── Action succès: Déplacer vers DONE/
├── Action échec: Déplacer vers FAILED/
└── Monitoring: ✅ Logs activés
```

### Output Directories

#### Print Output
**Path:** `/data/hotfolder_pao/OUTPUT/PRINT/`
**Contenu:** Fichiers PDF impression
**Format nommage:** `{JobID}_{CustomerID}_{Copies}_PRINT.pdf`
**Exemple:** `BAT001_ACME_3_PRINT.pdf`

#### Cut Output
**Path:** `/data/hotfolder_pao/OUTPUT/CUT/`
**Contenu:** Fichiers découpe (DXF/PDF/ZCC/SGP)
**Format nommage:** `{JobID}_{CustomerID}_{Copies}_CUT.{ext}`
**Exemples:**
- `BAT001_ACME_3_CUT.dxf` (DXF standard)
- `BAT001_ACME_3_CUT.pdf` (PDF cutter)
- `BAT001_ACME_3_CUT.zcc` (Zünd)
- `BAT001_ACME_3_CUT.sgp` (Summa)

### Done Folder
**Path:** `/data/hotfolder_pao/DONE/`
**Contenu:** Fichiers importés avec succès
**Action:** Déplacement automatique après import
**Archivage:** Copier régulièrement vers ARCHIVE/ par mois

### Failed Folder
**Path:** `/data/hotfolder_pao/FAILED/`
**Contenu:** Fichiers avec erreurs
**Monitoring:** Vérifier régulièrement
**Causes possibles:**
- Format non supporté
- Nom de fichier invalide
- Erreur lors du preflight

---

## 🔄 Monitoring & Maintenance (V2)

### Logs et Rapports

**Depuis PrimeCenter:**
- Paramètres > Production > CSV reports
- Activé: ✅ Oui
- Intervalle: 5 minutes
- Dossier: `/data/hotfolder_pao/OUTPUT/REPORTS/`

**Format rapport CSV:**
```
Timestamp,JobID,CustomerID,Status,Copies,LayoutName,FileName
2025-02-12T10:30:00,BAT001,ACME,SUCCESS,3,BAT001_ACME_Layout_01,BAT001_ACME_3_PRINT.pdf
2025-02-12T10:31:00,BAT002,TECHCO,SUCCESS,1,BAT002_TECHCO_Layout_01,BAT002_TECHCO_1_PRINT.pdf
2025-02-12T10:35:00,BAT999,BADFILE,FAILED,1,—,—
```

### Dossier FAILED — Troubleshooting

**À faire régulièrement:**
1. [ ] Vérifier dossier FAILED/
2. [ ] Identifier cause d'erreur
3. [ ] Corriger nom de fichier ou contenu
4. [ ] Déplacer vers INPUT/ pour réessayer

**Causes courantes:**
- `BAT 001_ACME_3_Poster.pdf` ❌ (espace au lieu de underscore)
- `BAT001_ACME_3.pdf` ❌ (manque {JobName})
- `BAT001.pdf` ❌ (nom trop court)
- Fichier corrompu ou format non supporté

---

## 📊 Performance Attendue (V2)

### Capacité du Hotfolder

| Métrique | Valeur |
|----------|--------|
| **Fichiers/jour** | 500+ |
| **Fichiers/heure** | 20-30 |
| **Fichiers/minute** | 0.5-1 |
| **Temps import/fichier** | 1-2 sec |
| **Temps preflight/fichier** | 2-5 sec |
| **Temps nesting/fichier** | 5-10 sec |
| **Temps total/fichier** | 10-15 sec |

### Calcul pour 500 BAT/jour

```
500 fichiers/jour
÷ 8 heures = 62.5 fichiers/heure
÷ 60 min = 1.04 fichiers/minute
× 15 sec = 15.6 sec par fichier

→ 1 serveur + 1 station PrimeCenter = ✅ Suffisant pour 500 BAT/jour
```

### Optimisations possibles

Si besoin de plus de capacité:
1. **Plusieurs recettes** en parallèle (Pro permet nombre illimité)
2. **Plusieurs stations** PrimeCenter (une par recette)
3. **Upgrade vers Max** pour automatisation complète (export auto)

---

## 🔐 Sécurité & Backup

### Permissions

**Linux/macOS:**
```bash
chmod 755 /data/hotfolder_pao/
chmod 755 /data/hotfolder_pao/*
```

**Windows:**
```
Dossier > Propriétés > Sécurité
├── Utilisateur PrimeCenter: Contrôle total
└── Service: Lecture/Écriture
```

### Backup

**Dossiers critiques à sauvegarder:**
```
/data/hotfolder_pao/OUTPUT/     ← Fichiers générés (IMPORTANT)
/data/hotfolder_pao/ARCHIVE/    ← Historique sources
```

**Fréquence:** Journalière ou hebdomadaire

### Archivage

**Script archivage (Linux/macOS):**
```bash
#!/bin/bash
# Archive files from DONE/ to ARCHIVE/YYYY-MM/
DATE=$(date +%Y-%m)
mkdir -p /data/hotfolder_pao/ARCHIVE/$DATE
mv /data/hotfolder_pao/DONE/* /data/hotfolder_pao/ARCHIVE/$DATE/
```

---

## 🐛 Dépannage V2

### Hotfolder ne détecte pas les fichiers

**Symptôme:** Fichiers dans INPUT/ non importés

**Solutions:**
1. [ ] Vérifier chemin hotfolder dans PrimeCenter
2. [ ] Vérifier permissions: `ls -la /data/hotfolder_pao/INPUT/`
3. [ ] Redémarrer PrimeCenter
4. [ ] Vérifier logs PrimeCenter

### Métadonnées non extraites

**Symptôme:** Fichiers importés sans JobID, CustomerID, etc.

**Solutions:**
1. [ ] Vérifier modèle: `{JobID}_{CustomerID}_{Copies}_{JobName}`
2. [ ] Vérifier noms de fichiers: `BAT001_ACME_3_Poster.pdf`
3. [ ] Tester extraction manuelle

### Performances dégradées

**Symptôme:** Hotfolder lent, files d'attente qui s'accumulent

**Solutions:**
1. [ ] Réduire taille images d'entrée (résolution)
2. [ ] Augmenter "Nesting optimization time"
3. [ ] Passer export manuel → semi-auto (si upgrade Max)
4. [ ] Ajouter deuxième station PrimeCenter

---

## 📅 Roadmap V2 → V3

```
V2 — Hotfolder semi-automatisé
├── ✅ Import auto
├── ✅ Preflight auto
├── ✅ Nesting auto
├── ❌ Export auto (limitation PRO)
└── Timeline: 1-2 mois test + optimisation

V3 — Upgrade Max (future)
├── ✅ Export auto
├── ✅ Tickets XML
├── ✅ Mode silencieux (recettes en bg)
├── ✅ Rapports XML
└── Timeline: Après validation 500 BAT/jour en PRO
```

---

**Session:** https://claude.ai/code/session_017yhksCaj1YoCEk79BwGw1G
