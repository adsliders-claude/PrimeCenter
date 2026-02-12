# Convention de Nommage des Fichiers BAT

**Système:** Extraction automatique des métadonnées depuis les noms de fichiers
**Approche:** PrimeCenter PRO + extraction filename (pas de XML)
**Format:** Cohérent et prévisible pour l'automatisation

---

## 🎯 Format Standard de Nommage

```
{JobID}_{CustomerID}_{Copies}_{JobName}.{ext}
```

### Exemple Concret:
```
BAT001_ACME_3_Poster_A1.pdf
BAT002_TECHCO_1_Banner_2mx1m.pdf
BAT003_DESIGN_2_Brochure.psd
```

---

## 📋 Composants du Nom de Fichier

| Composant | Type | Exemple | Description |
|-----------|------|---------|-------------|
| **JobID** | Texte + Nombre | `BAT001`, `JOB123` | Identifiant unique du travail |
| **CustomerID** | Texte court | `ACME`, `TECHCO` | Code client (max 20 chars) |
| **Copies** | Nombre | `1`, `3`, `10` | Nombre de copies à imprimer |
| **JobName** | Texte descriptif | `Poster_A1`, `Banner` | Description du travail (lisible) |
| **Extension** | Format fichier | `.pdf`, `.psd`, `.jpg` | Format d'entrée |

---

## 🔧 Modèle d'Extraction PrimeCenter

Pour configurer dans **PrimeCenter V4 > Recette > Onglet Fichiers > Paramètres d'import**:

```
{JobID}_{CustomerID}_{Copies}_{JobName}
```

### Mapping des Métadonnées:
- `{JobID}` → Custom property (pour annotations/export)
- `{CustomerID}` → Métadonnée "Customer ID"
- `{Copies}` → Métadonnée "Copies"
- `{JobName}` → Métadonnée "Job name"

---

## 📝 Exemples de Fichiers Valides

### PDF
- `BAT001_ACME_3_Poster_A1.pdf`
- `BAT002_TECHCO_1_Banner.pdf`
- `BAT003_DESIGN_2_Brochure.pdf`

### PSD (Photoshop)
- `BAT004_PRINT_5_Flyer.psd`
- `BAT005_SIGN_1_VinylBanner.psd`

### JPG / PNG (Raster)
- `BAT006_ARTWORK_10_Stickers.jpg`
- `BAT007_PHOTO_2_Poster.png`

---

## ⚠️ Règles Importantes

### ✅ À Faire
- Utiliser **underscores** `_` comme séparateurs (pas de tirets, espaces, ou caractères spéciaux)
- **Pas d'espaces** dans le nom
- **JobID unique** pour chaque travail (idéalement séquentiel: BAT001, BAT002, etc.)
- **Copies en nombre entier** (1, 2, 3, ... pas "one", "deux")
- **Extension en minuscule** (.pdf, .psd, .jpg, .png)

### ❌ À Éviter
- Espaces: `BAT 001 ACME 3 Poster.pdf` ❌
- Tirets: `BAT-001-ACME-3-Poster.pdf` ❌ (fonctionne mais pas standard)
- Caractères spéciaux: `BAT#001@ACME$3.pdf` ❌
- Majuscules mélangées non standards: `bAt001_aCmE_3_PoSTeR.pdf` (OK techniquement mais confus)
- Extension majuscule: `.PDF` (préférer `.pdf`)

---

## 🔄 Flux d'Automatisation (V2)

1. **Utilisateur place fichier** → `BAT001_ACME_3_Poster.pdf` dans hotfolder INPUT
2. **PrimeCenter détecte** le fichier automatiquement
3. **Extraction métadonnées:**
   - JobID = `BAT001`
   - CustomerID = `ACME`
   - Copies = `3`
   - JobName = `Poster`
4. **Recette appliquée** → Preflight + Bleed + Contours
5. **Fichiers générés:**
   - `BAT001_ACME_3_Poster_PRINT.pdf` (impression)
   - `BAT001_ACME_3_Poster_CUT.pdf` ou `.dxf` (découpe)

---

## 💡 Variations Possibles

Si votre système utilise des conventions différentes, le modèle d'extraction peut être adapté:

### Variation 1: Sans JobID
```
{CustomerID}_{Copies}_{JobName}
Exemple: ACME_3_Poster.pdf
```

### Variation 2: Avec Date
```
{Date}_{JobID}_{CustomerID}_{Copies}_{JobName}
Exemple: 20250212_BAT001_ACME_3_Poster.pdf
```

### Variation 3: Avec Code Produit
```
{JobID}_{ProductCode}_{CustomerID}_{Copies}
Exemple: BAT001_PRINT001_ACME_3.pdf
```

> **À confirmer avec votre système :** Quelle convention utilise-t-on réellement?

---

## 🎯 Cas d'Usage Courants

### Cas 1: Autocollants (10 copies)
```
BAT045_STICKER_CO_10_LogoSquare.pdf
```
- JobID: `BAT045`
- Client: `STICKER_CO`
- Copies: `10`
- Description: `LogoSquare`

### Cas 2: Banner grand format
```
BAT046_EVENT_1_Banner_2x1m.psd
```
- JobID: `BAT046`
- Client: `EVENT`
- Copies: `1`
- Description: `Banner_2x1m`

### Cas 3: Brochures multicolores
```
BAT047_PRINT_50_Brochure_A5.pdf
```
- JobID: `BAT047`
- Client: `PRINT`
- Copies: `50`
- Description: `Brochure_A5`

---

## 📊 Tableau de Validation

Avant de placer un fichier dans le hotfolder, vérifier:

| Élément | ✅ Valide | ❌ Invalide |
|---------|----------|-----------|
| **Séparateur** | `_` (underscore) | `-` (tiret) ou ` ` (espace) |
| **Nombres** | `1`, `10`, `100` | `one`, `ten`, `un` |
| **JobID** | `BAT001`, `JOB123` | `BAT_001`, `job.123` |
| **CustomerID** | `ACME`, `TECHCO` | `ACME Inc`, `TECH-CO` |
| **Extension** | `.pdf`, `.psd`, `.jpg` | `.PDF`, `.Pdf` |
| **Espaces** | Aucun | Partout `BAT 001 ACME` |

---

## 🚀 Prochaines Étapes

1. **Confirmer la convention** avec votre équipe
2. **Tester l'extraction** dans PrimeCenter V4 (demain)
3. **Documenter vos variations** si nécessaire
4. **Intégrer au système** de génération des noms de fichiers

---

**Session:** https://claude.ai/code/session_017yhksCaj1YoCEk79BwGw1G
