# Configuration Détaillée: PREFLIGHT_PAO_PRO

**Recette:** PREFLIGHT_PAO_PRO
**Version:** PrimeCenter V4 PRO
**Date:** 2025-02-12
**Status:** À tester demain (V1 Manuel)

---

## 📋 Les 8 Modules d'une Recette

```
1. INPUT                    → Import fichiers + métadonnées
2. CUTTER OPTIONS          → Configuration table de découpe
3. TRIMBOX                 → Recadrage (pas utilisé ici)
4. BLEEDING                → Fond perdu 5mm
5. ANNOTATIONS             → Annotations (optionnel)
6. MIRRORING               → Miroir (pas nécessaire)
7. NESTING                 → Imbrication (True Shape)
8. OUTPUT                  → Export impression + découpe
```

---

## 🔧 Module 1: INPUT (Import & Métadonnées)

### Configuration Générale
- **Recette:** `PREFLIGHT_PAO_PRO`
- **Hotfolder:** (V2) `/data/hotfolder_input/` ou `C:\INPUT\BAT\`
- **Traitement:** Automatique (fichiers importés auto du hotfolder)

### Extraction de Métadonnées depuis Noms de Fichiers
**Activer:** ✅ Oui
**Modèle:**
```
{JobID}_{CustomerID}_{Copies}_{JobName}
```

**Paramètres d'import:**
- **Extraction modèle:** Actif
- **Action succes:** Déplacer vers `/data/hotfolder_input/DONE/`
- **Action échec:** Déplacer vers `/data/hotfolder_input/FAILED/`
- **Copies par défaut:** 1 (overridden par extraction si trouvé)

### Profils de Vérification/Correction (Preflight) EN ENTRÉE
**Profil 1 — Vérification (Check):**
- **Nom:** `Check_PDFStandard_Colors_Fonts`
- **Action:** Check (vérification sans modification)
- **Paramètres:**
  - ✅ Vérifier résolution (300 DPI minimum pour impression)
  - ✅ Vérifier mode couleur (CMYK ou Spot)
  - ✅ Vérifier polices incorporées
  - ✅ Vérifier bleed existant
- **Génère:** Rapport visuel dans PrimeCenter

**Profil 2 — Correction (Fix):**
- **Nom:** `Fix_ColorConversion_FontEmbedding`
- **Action:** Fix (correction automatique)
- **Paramètres:**
  - ✅ Convertir RGB → CMYK si nécessaire
  - ✅ Incorporer polices manquantes
  - ✅ Corriger résolution si < 300 DPI
  - ✅ Nettoyer contours invalides
- **Génère:** PDF corrigé en sortie

### Fichiers d'Entrée Acceptés
```
✅ PDF (.pdf)          — Format recommandé
✅ PSD (.psd)          — Photoshop
✅ JPG (.jpg, .jpeg)   — Raster
✅ PNG (.png)          — Raster avec alpha
```

**Formats NON acceptés:**
```
❌ Fichiers protégés par mot de passe
❌ SVG (vectoriel léger)
❌ GIF (animation)
```

---

## 🔪 Module 2: CUTTER OPTIONS (Table de Découpe)

### Configuration Cutters
**Prérequis:** Un ou plusieurs cutters configurés dans Paramètres

**Paramètres par Cutter (exemple Zünd):**
- **Nom:** `Zund_G3_LargeFormat`
- **Fabricant:** Zünd
- **Modèle:** G3
- **Driver:** Zünd Cut Center (ZCC)
- **Dossier de sortie:** `/data/hotfolder_output/CUT/` ou `C:\OUTPUT\CUT\`
- **Connexion réseau:** (si disponible) adresse IP du cutter

**Marques de Coupe (Cut Marks):**
- **Type:** Marks externes (bords du média)
- **Forme:** Carrés (ou selon driver)
- **Taille:** Standard
- **Couleur:** Noir

**Options avancées (si plusieurs cutters):**
- Sélectionner le cutter par défaut pour cette recette
- Ou laisser manuelle (choix à l'export)

### Cas: Pas de Découpe (Impression Seule)
Si vous ne voulez pas de fichier de découpe:
- **Laisser AUCUN cutter sélectionné** → seuls PDF d'impression générés

---

## 📏 Module 3: TRIMBOX (Recadrage)

### Configuration
**Utilisation:** Non nécessaire pour cette recette
**Paramètre:** Désactivé ou par défaut

> Le trimbox ne s'applique que sur les PDF — nos fichiers auront déjà les bonnes dimensions

---

## 🩸 Module 4: BLEEDING (Fond Perdu = FP)

### ✅ CONFIGURATION PRINCIPALE POUR PREFLIGHT_PAO

**Type de Bleed:** Canvas (pour formes rectangulaires et non-rectangulaires)

**Méthode de Génération:**
```
✅ Extend (duplique les pixels de bord)
```

**Configuration des Dimensions:**
```
┌─────────────────┐
│   Document      │  ← Image originale
│                 │
└─────────────────┘

┌─────────────────────────────────┐
│  [5mm] Bleed Extension [5mm]   │
│  ┌─────────────────┐            │
│  │   Document      │            │
│  │                 │            │
│  └─────────────────┘            │
│  [5mm] Bleed Extension [5mm]   │
└─────────────────────────────────┘
```

**Paramètres à Configurer:**
- **Top:** `5 mm`
- **Bottom:** `5 mm`
- **Left:** `5 mm`
- **Right:** `5 mm`
- **Cible:** `Edges + Corners` (couvrir complètement)
- **Contours:**
  - Sélectionner `CutContourAuto` (auto-généré)
  - Ou sélectionner contours spécifiques du dictionnaire

**Application du Bleed:**
- **Automatique:** ✅ Appliqué à TOUS les fichiers importés
- **Manuel:** Possible via clic-droit sur fichier dans gestionnaire

---

## 🏷️ Module 5: ANNOTATIONS (Identificateurs)

### Configuration (Optionnel mais Recommandé)

**Format d'Annotation:**
```
Texte + Code Optique (QR code)
```

**Contenu du Texte:**
```
{JobID} | {CustomerID} | Copie 1/N
Exemple: BAT001 | ACME | Copie 1/3
```

**Contenu du Code QR:**
```
Same as text
ou
{JobID}_{Date}_{Timestamp}
```

**Position:**
- `Bottom` (bas de l'image)
- `Right` (à droite de l'image)

**Taille du texte:** `5 mm` (lisible mais discret)

**Protection Anti-Coupure:** ✅ Activée

---

## 🔄 Module 6: MIRRORING (Miroir)

### Configuration
**Utilisation:** Non nécessaire pour cette recette
**Paramètre:** Désactivé par défaut

> Le miroir ne s'applique que sur l'impression recto-verso (DSP) — non applicable ici

---

## 🧩 Module 7: NESTING (Imbrication)

### Configuration Générale
**Type:** True Shape (forme réelle pour optimisation maximale)

**Paramètres d'Imbrication:**

| Paramètre | Valeur | Description |
|-----------|--------|-------------|
| **Espacement** | `5 mm` | Marge minimale entre images |
| **Rotation min.** | `0°` | Permettre rotation libre |
| **Rotation max.** | `360°` | Angles multiples autorisés |
| **Durée d'optim.** | `30 sec` | Temps pour calcul optimal |
| **Limite de temps** | `60 sec` | Timeout si trop long |

**Modèle de Nom d'Amalgame:**
```
{JobID}_{CustomerID}_{LayoutName}
Exemple: BAT001_ACME_Layout_01
```

### Seuils de Génération Automatique (V2 — Hotfolder)

**Approche:** Sans déclencheur strict (générer dès que possible)

**Alternative 1 — Couverture Minimale:**
```
Générer layout quand couverture média ≥ 70%
```

**Alternative 2 — Temps Après Import:**
```
Générer layout si pas d'import depuis 5 minutes
```

**Recommandation:** Combiner les deux pour optimiser

### Ganging (Regroupement — Optionnel)
**Utilité:** Si fichiers de clients différents ne doivent pas se mélanger

**Configuration:**
- **Grouper par:** `CustomerID`
- **Résultat:** Un layout par client

---

## 📤 Module 8: OUTPUT (Export)

### Paramètres d'Exportation Généraux

**Optimisations globales:**
- ✅ Inclure contenu image
- ✅ Générer contours de découpe
- ✅ Ajouter repères de coupe

### Fichiers d'Impression (PDF)

**Format:** PDF 1.7

**Dossier de sortie:** `/data/hotfolder_output/PRINT/` ou `C:\OUTPUT\PRINT\`

**Modèle de nommage:**
```
{JobID}_{CustomerID}_{Copies}_PRINT.pdf
Exemple: BAT001_ACME_3_PRINT.pdf
```

**Contenu du PDF:**
- ✅ Image impression complète
- ✅ Fond perdu (bleed) 5mm inclus
- ✅ Marques de coupe (si cutter sélectionné)
- ✅ Annotations (JobID, CustomerID)
- ✅ Contours de découpe

**Mode d'Export (V1 vs V2):**
- **V1 (Manuel):** Clic sur "Print" bouton manuelle
- **V2 (Auto):** Export automatique via hotfolder (option Pro/Max)

### Fichiers de Découpe

**Format:** Dépend du driver
```
- DXF (standard, compatible tous cutters)
- PDF 1.7 (si PDF cutter)
- ZCC (si Zünd)
- SGP (si Summa)
```

**Dossier de sortie:** `/data/hotfolder_output/CUT/` ou `C:\OUTPUT\CUT\`

**Modèle de nommage:**
```
{JobID}_{CustomerID}_{Copies}_CUT.{ext}
Exemples:
- BAT001_ACME_3_CUT.dxf
- BAT001_ACME_3_CUT.pdf
```

**Contenu du fichier de découpe:**
- Contours de découpe (`CutContourAuto` généré)
- Marques de coupe (repères)
- Formes réelles des éléments
- Pas d'image (seulement vecteurs)

**Recto-Verso:** Non applicable ici (pas de DSP)

### Export Manual (V1 — Demain)

**Actions disponibles depuis Studio:**

| Action | Résultat |
|--------|----------|
| **Print** | Export PDF → dossier par défaut |
| **Print to...** | Choisir dossier → export PDF |
| **Cut** | Export découpe → dossier cutter |
| **Print & Cut** | Exporte les deux fichiers |

---

## 🔐 Résumé Configuration

### À Faire DEMAIN (V1 — Manuel)

```
✅ 1. Créer recette "PREFLIGHT_PAO_PRO" dans PrimeCenter
✅ 2. Module INPUT:
       - Modèle extraction: {JobID}_{CustomerID}_{Copies}_{JobName}
       - Profil Check: Vérifier résolution, couleurs, fonts
       - Profil Fix: Convertir RGB→CMYK, incorporer fonts

✅ 3. Module CUTTER OPTIONS:
       - Sélectionner cutter (ou none si impression seule)
       - Configuration marques de coupe

✅ 4. Module BLEEDING (IMPORTANT!):
       - Type: Canvas Extend
       - Top/Bottom/Left/Right: 5mm
       - Cible: Edges + Corners

✅ 5. Module NESTING:
       - Type: True Shape
       - Espacement: 5mm
       - Modèle nom: {JobID}_{CustomerID}_{LayoutName}

✅ 6. Module OUTPUT:
       - Dossier impression: /data/output/PRINT/
       - Dossier découpe: /data/output/CUT/
       - Modèles nommage: {JobID}_{CustomerID}_{Copies}_PRINT/CUT

✅ 7. SAUVEGARDER LA RECETTE
```

---

## 🚀 Pour V2 (Automatisation Hotfolder)

```
✅ 1. Configurer hotfolder d'entrée: /data/input/
✅ 2. Mode semi-automatique:
       - Import auto
       - Preflight auto
       - Export manuel
✅ 3. Monitoring + logs pour 500 BAT/jour
```

---

## 📞 Troubleshooting

### Problème: Bleed ne s'applique pas
**Solution:**
- Vérifier que Canvas Extend est sélectionné (pas Shape Extend)
- Vérifier que les valeurs 5mm sont appliquées à tous les côtés
- Appliquer manuellement via clic-droit > Apply Bleed

### Problème: Contours de découpe non détectés
**Solution:**
- Vérifier nom des contours dans fichier d'entrée
- Ajouter contours au dictionnaire si manquants
- Utiliser profil preflight pour générer automatiquement

### Problème: Métadonnées non extraites
**Solution:**
- Vérifier convention nommage: `{JobID}_{CustomerID}_{Copies}_{JobName}`
- Pas d'espaces, utiliser `_` comme séparateur
- Tester avec exemple: `BAT001_ACME_3_Poster.pdf`

---

**Session:** https://claude.ai/code/session_017yhksCaj1YoCEk79BwGw1G
