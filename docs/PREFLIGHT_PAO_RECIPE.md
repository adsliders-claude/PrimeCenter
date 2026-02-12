# Recette PREFLIGHT_PAO_PRO — Documentation Complète

**Nom Recette:** `PREFLIGHT_PAO_PRO`
**Paquet:** PrimeCenter V4 PRO
**Version:** 1.0 (Test Manual V1 — 2025-02-12)
**Objectif:** Automatiser la vérification et préparation des BAT pour impression/découpe

---

## 📖 Vue d'Ensemble

### Qu'est-ce qu'une Recette?

Une **recette** est une combinaison de **8 modules** qui définit comment les fichiers seront traités:

```
Recette PREFLIGHT_PAO_PRO
│
├─ 1. INPUT             → Import fichiers + métadonnées
├─ 2. CUTTER OPTIONS    → Configuration table découpe
├─ 3. TRIMBOX           → Recadrage (non utilisé)
├─ 4. BLEEDING          → Fond perdu 5mm ⭐ IMPORTANT
├─ 5. ANNOTATIONS       → Identificateurs (optionnel)
├─ 6. MIRRORING         → Miroir (non utilisé)
├─ 7. NESTING           → Imbrication (True Shape)
└─ 8. OUTPUT            → Export PDF + Découpe
```

### Les 4 Étapes de la Recette PREFLIGHT_PAO

```
1️⃣ CONTRÔLER
   └─ Profil Preflight Check
      └─ Vérifie: résolution, couleurs, fonts, bleed

2️⃣ CORRIGER
   └─ Profil Preflight Fix
      └─ Corrige: RGB→CMYK, incorporation fonts, résolution

3️⃣ AJOUTER 5MM FP (FOND PERDU)
   └─ Canvas Extend Bleed
      └─ Extension 5mm tous côtés pour sécurité découpe

4️⃣ AJOUTER CUTCONTOUR
   └─ Dictionnaire + Génération automatique
      └─ Contours de découpe → fichier DXF/PDF
```

---

## 🎯 Cas d'Usage

### Workflow d'Impression/Découpe Typique

```
BAT (Bon À Tirer)
  ↓
Fichier client (PDF/PSD/JPG)
  ↓
[RECETTE PREFLIGHT_PAO_PRO]
  ├─ Vérifier (résolution 300 DPI?, CMYK?, fonts?)
  ├─ Corriger (convertir RGB→CMYK, incorporer fonts)
  ├─ Ajouter bleed 5mm (sécurité découpe)
  ├─ Générer contours de découpe
  └─ Imbriquer optimalement
  ↓
Résultats
  ├─ PDF impression (avec bleed 5mm) → Imprimante
  └─ Fichier découpe (DXF avec contours) → Cutter
```

### Exemple Concret

**Entrée:**
```
BAT001_ACME_3_Poster.pdf
  └─ Format: 1000 × 600 px
  └─ Mode couleur: RGB (incorrect!)
  └─ Résolution: 72 DPI (trop faible)
  └─ Fonts: Arial (non incorporée)
```

**Après recette PREFLIGHT_PAO_PRO:**
```
Fichier corrigé:
  ├─ Mode couleur: CMYK ✓
  ├─ Résolution: 300 DPI ✓
  ├─ Fonts: Incorporées ✓
  ├─ Bleed 5mm ajouté ✓
  └─ Contours découpe ajoutés ✓

Fichiers générés:
  ├─ BAT001_ACME_3_PRINT.pdf     (impression)
  └─ BAT001_ACME_3_CUT.dxf       (découpe)
```

---

## 🔧 Configuration Détaillée des 8 Modules

### Module 1: INPUT (Import & Métadonnées)

**Rôle:** Importer les fichiers et extraire les informations automatiquement

#### Formats d'Entrée
```
✅ PDF           (format recommandé)
✅ PSD           (Photoshop)
✅ JPG / JPEG    (raster)
✅ PNG           (raster + alpha)
❌ SVG           (non supporté en import direct)
❌ Fichiers protégés par mot de passe
```

#### Extraction de Métadonnées
**Modèle:**
```
{JobID}_{CustomerID}_{Copies}_{JobName}
```

**Exemple:**
```
Fichier: BAT001_ACME_3_Poster.pdf
         ↓ Extraction
         JobID: BAT001
         CustomerID: ACME
         Copies: 3
         JobName: Poster
```

**Utilisation:**
- Annotations (affiché sur l'image)
- Tri/Ganging (regroupement par client)
- Nommage fichiers export

#### Profils Preflight EN ENTRÉE

**Profil 1 — Check (Vérification)**
```
Nom: "Verify_Basic_Files" ou "Check_PDFStandard"
Type: Check (sans modification)

Vérifie:
  ✓ Résolution ≥ 300 DPI
  ✓ Mode couleur CMYK ou Spot (pas RGB)
  ✓ Polices incorporées
  ✓ Pas d'objet transparent sans support
  ✓ Bleed requis présent

Résultat: Rapport visuel dans PrimeCenter
Fail → Message d'alerte, mais continue
```

**Profil 2 — Fix (Correction)**
```
Nom: "Fix_ColorConversion_FontEmbedding"
Type: Fix (modification automatique)

Corrige:
  ✓ RGB → CMYK (conversion automatique)
  ✓ Incorpore fonts manquantes
  ✓ Augmente résolution si < 300 DPI (via upsample)
  ✓ Nettoie objets invalides
  ✓ Ajuste transparences

Résultat: Fichier PDF corrigé
→ Appliqué automatiquement à chaque import
```

---

### Module 2: CUTTER OPTIONS (Table de Découpe)

**Rôle:** Configuration du cutter (table de découpe)

#### Configuration

| Paramètre | Valeur | Exemple |
|-----------|--------|---------|
| **Sélectionner cutter** | Configuré | Zünd G3 |
| **Driver** | Du cutter | ZCC / DXF / PDF |
| **Dossier sortie** | Path | `/data/output/CUT/` |
| **Connexion réseau** | (optionnel) | `192.168.1.100` |

#### Marques de Coupe (Cut Marks)

```
Configuration:
  ├─ Type: Marks externes (bords du média)
  ├─ Forme: Carrés / Croix / Cercles (selon driver)
  ├─ Taille: Standard
  ├─ Position: Corners (coins)
  └─ Couleur: Noir
```

**Résultat:** Petites marques aux coins du média pour orienter/couper manuellement

#### Cas Spéciaux

**Impression seule (pas de découpe):**
```
Laisser AUCUN cutter sélectionné
→ Seuls fichiers PDF générés
```

**Plusieurs cutters:**
```
Configurer plusieurs cutters dans Paramètres
Sélectionner défaut ou choisir à l'export
```

---

### Module 3: TRIMBOX (Recadrage)

**Rôle:** Recadrage de la boîte de coupe (cropping box)

**Utilisation pour PREFLIGHT_PAO:** ❌ NON UTILISÉ

Laissez par défaut — le trimbox s'applique seulement aux PDF qui ont déjà un trimbox défini dans le fichier source.

---

### Module 4: BLEEDING (Fond Perdu = FP) ⭐ CRITIQUE

**Rôle:** Ajouter une extension 5mm autour de l'image pour sécurité de découpe

#### Pourquoi Bleed?

```
SANS Bleed:                   AVEC Bleed 5mm:

┌─────────────────┐          ┌───────────────────────┐
│     Image       │          │ [Bleed 5mm]          │
│                 │          │ ┌──────────────────┐ │
│ Découpe exacte  │          │ │     Image        │ │
│ → Risque blanc  │          │ │   Découpe       │ │
│   après coupe   │          │ │  Pas de blanc!  │ │
│                 │          │ └──────────────────┘ │
└─────────────────┘          │ [Bleed 5mm]          │
                             └───────────────────────┘

Avantage: Tolère les imprécisions de découpe (±2-3mm)
```

#### Configuration PREFLIGHT_PAO

**Type:** Canvas (pour formes rectangulaires ET non-rectangulaires)

**Méthode:** Extend (duplique les pixels de bord)

**Dimensions:**
```
┌────────────────────────────────┐
│   [5mm] Top [5mm]             │
│ ┌─────────────────────────┐   │
│ │[5mm]  Image  [5mm]     │[5m│
│ │       Original         │m] │
│ │                        │   │
│ └─────────────────────────┘   │
│   [5mm] Bottom [5mm]          │
└────────────────────────────────┘

Paramètres à configurer:
  Top: 5 mm
  Bottom: 5 mm
  Left: 5 mm
  Right: 5 mm

Cible: Edges + Corners (couverture complète)
```

**Contours:**
```
Sélectionner contours du dictionnaire
(ex: CutContourAuto, ou nom custom)

Si vide: utilise contours existants ou auto-génère
```

#### Application du Bleed

**Automatique:**
```
✅ Appliqué à TOUS les fichiers importés
Via profil preflight ou setting recette
```

**Manuel:**
```
Gestionnaire fichiers > clic-droit > Apply Bleed
→ Utile pour appliquer après coup
```

#### Vérification du Bleed

Dans le Studio après génération:
```
✅ Image montre extension autour (zone claire/jaune)
✅ Bleed appliqué dans export PDF
✅ Taille finale = original + 10mm (5mm de chaque côté)
```

---

### Module 5: ANNOTATIONS (Identificateurs)

**Rôle:** Ajouter texte/code QR autour de l'image pour traçabilité

#### Configuration (Optionnel)

**Format:**
```
Texte + Code QR
```

**Contenu:**
```
Texte: {JobID} | {CustomerID} | Copie 1/N
Code QR: Même contenu ou timestamp

Exemple:
  ┌──────────────────────┐
  │   BAT001 | ACME      │
  │   Copie 1/3          │
  │  ┌────────────────┐  │
  │  │   QR CODE      │  │
  │  └────────────────┘  │
  │                      │
  └──────────────────────┘
```

**Position:**
```
Bottom (bas) ou Right (droite) de l'image
```

**Taille du texte:**
```
2 mm à 50 mm (ajustable)
Recommandé: 5 mm (lisible mais discret)
```

**Protection anti-coupure:**
```
✅ Activée (empêche code QR d'être coupé)
```

---

### Module 6: MIRRORING (Miroir)

**Rôle:** Inverser l'image horizontalement ou verticalement

**Utilisation pour PREFLIGHT_PAO:** ❌ NON UTILISÉ

Laissez par défaut (pas de miroir nécessaire pour BAT simples).

Le miroir ne s'applique que si impression recto-verso (DSP) — non pertinent ici.

---

### Module 7: NESTING (Imbrication)

**Rôle:** Placer optimalement les images sur le média pour réduire gaspillage

#### Type d'Imbrication

```
✅ True Shape (forme réelle)
   └─ Utilise contours réels des images
   └─ Optimisation maximale
   └─ Temps calcul: +30 sec

vs

❌ Rectangulaire (bounding box)
   └─ Utilise boîtes englobantes
   └─ Moins optimal mais plus rapide
```

**Pour PREFLIGHT_PAO:** Utiliser **True Shape**

#### Paramètres

| Paramètre | Valeur | Description |
|-----------|--------|-------------|
| **Espacement** | 5 mm | Marge minimale entre images |
| **Rotation min** | 0° | Rotation libre autorisée |
| **Rotation max** | 360° | Tous angles possibles |
| **Durée optim** | 30 sec | Temps pour calcul optimal |
| **Limit time** | 60 sec | Timeout si trop long |

#### Modèle de Nom d'Amalgame

```
{JobID}_{CustomerID}_{LayoutName}

Exemples:
  BAT001_ACME_Nest_001
  BAT002_TECHCO_Nest_001
  BAT003_DESIGN_Nest_001
```

#### Génératio Automatique (Seuils)

```
Option 1 — Couverture minimale:
  Générer layout quand ≥ 70% du média rempli

Option 2 — Délai temporel:
  Générer layout 5 minutes après dernier import

Recommandation: Combiner les deux
```

#### Ganging (Optionnel)

```
Grouper par métadonnée (ex: CustomerID)
→ Pas de mélange clients dans même layout

Utile si travaux de clients différents ne doivent pas se mélanger
```

---

### Module 8: OUTPUT (Export)

**Rôle:** Générer les fichiers finaux (impression + découpe)

#### Fichiers d'Impression

**Format:** PDF 1.7

**Dossier:** `/data/output/PRINT/` ou `C:\OUTPUT\PRINT\`

**Modèle de nommage:**
```
{JobID}_{CustomerID}_{Copies}_PRINT.pdf

Exemples:
  BAT001_ACME_3_PRINT.pdf
  BAT002_TECHCO_1_PRINT.pdf
```

**Contenu du PDF:**
```
✓ Image complète (avec bleed 5mm)
✓ Marques de coupe (coins)
✓ Annotations (optionnel)
✓ Contours de découpe (visibles)
✓ Pas de calques (flattened)
```

**Vérification:**
```
Ouvrir PDF dans Acrobat Reader
  ✓ Image visible
  ✓ Extension bleed visible
  ✓ Qualité correcte (300 DPI)
```

#### Fichiers de Découpe

**Format:** Dépend du driver
```
DXF      → Standard, compatible tous cutters
PDF      → Si PDF cutter
ZCC      → Format Zünd
SGP      → Format Summa
```

**Dossier:** `/data/output/CUT/` ou cutter folder

**Modèle de nommage:**
```
{JobID}_{CustomerID}_{Copies}_CUT.{ext}

Exemples:
  BAT001_ACME_3_CUT.dxf
  BAT002_TECHCO_1_CUT.pdf
```

**Contenu du fichier:**
```
✓ Contours de découpe (paths vectoriels)
✓ Marques de coupe (registration marks)
✓ Formes réelles (no raster image)
✓ Pas de couleur (pour découpe)
```

**Vérification:**
```
Ouvrir DXF dans AutoCAD/CAM logiciel
  ✓ Contours présents
  ✓ Marques de coupe visibles
  ✓ Pas d'image raster
```

---

## 🔄 Flux Complet de la Recette

### Vue d'Ensemble du Processus

```
ÉTAPE 1: IMPORT
└─ Fichier arrive: BAT001_ACME_3_Poster.pdf
└─ Extraction métadonnées: JobID=BAT001, CustomerID=ACME, Copies=3, JobName=Poster

ÉTAPE 2: PREFLIGHT CHECK (Vérification)
└─ Vérifie: résolution, couleurs, fonts, bleed
└─ Rapport: "OK" ou "Avertissement"

ÉTAPE 3: PREFLIGHT FIX (Correction)
└─ RGB → CMYK
└─ Incorpore fonts
└─ Augmente résolution si needed
└─ Nettoie objets invalides

ÉTAPE 4: BLEED AJOUTÉ
└─ Canvas Extend 5mm tous côtés
└─ Taille nouvelle: 1010 × 610 px (exemple)

ÉTAPE 5: NESTING (Imbrication)
└─ Optimise placement sur média
└─ Utilise True Shape
└─ Génère layout

ÉTAPE 6: CONTOURS DE DÉCOUPE
└─ Détecte contours du dictionnaire
└─ Ou génère automatiquement

ÉTAPE 7: ANNOTATIONS (optionnel)
└─ Ajoute JobID + CustomerID + QR code
└─ Position: bas/droite de l'image

ÉTAPE 8: EXPORT
├─ Fichier impression:
│  └─ BAT001_ACME_3_PRINT.pdf (avec bleed, marques)
│
└─ Fichier découpe:
   └─ BAT001_ACME_3_CUT.dxf (contours, marques)
```

---

## ⚙️ Configurations Conseillées par Cas d'Usage

### Cas 1: Impressions Simples (pas de découpe)

```
Module 2 (Cutter): AUCUN
Module 4 (Bleed): Canvas Extend 5mm (si impression au bord)
Module 5 (Annotations): Non nécessaire
Module 7 (Nesting): True Shape

Résultat: PDF impression seule
```

### Cas 2: Découpe Précise (découpeuse laser, etc.)

```
Module 2 (Cutter): Sélectionner cutter
Module 4 (Bleed): Canvas Extend 5mm (important!)
Module 5 (Annotations): Oui (traçabilité)
Module 7 (Nesting): True Shape

Résultat: PDF + DXF avec contours de découpe
```

### Cas 3: Production Haute Volume (500 BAT/jour)

```
Module 1 (Input): Hotfolder + extraction métadonnées
Module 4 (Bleed): Canvas Extend 5mm (auto)
Module 5 (Annotations): Oui (code QR pour suivi)
Module 7 (Nesting): True Shape + seuils auto
Module 8 (Output): Export semi-auto (Pro) ou full-auto (Max)

Résultat: Workflow complètement automatisé
```

---

## 🔐 Bonnes Pratiques

### Pour Fichiers d'Entrée

```
✅ Nommer avec convention: {JobID}_{CustomerID}_{Copies}_{JobName}.pdf
✅ Mode couleur: CMYK si possible (évite conversion)
✅ Résolution: 300 DPI minimum
✅ Polices: Incorporer dans fichier source
✅ Format: PDF préféré (plus stable qu'AI/PSD)
```

### Pour Utilisation de la Recette

```
✅ Sauvegarder la recette (Ctrl+S)
✅ Dupliquer pour variantes (tailles différentes)
✅ Documenter les modifications (commentaires)
✅ Tester avec fichiers d'exemple d'abord
✅ Vérifier exports avant production
```

### Pour Production (V2 Hotfolder)

```
✅ Monitorer dossier FAILED/ régulièrement
✅ Archiver fichiers traités par mois
✅ Générer rapports de production CSV
✅ Tester capacité (scaling pour 500 BAT/jour)
✅ Backup dossier OUTPUT/ régulièrement
```

---

## 📞 Troubleshooting Rapide

| Problème | Cause | Solution |
|----------|-------|----------|
| Bleed ne s'applique pas | Type Canvas Extend non sélectionné | Vérifier Module 4 type = Canvas |
| Contours non générés | Contours mal nommés dans source | Ajouter au dictionnaire |
| Métadonnées vides | Nom fichier invalide | Renommer: `{JobID}_{CustomerID}_{Copies}_{JobName}` |
| Export échoue | Dossier inexistant / pas de permission | Créer dossier, vérifier chmod 755 |
| Performance lente | Trop de fichiers, nesting trop long | Réduire taille images, augmenter timeout |

---

## 🚀 Prochaines Étapes

### V1 (Demain) — Test Manuel
- [ ] Créer recette dans PrimeCenter V4 UI
- [ ] Importer fichiers d'exemple
- [ ] Générer layouts
- [ ] Exporter et vérifier résultats
- [ ] Documenter résultats

### V2 (Production) — Automatisation Hotfolder
- [ ] Configurer hotfolder d'entrée
- [ ] Tester volume croissant (100 → 500 BAT/jour)
- [ ] Monitoring + logs
- [ ] Optimisations de performance

### V3 (Future) — Upgrade Max (si nécessaire)
- [ ] Export complètement automatisé
- [ ] Tickets XML pour ERP
- [ ] Mode silencieux (recettes en bg)
- [ ] Rapports XML avancés

---

## 📚 Documentation Associée

```
PrimeCenter/
├── docs/
│   ├── FILENAME_CONVENTION.md      → Comment nommer les fichiers
│   ├── MANUAL_TEST_GUIDE_V1.md     → Guide test demain
│   └── AUTOMATION_SETUP_V2.md      → Setup hotfolder (après V1)
├── recipes/
│   └── PREFLIGHT_PAO_PRO_CONFIGURATION.md  → Config détaillée
├── hotfolder/
│   └── README.md                   → Structure dossiers V2
└── README.md                       → Vue d'ensemble projet
```

---

**Session:** https://claude.ai/code/session_017yhksCaj1YoCEk79BwGw1G
