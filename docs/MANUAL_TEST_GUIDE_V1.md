# Guide de Test Manuel V1 — PREFLIGHT_PAO_PRO

**Objectif:** Créer et tester manuellement la recette dans PrimeCenter V4
**Timeline:** Demain (test manuel)
**Status:** À suivre étape par étape

---

## 🎯 Objectif Final

À la fin de ce guide, vous aurez:
- ✅ Une recette fonctionnelle `PREFLIGHT_PAO_PRO`
- ✅ Fichiers d'impression (PDF) avec bleed 5mm
- ✅ Fichiers de découpe (DXF/PDF) avec contours
- ✅ Métadonnées extraites automatiquement des noms de fichiers

---

## 📋 Prérequis

Avant de commencer:
- ✅ PrimeCenter V4 PRO installé et fonctionnel
- ✅ Cutters configurés (ou planifier impression seule)
- ✅ Fichiers d'exemple prêts (PDF, PSD, JPG, PNG)
- ✅ Dossiers de sortie créés
- ✅ Accès à cette documentation

**Fichiers d'exemple recommandés:**
```
BAT001_ACME_3_Poster.pdf
BAT002_TECHCO_1_Banner.psd
BAT003_DESIGN_2_Brochure.jpg
```

---

## 🚀 Étape 1: Créer la Recette

### 1.1 Lancer PrimeCenter V4

```
Écran d'accueil
├── Nouvelle recette
├── Modèle de recette
└── Tutoriels
```

**Action:** Cliquer sur **Nouvelle recette** ou **+ (nouvel onglet)**

### 1.2 Nommer la Recette

Dans le panneau latéral gauche ou la barre d'onglets:
- **Nom:** `PREFLIGHT_PAO_PRO`
- **Description:** (optionnel) `Automatisation vérification et préparation BAT`

**Sauvegarder:** Ctrl+S ou via le menu

---

## 🔧 Étape 2: Configuration — Module INPUT

### 2.1 Accéder aux Paramètres d'Import

```
Recette PREFLIGHT_PAO_PRO
└── Panneau gauche: onglet "Fichiers"
    └── Paramètres d'import
```

### 2.2 Extraction de Métadonnées

**Section:** "Import parameters" ou "File properties"

**Activer extraction:**
- [ ] Cocher ☑️ "Extract properties from filename"

**Modèle d'extraction:**
```
{JobID}_{CustomerID}_{Copies}_{JobName}
```

> Copier-coller ce texte exactement dans le champ

**Résultat attendu:**
```
Fichier: BAT001_ACME_3_Poster.pdf
         ↓ Extraction
         - JobID: BAT001
         - CustomerID: ACME
         - Copies: 3
         - JobName: Poster
```

### 2.3 Profils de Vérification/Correction

**Section:** "Preflight profiles" ou "Input fixup"

#### Profil 1 — Vérification (Check)

**Ajouter profil:**
1. Cliquer sur **+ Ajouter profil**
2. Chercher "Check" ou "Verify"
3. Sélectionner profil contenant:
   - `Check_PDFStandard` ou `Verify_Colors_Fonts` ou similaire
   - → Chercher "Verify Basic Files" (V4.1+)

**Configuration (si paramétrable):**
- ✅ Vérifier résolution (300 DPI minimum)
- ✅ Vérifier mode couleur (CMYK)
- ✅ Vérifier polices
- ✅ Vérifier bleed

**Ordre:** Premier dans la liste (Check avant Fix)

#### Profil 2 — Correction (Fix)

**Ajouter profil:**
1. Cliquer sur **+ Ajouter profil**
2. Chercher "Fix" ou "Fixup"
3. Sélectionner profil contenant:
   - `Fix_Colors` ou `Fixup_ColorConversion`
   - `Fix_Fonts` ou `Fixup_FontEmbedding`
   - → Combiner ou chercher profil unifié

**Configuration (si paramétrable):**
- ✅ Convertir RGB → CMYK
- ✅ Incorporer polices
- ✅ Corriger résolution
- ✅ Nettoyer contours invalides

**Ordre:** Deuxième dans la liste (après Check)

**Résultat:** Les profils s'appliqueront automatiquement à chaque fichier importé

---

## 🔪 Étape 3: Configuration — Module CUTTER OPTIONS

### 3.1 Sélectionner un Cutter (ou passer si impression seule)

```
Recette PREFLIGHT_PAO_PRO
└── Panneau gauche: onglet "Layout"
    └── Cutter options
        └── Sélectionner cutter
```

**Options:**
- Si vous avez un cutter (Zünd, Summa, etc.): Sélectionner dans la liste
- Si **impression seule**: Laisser "Aucun" ou "PDF Cutter"

### 3.2 Configurer Marques de Coupe

**Section:** "Cut marks" ou "Cutting options"

Si cutter sélectionné:
- **Type:** Marks externes (bords)
- **Forme:** Carrés (ou selon driver disponible)
- **Taille:** Standard
- **Position:** Corners (coins)

**Si pas de cutter:** Cette section est optionnelle, passer

---

## 📏 Étape 4: Configuration — Module BLEEDING (IMPORTANT!)

### 4.1 Accéder aux Outils de Mise en Page

```
Recette PREFLIGHT_PAO_PRO
└── Panneau gauche: onglet "Layout"
    └── "Outils de mise en page et d'édition"
        └── "Canvas Bleeding" ou "Bleed & Crop"
```

### 4.2 Activer et Configurer le Bleed

**Type de Bleed:**
- [ ] Sélectionner **"Canvas"** (pas "Shape")

**Méthode:**
- [ ] Sélectionner **"Extend"** (duplique pixels de bord)

**Dimensions (CRITIQUES):**
- [ ] Top: **5 mm**
- [ ] Bottom: **5 mm**
- [ ] Left: **5 mm**
- [ ] Right: **5 mm**

> ⚠️ **IMPORTANT:** Tous les côtés à 5mm!

**Cible:**
- [ ] Sélectionner **"Edges + Corners"** (couverture complète)

**Contours:**
- [ ] Sélectionner contour du dictionnaire (ex: `CutContourAuto`)
- [ ] Ou laisser vide si auto-généré

**Sauvegarder:** Confirmer configuration

---

## 🧩 Étape 5: Configuration — Module NESTING

### 5.1 Accéder aux Paramètres de Nesting

```
Recette PREFLIGHT_PAO_PRO
└── Panneau gauche: onglet "Layout"
    └── "Outils de mise en page"
        └── "True Shape Nesting" (déjà actif par défaut)
```

### 5.2 Configuration de Base

**Type:** True Shape (déjà sélectionné)

**Paramètres:**

| Paramètre | Valeur | Action |
|-----------|--------|--------|
| Espacement | 5 mm | Garder par défaut |
| Rotation min | 0° | Permettre rotation libre |
| Rotation max | 360° | Angles multiples |
| Durée optim | 30 sec | Temps pour calcul |

**Modèle de Nom:**
```
{JobID}_{CustomerID}_{LayoutName}
```

Ou laisser par défaut (ex: `Nest_001`, `Nest_002`)

---

## 📤 Étape 6: Configuration — MODULE OUTPUT

### 6.1 Paramètres d'Exportation

```
Recette PREFLIGHT_PAO_PRO
└── Panneau droit: "Export settings"
    └── Fichiers d'impression & découpe
```

### 6.2 Fichiers d'Impression (PDF)

**Dossier de sortie:**
```
Défaut: C:\Users\[user]\PrimeCenter\Output\Print\
Ou définir chemin: /data/output/PRINT/
```

**Modèle de nommage:**
```
{JobID}_{CustomerID}_{Copies}_PRINT.pdf
```

**Options:**
- ✅ Include bleed
- ✅ Include cut contours
- ✅ Include cut marks

### 6.3 Fichiers de Découpe

**Dossier de sortie:**
```
Défaut: [Dossier cutter configuré]
Ou définir: /data/output/CUT/
```

**Modèle de nommage:**
```
{JobID}_{CustomerID}_{Copies}_CUT.dxf
```

> Extension dépend du driver (`.dxf`, `.pdf`, `.zcc`, `.sgp`)

---

## ✅ Étape 7: Importer Fichiers d'Exemple

### 7.1 Préparer Fichiers d'Exemple

**Créer 3 fichiers de test:**
```
BAT001_ACME_3_Poster.pdf
BAT002_TECHCO_1_Banner.psd
BAT003_DESIGN_2_Brochure.jpg
```

### 7.2 Importer Manuellement

**Action:**
```
Recette PREFLIGHT_PAO_PRO
└── Panneau gauche: onglet "Fichiers"
    └── Gestionnaire de fichiers
        └── Bouton "Ouvrir" ou Ctrl+O
```

**Sélectionner les fichiers:**
- [ ] BAT001_ACME_3_Poster.pdf
- [ ] BAT002_TECHCO_1_Banner.psd
- [ ] BAT003_DESIGN_2_Brochure.jpg

**Cliquer:** Open / Ouvrir

### 7.3 Vérifier Extraction de Métadonnées

**Après import**, dans le gestionnaire de fichiers:
- [ ] Sélectionner `BAT001_ACME_3_Poster.pdf`
- [ ] Panneau d'infos à droite:
  ```
  Propriétés:
  - JobID: BAT001 ✓
  - Customer ID: ACME ✓
  - Copies: 3 ✓
  - Job name: Poster ✓
  ```

> Si métadonnées absentes, vérifier modèle d'extraction

---

## 🔄 Étape 8: Générer les Layouts

### 8.1 Insérer les Fichiers dans le Studio

**Action:**
```
Gestionnaire de fichiers (gauche)
└── Sélectionner: BAT001_ACME_3_Poster.pdf
└── Bouton "Insérer" ou Entrée
    ou Drag & Drop vers Studio (centre)
```

**Résultat:** Image apparaît dans le Studio

### 8.2 Générer les Layouts

**Action:**
```
Studio (centre)
└── Bouton "Générer" (ou Generate)
```

**Processus:**
1. Preflight Check (vérification)
2. Preflight Fix (correction)
3. Bleed appliqué (5mm)
4. Nesting (imbrication)
5. Layout généré

**Résultat:** Mise en page affichée dans le Studio

**Durée attendue:** 5-30 secondes selon taille

### 8.3 Prévisualiser

**Dans le Studio:**
- [ ] Vérifier présence du **bleed 5mm** (zone jaune/orange généralement autour de l'image)
- [ ] Vérifier **contours de découpe** (lignes vectorielles si présentes)
- [ ] Vérifier **marques de coupe** (petites marques aux coins si cutter sélectionné)

---

## 📤 Étape 9: Exporter Manuellement

### 9.1 Accéder aux Actions d'Export

```
Panneau droit: "Layouts"
└── Liste des mises en page générées
    └── Sélectionner layout
        └── Boutons d'action
            ├── Print
            ├── Cut
            └── Print & Cut
```

### 9.2 Exporter les Fichiers

**Option 1 — Impression seule:**
- [ ] Cliquer **Print**
- [ ] Fichier PDF généré:
  ```
  BAT001_ACME_3_PRINT.pdf
  ```
  vers dossier OUTPUT/PRINT/

**Option 2 — Découpe seule:**
- [ ] Cliquer **Cut**
- [ ] Fichier découpe généré:
  ```
  BAT001_ACME_3_CUT.dxf
  ```
  vers dossier OUTPUT/CUT/

**Option 3 — Les deux:**
- [ ] Cliquer **Print & Cut**
- [ ] Les deux fichiers générés

### 9.3 Vérifier les Fichiers Générés

**Fichier d'impression (PDF):**
```
Ouvrir: BAT001_ACME_3_PRINT.pdf
Vérifier:
✅ Image présente
✅ Bleed 5mm visible (zone étendue)
✅ Marques de coupe aux coins
✅ Annotations (JobID, CustomerID) optionnel
```

**Fichier de découpe (DXF):**
```
Ouvrir dans: AutoCAD, DXF viewer, ou Zünd Center
Vérifier:
✅ Contours de découpe présents
✅ Marques de coupe
✅ Pas d'image raster (seulement vecteurs)
```

---

## 📊 Étape 10: Validation & Troubleshooting

### 10.1 Checklist de Validation

- [ ] Métadonnées extraites correctement
- [ ] Bleed 5mm appliqué à tous les côtés
- [ ] Contours de découpe détectés/générés
- [ ] PDF impression généré avec bleed
- [ ] Fichier découpe généré avec contours
- [ ] Marques de coupe présentes
- [ ] Nommage fichiers correct

### 10.2 Problèmes Courants & Solutions

#### ❌ Métadonnées non extraites

**Symptôme:** JobID, CustomerID, etc. vides dans properties

**Causes possibles:**
1. Modèle d'extraction mal configuré
2. Nom du fichier ne respecte pas convention

**Solutions:**
1. [ ] Vérifier modèle: `{JobID}_{CustomerID}_{Copies}_{JobName}`
2. [ ] Renommer fichier: `BAT001_ACME_3_Poster.pdf`
3. [ ] Réimporter le fichier
4. [ ] Vérifier case-sensitivity (majuscules/minuscules)

#### ❌ Bleed ne s'applique pas

**Symptôme:** Image sans extension bleed dans l'export

**Causes possibles:**
1. Type Canvas Extend non sélectionné
2. Valeurs bleed à 0mm
3. Profil preflight efface le bleed

**Solutions:**
1. [ ] Vérifier type: Canvas (pas Shape Extend)
2. [ ] Vérifier valeurs: 5mm tous côtés
3. [ ] Appliquer manuellement: clic-droit fichier > Apply Bleed
4. [ ] Vérifier profil Fix n'efface pas bleed

#### ❌ Contours de découpe non détectés

**Symptôme:** Pas de contours dans fichier DXF généré

**Causes possibles:**
1. Contours mal nommés dans fichier PDF
2. Contours non dans dictionnaire
3. Contours pas en traits vectoriels

**Solutions:**
1. [ ] Vérifier nom contours dans fichier: `CutContour`, `CutLine`, etc.
2. [ ] Ajouter au dictionnaire:
   ```
   Paramètres > Dictionnaire > Ajouter > NOM_CONTOUR
   ```
3. [ ] Vérifier fichier: contours = traits (strokes), pas remplissages
4. [ ] Utiliser profil Fix pour générer automatiquement

#### ❌ Export ne crée pas de fichier

**Symptôme:** Bouton "Print" ou "Cut" ne fait rien

**Causes possibles:**
1. Dossier de sortie n'existe pas
2. Pas de permission d'écriture
3. Cutter non configuré (pour Cut)
4. Layout verrouillé

**Solutions:**
1. [ ] Créer dossier: `/data/output/PRINT/` et `/data/output/CUT/`
2. [ ] Vérifier permissions: dossier accessible en lecture/écriture
3. [ ] Vérifier cutter sélectionné (pour découpe)
4. [ ] Déverrouiller layout: clic-droit > Unlock

---

## 🎉 Résultat Final Attendu (V1)

À la fin du test manuel:

```
Structure générée:
├── Recette PREFLIGHT_PAO_PRO (sauvegardée)
├── Fichiers générés:
│   ├── /data/output/PRINT/BAT001_ACME_3_PRINT.pdf ✅
│   ├── /data/output/PRINT/BAT002_TECHCO_1_PRINT.pdf ✅
│   ├── /data/output/PRINT/BAT003_DESIGN_2_PRINT.pdf ✅
│   ├── /data/output/CUT/BAT001_ACME_3_CUT.dxf ✅
│   ├── /data/output/CUT/BAT002_TECHCO_1_CUT.dxf ✅
│   └── /data/output/CUT/BAT003_DESIGN_2_CUT.dxf ✅
└── Résultats:
    ✅ Métadonnées extraites
    ✅ Bleed 5mm appliqué
    ✅ Contours de découpe ajoutés
    ✅ Marques de coupe présentes
    ✅ Nommage fichiers cohérent
```

---

## 🚀 Prochaine Étape: V2 (Automatisation)

Une fois V1 validée:
1. Configurer hotfolder d'entrée
2. Passer en semi-automatique (import auto)
3. Tester avec 100+ fichiers
4. Atteindre 500 BAT/jour

→ Voir `docs/AUTOMATION_SETUP_V2.md`

---

**Session:** https://claude.ai/code/session_017yhksCaj1YoCEk79BwGw1G
