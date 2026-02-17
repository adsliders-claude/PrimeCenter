# Recettes PrimeCenter — 5 Types Documentés
**Système:** PrimeCenter V4 PRO
**Version:** 1.0 — Fév 2026
**Contexte:** Chaque type de produit = 2 recettes (BAT validation + PROD amalgame)

---

## 🗺️ Vue d'Ensemble des Recettes

```
5 TYPES DE PRODUITS:                    2 VERSIONS PAR TYPE:

1. PREFLIGHT_PAO          →  BAT: PREFLIGHT_PAO_BAT (validation 1 visuel)
   (impression standard)      PROD: PREFLIGHT_PAO_PROD (amalgame)

2. IMPRESSION_DIRECTE     →  BAT: IMPRESSION_DIRECTE_BAT
   (print + cut simple)       PROD: IMPRESSION_DIRECTE_PROD

3. IMPRESSION_VITRINE     →  BAT: IMPRESSION_VITRINE_BAT
   (vitrine multi-lés)        PROD: IMPRESSION_VITRINE_PROD

4. VITROPHANIE_STICKERS   →  BAT: VITROPHANIE_STICKERS_BAT
   (avec blanc + miroir)      PROD: VITROPHANIE_STICKERS_PROD

5. IMPRESSION_BACHE       →  BAT: IMPRESSION_BACHE_BAT
   (bâche + oeillets)         PROD: IMPRESSION_BACHE_PROD

TOTAL: 10 recettes à créer dans PrimeCenter
```

---

## ✅ RÈGLE GLOBALE: BAT vs PROD

```
BAT (Bon À Tirer):
  → 1 seul visuel unique
  → Résultat: 1 PDF pour validation client
  → Pas d'amalgame
  → Dossier sortie: 02_OUTPUT_PREFLIGHT_FIXUP

PROD (Production):
  → Amalgame par gangName (même matière)
  → Nesting optimisé (True Shape)
  → Groupement par: gangName + recette type
  → Résultat: 1 amalgame multi-visuels
  → Dossier sortie: 04 - OUTPUT_PRINTFILES + 04 - OUTPUT_CUTFILES
```

---

## 1️⃣ PREFLIGHT_PAO — Validation BAT Standard

**Usage:** Vérification et correction générale du fichier client avant validation

### Paramètres spécifiques:
```
Fond perdu:        5mm tous côtés (Canvas Extend)
Blanc:             ❌ Non
Miroir:            ❌ Non
Renfort:           ❌ Non
Oeillets:          ❌ Non
CutContour:        ✅ Oui (si présent dans fichier source)
Ton direct:        ❌ Non
Façonnage:         ❌ Non
Encre blanc:       ❌ Non
```

### Configuration Modules:
```
Module 1 — INPUT:
  Formats: PDF, PSD, JPG, PNG
  Extraction: {orderId}_{jobId}_{jobName}_{gangName}_{formatWidth}x{formatHeightmm_{copies}ex
  Preflight Check: Verify_Colors_Resolution_Fonts
  Preflight Fix: Fix_RGB_CMYK + Fix_FontEmbedding + Fix_Resolution300

Module 4 — BLEEDING:
  Type: Canvas Extend
  Méthode: Extend (répliquer pixels bord)
  Dimensions: 5mm (top, bottom, left, right)
  Cible: Edges + Corners

Module 7 — NESTING (BAT uniquement):
  Type: Rectangulaire (pas True Shape pour BAT rapide)
  1 seul visuel → pas vraiment de nesting

Module 8 — OUTPUT:
  Impression: {orderId}_{jobId}_{jobName}_{gangName}_{formatWidth}x{formatHeight}mm_{copies}ex_BAT.pdf
  Dossier: 02_OUTPUT_PREFLIGHT_FIXUP
  Rapport: 06 - RAPPORTS PRIMECENTER\{orderId}_{jobId}_rapport.xml
```

### ⚡ Version PROD (PREFLIGHT_PAO_PROD):
```
Différences vs BAT:
  Module 7 — NESTING: True Shape (optimisation maximale)
  Module 7 — Groupage: par gangName
  Module 7 — Seuil auto: 70% couverture OU 5 minutes délai
  Module 8 — OUTPUT:
    Dossier: 04 - OUTPUT_PRINTFILES
    Ticket XML: 06 - RAPPORTS PRIMECENTER
```

---

## 2️⃣ IMPRESSION_DIRECTE — Print + Cut Standard

**Usage:** Impression + découpe sans façonnage, sans blanc, sans ton direct

### Paramètres spécifiques:
```
Fond perdu:        5mm tous côtés (Canvas Extend)
Blanc:             ❌ Non (pas d'encre blanc)
Miroir:            ❌ Non
Renfort:           ❌ Non
Oeillets:          ❌ Non
CutContour:        ✅ Oui (obligatoire pour découpe)
Ton direct:        ❌ Non
Façonnage:         ❌ Non (découpe simple)
Encre blanc:       ❌ Non
```

### Cas d'usage typique:
```
Produits: Stickers standards, enseignes, signalétique simple,
          panneaux PVC, kakémonos simples, roll-ups standard

Exemple nomenclature:
012345_001_ImprimDirect_Vinyl80_200x300mm_50ex.pdf
```

### Configuration Modules:
```
Module 2 — CUTTER:
  Cutter: [selon matériel atelier]
  Marques de coupe: Coins, forme standard
  CutContour: Dictionnaire → CutContour / CutLine / SpotColor_Découpe

Module 4 — BLEEDING:
  Type: Canvas Extend
  5mm tous côtés

Module 5 — ANNOTATIONS:
  Texte: {orderId} | {jobName} | {copies}ex
  QR Code: Oui (traçabilité atelier)
  Position: Bas de l'image

Module 8 — OUTPUT:
  Impression: {orderId}_{jobId}_{jobName}_{gangName}_{format}_PRINT.pdf
  Découpe: {orderId}_{jobId}_{jobName}_{gangName}_{format}_CUT.dxf
```

### ⚡ Version PROD (IMPRESSION_DIRECTE_PROD):
```
Nesting True Shape par gangName
Groupage: même matière → même amalgame
Export simultané: PRINT.pdf + CUT.dxf
```

---

## 3️⃣ IMPRESSION_VITRINE — Vitrine avec Lés

**Usage:** Vitrine de magasin, grande surface, avec recouvrement pour assemblage

### Paramètres spécifiques:
```
Fond perdu:        ASYMÉTRIQUE!
  - Haut: 2cm (20mm) — recouvrement assemblage
  - Bas: 5cm (50mm) — repli sous vitrine ou pied
  - Droite: 5cm (50mm) — repli latéral ou fenêtre
  - Gauche: 5mm standard (ou 5cm selon montage)

Blanc:             ❌ Non
Miroir:            ❌ Non
CutContour:        ✅ Oui
Lés:               ✅ Oui — découpage en bandes verticales
Nombre de lés:     Selon largeur totale ÷ largeur max imprimante
```

### Règle des Lés:
```
Largeur visuel: 3600mm
Largeur max imprimante: 1300mm

→ Nombre de lés: 3 (3 × 1200mm avec 2 × 2cm recouvrement)

Calcul:
  Lé 1: 1200mm (0 à 1200)
  Recouvrement: 20mm
  Lé 2: 1220mm (1180 à 2400)
  Recouvrement: 20mm
  Lé 3: 1220mm (2380 à 3600)

PrimeCenter calcule automatiquement avec module Tiling/Lés
```

### Configuration Modules:
```
Module 1 — INPUT:
  Même que standard + paramètre lés actif

Module 3 — TRIMBOX / TILING (lés):
  Activer: Tiling / Découpage en lés
  Largeur max lé: [largeur max imprimante - 2×recouvrement]
  Recouvrement: 20mm (2cm)
  Répétition: Automatique

Module 4 — BLEEDING (ASYMÉTRIQUE):
  Top: 20mm (2cm — recouvrement haut)
  Bottom: 50mm (5cm — repli bas)
  Right: 50mm (5cm — repli droit)
  Left: 5mm standard (OU 50mm selon installation)
  Type: Canvas Extend

Module 8 — OUTPUT:
  Nommage lé: {orderId}_{jobId}_{jobName}_Le{N}_{gangName}_{format}.pdf
  Exemple: 012345_001_Vitrine_Le1_Orange02_1210x650mm_20ex_PRINT.pdf
```

### Cas d'usage:
```
Vitrine de Noël 3.6m × 2.4m en 3 lés:
012345_001_Vitrine_Noel_Orange02_3600x2400mm_1ex.pdf
→ Génère:
  012345_001_Vitrine_Noel_Le1_Orange02_1210x2400mm_1ex_PRINT.pdf
  012345_001_Vitrine_Noel_Le2_Orange02_1210x2400mm_1ex_PRINT.pdf
  012345_001_Vitrine_Noel_Le3_Orange02_1210x2400mm_1ex_PRINT.pdf
```

---

## 4️⃣ VITROPHANIE_STICKERS — Avec Blanc + Miroir

**Usage:** Stickers vitrophanie, impressions sur supports transparents avec couche blanche dessous

### Paramètres spécifiques:
```
Fond perdu:        5mm tous côtés (Canvas Extend)
Blanc:             ✅ Oui — couche blanche sous le visuel
Miroir:            ✅ Oui — impression en miroir (vue de face = endroit)
CutContour:        ✅ Oui
Ton direct:        ❌ Non
Façonnage:         ❌ Non
```

### Pourquoi Miroir + Blanc?
```
Vitrophanie = impression vue de l'EXTÉRIEUR du magasin:
  → Le client voit l'image DEPUIS DEHORS
  → L'image est posée CÔTÉ INTÉRIEUR de la vitre
  → Donc impression miroir (horizontalement)
  → Couche blanche DESSUS (entre image et vitre) pour opacité

Ordre des couches:
  [Vitre]
  [Image en miroir] ← imprimée côté intérieur
  [Couche blanche]  ← pour opacité et blanc
  [Support vitrophanie]
```

### Configuration Modules:
```
Module 4 — BLEEDING:
  5mm tous côtés standard

Module 6 — MIRRORING:
  Type: Horizontal (gauche/droite inversé)
  Activer: ✅ Oui

Module Blanc (White ink — si imprimante compatible):
  Calque blanc: Sous le visuel (White underlay)
  Densité: 100% (opacité max)
  Surprint: White below CMYK

Module 8 — OUTPUT:
  Fichier impression: Inclut calque blanc + miroir
  Fichier découpe: Contours réels (pas miroir)
```

### Attention imprimantes:
```
⚠️ La couche blanche nécessite une imprimante avec tête blanc (W)
   Exemples: Roland SOLJET, Mimaki UCJV, Mutoh ValueJet W

⚠️ Vérifier avec atelier que l'imprimante supporte le blanc
   avant d'activer cette recette
```

---

## 5️⃣ IMPRESSION_BACHE — Bâche avec Oeillets

**Usage:** Bâches grand format pour extérieur, banderoles, affichage temporaire

### Paramètres spécifiques:
```
Fond perdu:        PERSONNALISÉ selon renfort:
  - Renfort périmétral = fond perdu = épaisseur renfort (ex: 30mm)
  - Sans renfort: 5mm standard

Blanc:             ❌ Non
Miroir:            ❌ Non
CutContour:        ✅ Oui
Renfort périmétral: ✅ Oui — bord renforcé pour oeillets
Oeillets:          ✅ Oui — tous les 250mm sur le périmètre
Ton direct:        ❌ Non
```

### Règle des Oeillets:
```
Position: Tous les 250mm sur TOUT le périmètre
Type: Oeillets métalliques soudés ou sertis
Taille standard: ⌀ 30mm (diamètre oeillet)

Calcul automatique PrimeCenter:
  Périmètre = 2 × (largeur + hauteur)
  Nombre oeillets = périmètre ÷ 250mm (arrondi)
  Premier oeillet: 125mm du coin (= 250mm ÷ 2)
  Repères: Affichés sur fichier découpe

Exemple bâche 3000 × 1500mm:
  Périmètre = 2 × (3000 + 1500) = 9000mm
  Oeillets = 9000 ÷ 250 = 36 oeillets
  Sur 3000mm de large: 13 oeillets
  Sur 1500mm de haut: 7 oeillets de chaque côté
```

### Renfort Périmétral:
```
Type: Bord replié et soudé (thermosoudé ou cousu)
Largeur standard: 30mm (possibilité 25mm ou 40mm)
Matière renfort: Même bâche ou renfort PVC renforcé
Position: Tout le tour

PrimeCenter:
  → Le fond perdu = largeur du renfort (30mm)
  → Le module Bleed crée l'extension pour le repli
  → Les repères oeillets sont dans la zone de renfort
```

### Configuration Modules:
```
Module 4 — BLEEDING:
  Type: Canvas Extend
  Dimensions: 30mm tous côtés (renfort)
  OU différencié selon côtés si nécessaire

Module spécifique Oeillets (si disponible dans PrimeCenter):
  Espacement: 250mm
  Taille: ⌀ 30mm
  Position: Périmètre complet
  Premier oeillet: 125mm des coins

Module 2 — CUTTER:
  CutContour pour forme finale
  Repères oeillets: Inclus dans DXF/ZCC

Module 8 — OUTPUT:
  Impression: {orderId}_{jobId}_Bache_{gangName}_{format}_PRINT.pdf
  Découpe + oeillets: {orderId}_{jobId}_Bache_{gangName}_{format}_CUT.dxf
```

### Cas d'usage:
```
Bâche publicitaire extérieure:
012345_007_Bache_Bache550_3000x1500mm_2ex.pdf

→ Génère:
  012345_007_Bache_Bache550_3000x1500mm_2ex_PRINT.pdf (avec renfort 30mm)
  012345_007_Bache_Bache550_3000x1500mm_2ex_CUT.dxf (avec 36 repères oeillets)
```

---

## 📋 Tableau Comparatif des 5 Recettes

| Paramètre | PAO_PREFLIGHT | IMPR_DIRECTE | VITRINE | VITROPHANIE | BACHE |
|-----------|:---:|:---:|:---:|:---:|:---:|
| **Fond perdu (FP)** | 5mm | 5mm | Asym. | 5mm | 30mm |
| **Blanc (W)** | ❌ | ❌ | ❌ | ✅ | ❌ |
| **Miroir** | ❌ | ❌ | ❌ | ✅ | ❌ |
| **Lés** | ❌ | ❌ | ✅ | ❌ | ❌ |
| **Oeillets** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Renfort** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **CutContour** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Ton direct** | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Façonnage** | ❌ | ❌ | ❌ | ❌ | ❌ |

---

## 🎯 Comment Choisir la Bonne Recette?

L'Agent LLM utilise cette logique pour choisir automatiquement:

```python
def choisir_recette(job_name: str, white: bool, mirror: bool,
                    lés: bool, oeillets: bool) -> str:
    if white or mirror:
        return "VITROPHANIE_STICKERS"
    elif lés:
        return "IMPRESSION_VITRINE"
    elif oeillets:
        return "IMPRESSION_BACHE"
    elif job_name in ["ImprimDirect", "Sticker", "Kakemono", "RollUp"]:
        return "IMPRESSION_DIRECTE"
    else:
        return "PREFLIGHT_PAO"  # Défaut

# Version BAT ou PROD:
def version_recette(recette: str, mode: str) -> str:
    return f"{recette}_{'BAT' if mode == 'bat' else 'PROD'}"
```

---

**Session:** https://claude.ai/code/session_017yhksCaj1YoCEk79BwGw1G
