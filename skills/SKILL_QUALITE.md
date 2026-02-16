# 🟡 SKILL QUALITÉ — Standardisation & Excellence

**Objet** : Tout ce qui assure qualité, conformité, traçabilité.
**Utilisé pour** : Préflight systématique, gestion couleur, job ticket, contrôle qualité.

---

## 📚 SECTIONS

### 1️⃣ PRÉFLIGHT SYSTÉMATIQUE (Checklist Défaillance Zéro)

**Règle d'Or** : 50% des erreurs production = erreur PDF non détectée avant.

#### Checklist Préflight Standard (OBLIGATOIRE)
```
✓ Dimensions document = dimensions production attendues (+ fonds perdus 5mm)
✓ Résolution images ≥ 240 ppi (idéal 300 ppi)
✓ Pas d'images CMYK+spot combinées (privilégier CMYK pur)
✓ Noirs : évaluer overprint (text=K100 pur, riche=C30M30Y30K100)
✓ Transparences : niveau acceptable, pas de blend modes complexes
✓ Traits fins : MINIMUM 0.5pt (< = risque disparition)
✓ Surimpressions : déterminées et documentées
✓ Polices : COURBER OBLIGATOIREMENT (pas d'outlines = catastrophe)
✓ Crop marks / bleed : vérifier cohérence avec fonds perdus
✓ Métadonnées : titre, author, date dernière modif présentes
✓ Format PDF : PDF/X-4 prioritaire (préservation couleur)
✓ Profil ICC : inclus OU spécifié pour production
```

#### Checklist Étendue (Par cas)
**Si couleur critique** :
- Profil ICC applicatif spécifié ✓
- Gamut couleur évalué (recadrage si dépasse) ✓
- ΔE tolérance documentée ✓

**Si géométrie complexe** :
- Détourage paths fermées ✓
- Pas de points isolés ✓
- Rayon minimum courbes = machine capable ✓

**Si découpe** :
- Cut contour présent (DXF) ✓
- Marges découpe respectées (0.5-2mm selon machine) ✓
- Pas de cut trop fin (risque arrachement) ✓

**Si lamination** :
- Fichier contient zones lamination identifiées ✓
- Pas de surcharge pliure ✓

#### Template Rapport Préflight (Contractuel)

```
═══════════════════════════════════════════════════════════════
RAPPORT PRÉFLIGHT — [Projet P-XXXX]
═══════════════════════════════════════════════════════════════

📋 FICHIER ANALYSÉ
Nom : [filename.pdf]
Taille : [XX MB] | Createur : [Logiciel] | Version PDF : [1.4/1.7]
Date analyse : [JJ/MM/YYYY] | Analyseur : [Nom]

✅ CONFORMITÉS VALIDÉES
- Dimensions : [X mm × Y mm] + [5mm bleed] ✓
- Résolution : [300 ppi] ✓
- Format : [PDF/X-4] ✓
- Profil ICC : [Spec valide] ✓
- Polices : [Courbes appliquées] ✓
- Noirs : [K100 pur identifié] ✓

⚠️ REMARQUES / À CORRIGER (Par priorité)
1. [Remarque 1]
   → Impact : [Faible/Modéré/Critique]
   → Action requise : [Description]
   → Deadline : [ASAP/Avant production]

2. [Remarque 2]
   → Impact : [Faible/Modéré/Critique]
   → Action requise : [Description]

✅ VALIDÉ POUR PRODUCTION
Signé par : [Prépresse - Nom] | Date : [JJ/MM/YYYY]
Prêt pour : [Techno impression - DATE LANCEMENT]

═══════════════════════════════════════════════════════════════
```

---

### 2️⃣ GESTION COULEUR (ISO 12647 / GWG Standards)

**Principe** : "Attendu client" ≠ "joli écran" → formaliser + contractualiser.

#### 3 Niveaux de Gestion Couleur

**Niveau 1 : BASIQUE**
- CMYK cohérent, pas vérification externe
- ✓ Acceptable pour : budget minimal, couleur non-critique
- ❌ Risque : variations ±5 ΔE possibles

**Niveau 2 : STANDARD**
- Profil ICC spécifié + épreuve numérique (PDF/X-4)
- ✓ Acceptable pour : majorité projets
- ✓ Tolérance : ΔE < 3-5 OK (client accepte naturelle variation)

**Niveau 3 : PREMIUM (Contractuel)**
- Épreuve couleur physique tirée + mesure spectro
- ✓ Acceptable pour : couleur critique (logo, brand)
- ✓ Tolérance : ΔE < 2 garantie (client signe épreuve)

#### Tolérance Couleur ΔE (Delta E = Écart Perceptuel)
```
ΔE < 1   : Imperceptible (impossible sans équipement)
ΔE < 2   : Excellent (couleur critique, qualité premium)
ΔE < 3   : Bon (standard, acceptable)
ΔE < 5   : Acceptable si prévu client (economy)
ΔE > 5   : REJETÉ (visible, inacceptable)
```

#### Intention de Rendu (Rendering Intent)
**Perceptual** :
- Compression chromatique si gamut dépasse
- → "Couleur naturelle"
- Quand : photos, gradient

**Colorimétrique Relatif** :
- Préserve point blanc
- → Fidélité couleur repère
- Quand : couleur exacte, logo

**Colorimétrique Absolu** :
- Inclut blanc du papier
- → Usage lab printing
- Quand : très spécialisé

#### Profil ICC (Choix & Utilisation)
```
1. OBTENIR profil machine cible
   → Demander fournisseur production
   → OU utiliser GWG standard (Europe = ISO Coated v2)

2. INCLURE dans BAT
   → "Épreuve générée avec profil [NOM PROFIL]"
   → "Couleur visuelle peut varier selon éclairage"

3. COMMUNIQUER
   → Document couleur = informatif (non-contractuel) SAUF accord
   → Épreuve physique = seule référence contractuelle possible
```

#### Quand Inclure Épreuve (Critères)

**OUI (Inclure épreuve) si** :
- ✓ Client demande match exact Pantone
- ✓ Logo marque = couleur critique
- ✓ Photos = fidélité couleur clés
- ✓ Support couleur base important (noir riche vs K pur)

**NON (BAT standard OK) si** :
- ✓ Couleur secondaire, pas critique
- ✓ Budget serré (épreuve = +100€, +3j)
- ✓ Client accepte tolérance (écrit clairement BAT)

---

### 3️⃣ JOB TICKET (Document Unique Projet)

**Objet** : Traçabilité 100% du projet, de brief à archivage.

#### Template Job Ticket Complet

```
╔══════════════════════════════════════════════════════════════════╗
║              JOB TICKET PROJET — TRAÇABILITÉ COMPLÈTE           ║
╚══════════════════════════════════════════════════════════════════╝

📋 IDENTIFICATION
  Identifiant Projet    : [P-XXXX-YYYY] (format : P-CLIENT-YEAR-SEQ)
  Nom Projet Court      : [Nom court intelligible]
  Date Création         : [JJ/MM/YYYY]
  Date Deadline         : [JJ/MM/YYYY]
  Statut Current        : [Discovery/Engineering/Preflight/Production/Delivery/Archive]

👤 CLIENT
  Nom Société           : [Société]
  Contact Principal     : [Nom]
  Email                 : [Email]
  Téléphone             : [Tel]
  PO / Ref Client       : [Numéro si applicable]

🎯 USAGE & BRIEF
  Destination Finale    : [Intérieur/Extérieur/Vitrine/Véhicule/Chantier/Autre]
  Durée Requise         : [Jours/Mois/Ans - Format clair]
  Temporaire / Perm     : [Temporaire/Définitif]
  Usage Spécifique      : [Description courte usage réel]

📦 SUPPORT & FABRICATION
  Support Matière       : [Marque/Référence - Ex: Vinyl Coulé Polymère Ref.XYZ]
  Dimensions            : [XXX × YYY mm] + [5mm bleed]
  Quantité              : [Nombre unités]
  Finition              : [Brillant/Mat/Satin/Anti-graffiti/Autre]
  Techno Impression     : [UV plat/UV Roll/Éco-solvent/Résine/Sublimation]
  Découpe Requise       : [Oui/Non - Si oui: type]
  Lamination Type       : [Brillant/Mat/Satin/Anti-graffiti/Aucune]
  Assemblage Special    : [Pliage/Rainage/Contrecollage/Œillets/Aucun]

🔧 SPÉCIFICATIONS FICHIERS
  Format Accepté        : [PDF/X-4 obligatoire]
  Résolution Requise    : [300 ppi minimum]
  Profil ICC Cible      : [Spec ou standard]
  Noirs Spécifiés       : [K100 pur / Riche C30M30Y30K100]
  Surimpressions        : [Documentées - ex: Black K100 overprint=OUI]
  Couleur Critique      : [OUI/NON - Si OUI: ΔE < ? Tolérance]
  Épreuve Requise       : [NON/Standard/Contractuelle]

📄 FICHIERS LIÉS
  PDF Final Validé      : [Filename_FINAL.pdf] | Validé [JJ/MM] par [Nom]
  BAT Signé Client      : [Filename_BAT_SIGNED.pdf] | [JJ/MM]
  DXF Découpe (si)      : [Filename_CUT.dxf] | [JJ/MM]
  Archive Haute Rés     : [Filename_ARCHIVE.tif] | [JJ/MM]
  Sources (PSD/AI)      : [Stocké à] | Archivé [OUI/NON]

✅ VALIDATIONS (Sign-off Chain)
  Créatif Validé        : ☐ [Nom] | [JJ/MM]
  Prépresse Validé      : ☐ [Nom] | [JJ/MM]
  Production Validé     : ☐ [Nom] | [JJ/MM]
  Client Approuve BAT   : ☐ [Signature] | [JJ/MM]

🚨 RISQUES IDENTIFIÉS
  Risque 1              : [Description]
  Mitigation            : [Action préventive]
  Propriétaire          : [Nom responsable]

  Risque 2              : [Description]
  Mitigation            : [Action]
  Propriétaire          : [Nom]

📊 TIMING
  Phase 1 : Discovery   : [JJ/MM → JJ/MM] Durée : [X jours]
  Phase 2 : Engineering : [JJ/MM → JJ/MM] Durée : [X jours]
  Phase 3 : Preflight   : [JJ/MM → JJ/MM] Durée : [X jours]
  Phase 4 : Production  : [JJ/MM → JJ/MM] Durée : [X jours]
  Phase 5 : Delivery    : [JJ/MM → JJ/MM] Durée : [X jours]

  TOTAL Délai Réaliste  : [XX jours] (+ XX buffer)
  Date Livraison        : [JJ/MM/YYYY DÉFINITIF]

📍 QUALITÉ & CONTRÔLE
  Contrôle 1er Tirage   : [OUI/NON] | Validé [Nom] | [JJ/MM]
  Tolérance Couleur     : [ΔE < 3] ✓ Mesuré spectro [OUI/NON]
  Contrôle Découpe      : [OUI/NON] | Validé [Nom] | [JJ/MM]
  Photos Qualité Finale : [OUI/NON] | [Nombre photos]
  Conformité Finale     : [ACCEPTÉ/REJETÉ/CONDITIONNEL] | [JJ/MM]

🚚 LOGISTIQUE
  Emballage Type        : [Bobine/Palette/Carton/Spécial]
  Adresse Livraison     : [Adresse complète]
  Conditions Livrais    : [Horaires/Accès spéciaux/Assurance]
  Transport Assuré      : [OUI/NON]

📦 ARCHIVAGE
  Stockage Fichiers     : [Localisation serveur/cloud]
  Rétention Minimale    : [3-5 ans]
  Réassorts Prévus      : [OUI/NON - Si OUI : frequency]

💡 NOTES LESSON LEARNED
  [Qu'avons-nous appris ? À améliorer ? Blocages rencontrés ?]

╚══════════════════════════════════════════════════════════════════╝
```

#### Points de Validation Clés (Sign-off Chain)

```
1. CRÉATIF ✓
   - Texte OK ? Orthographe ?
   - Mise en page OK ? Alignements ?
   - Couleur écran = intention ?

2. PRÉPRESSE ✓
   - PDF conforme spec ? (résolution, dimensions, polices courbes)
   - Préflight OK ? (pas d'erreurs détectées)
   - Profil ICC appliqué ? Noirs OK ?

3. PRODUCTION ✓
   - Machine calibrée ? (profil ICC charge)
   - Test premier tirage validé
   - Finition conforme ? (découpe, lamination)
   - Photos qualité prise

4. CLIENT ✓
   - BAT approuvé et signé
   - Accepte conditions couleur (contractuel ou informatif ?)
   - Approuve timeline

→ **Chaque signature = responsabilité claire = réclamation impossible post-signature**
```

---

### 4️⃣ SPÉCIFICATIONS FICHIERS (Gabarit Projet)

#### Template Specs PDF/X à envoyer au client

```
═══════════════════════════════════════════════════════════════════
SPÉCIFICATIONS FICHIERS — [Nom Projet]
═══════════════════════════════════════════════════════════════════

📐 DIMENSIONS
  Dimensions finales    : [XXX × YYY mm]
  Fonds perdus (bleed)  : [5 mm minimum TOUS les côtés]
  Dimension fichier     : [XXX + 10 × YYY + 10 mm]
  Exemple              : Si final 1000×500, fichier = 1010×510 mm

📊 RÉSOLUTION
  Résolution minimale   : 240 ppi (idéal 300 ppi)
  Distance lecture      : [Proximité/Moyen/Loin] → détermine exigence
  Images héritées       : Si résolution < 240 ppi, indiquer qui assume
  Formule              : Résolution utile = source ppi × (facteur zoom %)

🎨 COULEUR & PROFIL
  Espace couleur        : CMYK pur obligatoire (pas RGB)
  Profil ICC Embédé     : [Spécifier ou préciser application]
  Rendu intention       : Colorimétrique Relatif (standard)
  Noirs spécifiés       : [K100 pur OU Riche C30M30Y30K100]
  Couleur critique ΔE   : [< 3 standard / < 2 premium]

✏️ TYPOGRAPHIE
  Polices              : COURBER OBLIGATOIREMENT
  Textes fins          : Épaisseur min 0.5pt
  Effet texte          : Pas d'ombres flous / halos (rasterize)

🎭 ÉLÉMENTS SPÉCIAUX
  Transparences        : Localiser exactement (à rasterize avant export)
  Surimpressions       : Lister éléments overprint (ex: Black K100 always overprint)
  Trait fins           : Minimum 0.5pt épaisseur
  Fonds perdus         : Vérifier débord 5mm pour chaque élément

📄 FORMAT EXPORT
  Format obligatoire   : PDF/X-4 (prioritaire) sinon PDF/X-3
  Compression          : Aucune perte image
  Version PDF          : 1.4 ou ultérieur

✅ CHECKLIST PRÉ-EXPORT
  ☐ Dimensions = [XXX + bleed] vérifiées
  ☐ Résolution ≥ 240 ppi confirmée
  ☐ Polices courbes (pas outline)
  ☐ Pas de transparences (rasterize)
  ☐ CMYK pur appliqué
  ☐ Noirs spécifiés (K100 OU riche)
  ☐ Fonds perdus 5mm sur tous côtés

═══════════════════════════════════════════════════════════════════
```

---

### 5️⃣ CONTRÔLE QUALITÉ (Défaillance Zéro)

#### Checklist Production QC

```
☑ Fichier correct confirmé avant lancement machine
☑ Machine calibrée & profil ICC chargé
☑ Test premier tirage OK (couleur, traits, résolution visuels)
☑ Tous les tirages contrôlés (par échantillonnage ou 100%)
☑ Finition exécutée conforme (découpe, rainage, lamination)
☑ Emballage protecteur appliqué
☑ Étiquetage projet + numéro lot + date production
☑ Traçabilité : photo qualité finale prise avant expédition
☑ PV qualité signé par responsable production

Tolérance Couleur Mesurée
  ΔE < 2   : ✓ EXCELLENT - Approbation immédiate
  ΔE < 3   : ✓ BON - Approbation standard
  ΔE < 5   : ⚠️ ACCEPTABLE si client accepte economy
  ΔE > 5   : ❌ REJETÉ - Relancer tirage
```

---

### 6️⃣ BEST PRACTICES QUALITÉ

#### Principe 1 : Préflight SYSTÉMATIQUE
→ Jamais sauter étape (même client "urgent")
→ Template systématisé = 5 min par projet

#### Principe 2 : BAT CONTRACTUEL
→ Document BAT = accord écrit couleur policy
→ Clause claire : "À titre informatif" OU "Épreuve physique garantie"
→ Signature client = accepte conditions

#### Principe 3 : Job Ticket COMPLET
→ Un seul document source de vérité
→ Traçabilité A → Z du brief à archivage
→ Lesson learned documentée = amélioration continue

#### Principe 4 : Mesure Spectrophotométrie (Si couleur critique)
→ Étalonnage blanc + noir de référence
→ ΔE mesuré (pas estimation visuelle)
→ Certificat remis client si contractuel

#### Principe 5 : Photo QC Systématique
→ Avant expédition (preuve conformité)
→ Identifiable (numéro projet visible)
→ Archivée 5 ans minimum

---

## ⚡ UTILISATION RAPIDE

### Avant production :
1. Checklist préflight complète ✓
2. Rapport préflight signé ✓
3. Job ticket 90% complété ✓
4. Spécifications fichiers confirmées ✓
5. BAT client signé ✓

### Pendant production :
1. Machine calibrée ✓
2. Test 1er tirage OK ✓
3. Tous les échantillons contrôlés ✓
4. Photos QC prises ✓
5. PV qualité signé ✓

### Après production :
1. Archivage fichiers 5 ans ✓
2. Lesson learned documenté ✓
3. Job ticket complété 100% ✓
4. Photos stockées ✓
5. Client satisfait → Récit positif ✓

---

## 📖 RESSOURCES LIÉES

- Voir `SKILL_METIER.md` pour préflight mental & diagnostic
- Voir `SKILL_MANAGEMENT.md` pour coordin sourcing
- Voir `PRINT_MANAGEMENT_EXPERTISE.md` pour détails complets
- ISO 12647 référence couleur (www.iso.org)
- GWG standards (www.gwgonline.com)

---

**Skill Version** : 2.0 (Phase 2)
**Dernière MAJ** : 2026-02-16
**Status** : Opérationnel pour assurance qualité
