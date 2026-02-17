# Nomenclature Complète — PrintFlow SaaS
**Système:** PrimeCenter V4 PRO — Extraction depuis nom de fichier
**Format Standard:** `OrderId_jobId_jobName_gangName_formatWidthxformatHeightmm_copie_ex`
**Version:** 2.0 — Fév 2026 (remplace FILENAME_CONVENTION.md)

---

## 🎯 Format Officiel

```
OrderId_jobId_jobName_gangName_formatWidthxformatHeightmm_copie_ex.ext

EXEMPLE COMPLET:
012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf

┌─────────────────────────────────────────────────────────────┐
│ 012345   = OrderId   → N° dossier LPF (numéro interne)     │
│ 001      = jobId     → Unité de production (1V=1F=1M)       │
│ Vitrine  = jobName   → Catégorie produit                    │
│ Orange02 = gangName  → Référence matière (base de données)  │
│ 1210     = Width     → Largeur du visuel en mm              │
│ x        = séparateur dimensions                            │
│ 650      = Height    → Hauteur du visuel en mm              │
│ mm       = unité     → Millimètres (toujours)               │
│ 20ex     = copies    → Nombre d'exemplaires                 │
│ .pdf     = extension → Format fichier                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 Détail de Chaque Segment

### 1️⃣ `OrderId` — N° Dossier LPF
```
Type: Numéro séquentiel de 6 chiffres
Format: 012345
Règle: Identifiant unique du dossier client

Exemples:
  012345 → Dossier LPF n°12345
  000001 → Premier dossier
  045678 → Dossier LPF n°45678 (= LPF045678)

Source: CRM / Système de gestion interne
```

### 2️⃣ `jobId` — Unité de Production
```
Type: Numéro séquentiel de 3 chiffres (dans le dossier)
Format: 001, 002, 003...
Règle: 1 jobId = 1 visuel + 1 format + 1 matière

⚠️ IMPORTANT — PDF multi-pages:
  Si un PDF a 3 pages (3 visuels différents):
  → 012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf ← page 1
  → 012345_002_Vitrine_Orange02_1210x650mm_20ex.pdf ← page 2
  → 012345_003_Vitrine_Orange02_1210x650mm_20ex.pdf ← page 3
  Chaque page = 1 jobId séparé

Exemples:
  001 → Premier visuel du dossier
  002 → Deuxième visuel (même dossier, format/matière/copies différents possible)
  010 → Dixième visuel
```

### 3️⃣ `jobName` — Catégorie Produit
```
Type: Texte sans espaces (underscores si plusieurs mots)
Format: PascalCase recommandé

Valeurs autorisées (liste extensible):
  Vitrine            → Vitrine magasin
  Vitrine_Noel       → Vitrine thématique Noël
  Sticker            → Autocollant standard
  Vitrophanie        → Sticker vitrophanie (sans solvant)
  Bache              → Bâche grand format
  Kakemono           → Kakémono/roll-up
  RollUp             → Roll-up spécifique
  PLV                → Publicité sur lieu de vente
  ImprimanteDirect   → Impression directe standard
  Toile              → Toile canvas
  Custom: [SaisiLibre] → Texte libre si pas de catégorie
```

### 4️⃣ `gangName` — Référence Matière
```
Type: Code alphanumérique de la base de données matières
Format: [NomMatière][Numéro]
Règle: Référence interne unique (traçabilité)

IMPORTANT — Utilisation pour ganging (amalgame):
  gangName = clé de regroupement!
  Tous les jobs avec MÊME gangName → amalgamé ensemble
  Optimise: réduction perte matière + manipulation atelier

Exemples (à définir dans votre base de données):
  Orange02   → Film Orange, épaisseur 02
  Vinyl80    → Vinyle adhésif, 80 microns
  Bache550   → Bâche PVC 550g/m²
  Vitro200   → Vitrophanie 200 microns
  Satin100   → Satin photo 100g
  [À compléter selon votre catalogue matières]

Source: Base de données matières interne
```

### 5️⃣ `formatWidthxformatHeightmm` — Dimensions du Visuel
```
Type: Dimensions numériques + séparateur + unité
Format: [Largeur]x[Hauteur]mm
Unité: Toujours mm (millimètres)

Règles:
  → Dimensions du VISUEL FINI (sans fond perdu)
  → Le fond perdu sera ajouté par PrimeCenter selon la recette
  → Largeur AVANT Hauteur (convention paysage/portrait)

Exemples:
  1210x650mm   → Vitrine 1210mm large x 650mm haut
  500x500mm    → Sticker carré 50cm
  3000x1000mm  → Bâche 3m x 1m
  420x594mm    → Format A2 (297x420 → 594x420 landscape)
  600x800mm    → Portrait standard
```

### 6️⃣ `copie_ex` — Nombre d'Exemplaires
```
Type: Nombre entier + suffixe "ex"
Format: [N]ex
Règle: Nombre total d'exemplaires de CE visuel

Exemples:
  1ex    → 1 exemplaire (maquette, proto)
  5ex    → 5 exemplaires
  20ex   → 20 exemplaires
  100ex  → 100 exemplaires
  250ex  → Petite série
```

---

## 📝 Exemples Complets par Type de Produit

### Vitrine Magasin
```
012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf
       ↑    ↑       ↑         ↑           ↑
     Doss  Job   Catég.    Matière     Copies
```

### Vitrophanie / Sticker
```
012345_002_Vitrophanie_Vitro200_500x500mm_50ex.pdf
                                → Film vitrophanie
                                → 50 autocollants 50x50cm
```

### Bâche
```
012345_003_Bache_Bache550_3000x1000mm_1ex.pdf
                          → Bâche 3m x 1m, 1 exemplaire
```

### Impression Directe (Print+Cut)
```
012345_004_ImprimDirect_Vinyl80_200x300mm_100ex.pdf
                                 → 100 stickers vinyle
```

### Kakémono / Roll-up
```
012345_005_Kakemono_Satin100_850x2000mm_2ex.pdf
                              → 2 roll-ups 85cm x 2m
```

### PLV Thématique
```
012345_006_PLV_Noel_CartouFoam_400x600mm_5ex.pdf
                    → Matière carton mousse
```

---

## 🔄 Mapping NAS — Où va chaque fichier?

```
\\obelix_nascp\Boite de transferts\KARIM\PRIMECENTER\TEST Mise en place\

01_INPUT_FILES\
  └── 012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf  ← Fichier brut CLIENT

02_OUTPUT_PREFLIGHT_FIXUP\
  └── 012345_001_Vitrine_Orange02_1210x650mm_20ex_BAT.pdf  ← BAT corrigé (VALIDATION)

02_PROD_PREFLIGHT_FIXUP\
  └── [Idem mais version PROD pour amalgame]

03_BAT_CTRL_PREFLIGHT\
  └── 012345_001_Vitrine_Orange02_1210x650mm_20ex_CTRL.pdf  ← Rapport contrôle

03_PROD_PREFLIGHT_INPUT\
  └── [Input pour recette PROD après validation BAT]

04 - OUTPUT_PRINTFILES\
  └── 012345_001_Vitrine_Orange02_1210x650mm_20ex_PRINT.pdf  ← Fichier impression

04 - OUTPUT_CUTFILES\
  └── 012345_001_Vitrine_Orange02_1210x650mm_20ex_CUT.dxf   ← Fichier découpe

05 - RECIPES\
  └── [Recettes PrimeCenter sauvegardées]

06 - RAPPORTS PRIMECENTER\
  └── 012345_001_Vitrine_Orange02_1210x650mm_20ex.xml  ← Ticket XML sortie
```

---

## 🔧 Mapping dans PrimeCenter

**Configuration extraction dans PrimeCenter V4:**
```
Modèle d'extraction:
{orderId}_{jobId}_{jobName}_{gangName}_{formatWidth}x{formatHeight}mm_{copies}ex

Dans PrimeCenter UI:
→ Recette > Fichiers > Paramètres d'import > Modèle extraction
→ Coller: {orderId}_{jobId}_{jobName}_{gangName}_{formatWidth}x{formatHeight}mm_{copies}ex
```

**Mapping PrimeCenter ↔ XML:**
| Segment Fichier | Champ PrimeCenter | XML Tag |
|-----------------|-------------------|---------|
| `012345` | Order ID | `<orderID>` |
| `001` | Job ID | `<jobID>` |
| `Vitrine` | Job Name | `<jobName>` |
| `Orange02` | Customer/Gang ID | `<gang>` / `<customerID>` |
| `1210` | Media Width | `<width unit="mm">1210</width>` |
| `650` | Media Height | `<height unit="mm">650</height>` |
| `20` | Copies | `<copies>20</copies>` |

---

## ⚠️ Règles et Contraintes

### Séparateurs
```
✅ Underscore `_` entre tous les segments
✅ x minuscule entre dimensions (1210x650)
✅ mm en minuscule collé aux chiffres (650mm)
✅ ex en minuscule collé au nombre (20ex)

❌ Espaces interdits dans le nom
❌ Tirets (-) entre les segments
❌ Caractères spéciaux: é, è, à, ù, @, #, $, %
❌ Majuscules-minuscules mélangées aléatoirement
```

### Longueur maximum
```
Recommandé: < 100 caractères au total
Path NAS complet: < 260 caractères (limite Windows)
```

### Extensions autorisées
```
Entrée (INPUT_FILES):     .pdf, .psd, .jpg, .jpeg, .png
Sortie impression:         .pdf
Sortie découpe:            .dxf, .zcc, .pdf (selon cutter)
Tickets XML:               .xml
```

---

## 📊 Tableau de Validation Rapide

Avant de placer un fichier dans l'INPUT:

| Vérification | ✅ Valide | ❌ Invalide |
|-------------|----------|-----------|
| OrderId 6 chiffres | `012345` | `LPF045` |
| jobId 3 chiffres | `001` | `1` |
| jobName sans espace | `Vitrine_Noel` | `Vitrine Noel` |
| gangName en base | `Orange02` | `Film orange 2` |
| Format avec x et mm | `1210x650mm` | `1210 x 650 mm` |
| Copies avec ex | `20ex` | `20 ex` ou `20` |
| Extension minuscule | `.pdf` | `.PDF` |
| Pas de caractères spéciaux | `Sticker` | `Sticker_été` |

---

## 🚀 Génération Automatique (via Agent LLM)

L'Agent LLM "Expert Print Manager" génère automatiquement la nomenclature depuis:

```python
# Input depuis formulaire web:
{
    "order_id": "012345",         # Auto-incrémenté depuis CRM
    "job_id": "001",              # Auto-incrémenté dans le dossier
    "job_name": "Vitrine",        # Sélectionné dans dropdown
    "gang_name": "Orange02",      # Sélectionné depuis catalogue matières
    "width_mm": 1210,             # Saisi dans formulaire
    "height_mm": 650,             # Saisi dans formulaire
    "copies": 20                  # Saisi dans formulaire
}

# Output généré:
"012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf"
```

Voir: `scripts/windows/generate_nomenclature.py`

---

**Session:** https://claude.ai/code/session_017yhksCaj1YoCEk79BwGw1G
