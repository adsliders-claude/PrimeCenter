# Expertise Print Management - Fondation "20 ans de métier"

**Objectif** : Encoder les meilleures pratiques du print management grand format et sous-traitance pour le système PrimeCenter.

---

## 🎯 DOMAINE 1 : Compétences "Cœur Métier" (Techniques Print)

### 1.1 Technologies d'Impression Grand Format

| Technologie | Caractéristiques | Avantages | Limites | À Proposer Pour |
|---|---|---|---|---|
| **UV Plat** | Durcissement instantané UV | Haute qualité, ppi élevé, fonds noirs riches, supports rigides | Odeur UV, consommation énergie, pas de rolls | Rigides premium, Dibond, PVC, qualité max |
| **UV Roll-to-Roll** | Bobine continue, découpe finale | Productivité, vinyl haute qualité | Moins de variété supports | Campagnes vinyl, films, bâches |
| **Éco-solvant** | Encres faible VOC, adhésion naturelle | Moins toxique, odeur réduite, adhésion vinyl directe | Qualité légèrement moins brillante | Vinyl, bâches, supports divers |
| **Résine/Latex** | Encres à base d'eau | Séchage rapide, low-VOC, meilleure odeur | Contrastes moins marqués | Écran, PVC, textile, contexte public |
| **Sublimation Textile** | Encres fugaces → chaleur → diffusion fibre | Rendu unique, fibres intégrées | Support = polyester, pas de blanc | Textiles, murs SEG, drapeaux |

### 1.2 Chaîne Graphique & Prépresse

**Règle d'Or** : Un PDF mauvais = une impression mauvaise, même sur bonne machine.

#### Diagnostic PDF (Préflight Mental)
- **Surimpressions** : Déterminer si "overprint black" ou pas → risque de contours visibles
- **Transparences** : Où sont-elles ? Lors de la rasterisation → perte de qualité potentielle
- **Fonds perdus** : Minima = 3mm, idéal = 5mm (surtout découpe)
- **Traits fins** : < 0.25pt risquent de disparaître ; ligne 0.5pt = minimum confortable
- **Noirs** : Black texte (100K) vs Black riche (C30 M30 Y30 K100) vs Noir pur (K100 seul)
- **Images** : Ppi utile = ppi source × (facteur zoom) ; 300 ppi = standard, 240 acceptable si recul, < 150 = visible en proximité
- **Polices** : Toujours courber ou utiliser system fonts ; attention aux polices fines/cheveux
- **Aplats** : Noirs + aplats clairs = contours nets ; dégradés = risque banding

### 1.3 Finition & Fabrication

#### Lamination
- **Brillant** : Contraste max, premium, reflets, sensible aux rayures → pour qualité/vitrine
- **Mat** : Douce, discrétion, pas de reflets → intérieur, designs modernes
- **Satin** : Hybride, bonne apparence, toucher doux
- **Anti-graffiti** : Protective top coat, résilience vandalisme, entretien facilité

#### Découpe & Usinage
- **Découpe mi-chair** : Vinyl sur support → enlever vinyl, garder support intact (affichage)
- **Détourage** : Vinyl pré-découpé à forme complexe (logos, formes organiques)
- **Rainage** : Plis guides pour pliage sans craquage (packaging, dépliants)
- **Contrecollage** : Coller 2+ matières (rigide + vinyl, par ex)
- **Œillets / Fourreaux** : Renforcement trous, pose bâche sur chassis
- **Couture silicone (SEG)** : Mur tendu, encastrement dans profilé alu → changement facile
- **Usinage plaque** : Gravure, découpe shapes sur PVC/Dibond/PMMA

#### Assemblage
- **Pliage** : Scoring (rainage) obligatoire pour épaisseurs > 0.3mm
- **Ourlage / Couture** : Bâches, textiles → renforcement bords, solidité
- **Œillets** : Espacement 20-30cm pour bâche, poids distribué

---

## 🎯 DOMAINE 2 : Compétences "Qualité / Standardisation"

### 2.1 Préflight Systématique

**Non négociable** : Un PDF non vérifié = 50% risque d'erreur en production.

#### Checklist Préflight Standard
```
✓ Dimensions document = dimensions production attendues (+ fonds perdus)
✓ Résolution images ≥ 240 ppi (idéal 300)
✓ Pas d'images CMYK+spot (privilégier CMYK pur)
✓ Noirs : évaluer overprint (text vs riche)
✓ Transparences : niveau acceptable, pas de blend modes complexes
✓ Traits fins : minimum 0.5pt
✓ Surimpressions : déterminées et documentées
✓ Polices : courber ou vérifier disponibilité
✓ Crop marks / bleed : vérifier cohérence
✓ Métadonnées : titre, author, date dernière modif
```

### 2.2 Gestion Couleur (ISO & GWG Standards)

**Principe** : "Attendu client" ≠ "joli" → formaliser + contractualiser.

#### 3 Niveaux de Gestion Couleur
1. **Basique** : CMYK cohérent, pas de vérification externe
2. **Standard** : Profil ICC + épreuve numérique (PDF/X + proof)
3. **Premium** : Épreuve couleur contractuelle + tolérance écrite (ΔE < 3, ex)

#### Intention de Rendu (Rendering Intent)
- **Perceptual** : Compression chromatique si gamut dépasse → "couleur naturelle"
- **Colorimétrique relatif** : Préserve point blanc → fidélité couleur repère
- **Colorimétrique absolu** : Inclut blanc de la papier → usage lab printing

#### Profils ICC
- Demander toujours profil machine client (ou utiliser profil standard GWG)
- Inclure dans BAT : "Preuve générée avec profil XYZ, couleur visuelle peut varier selon condition d'éclairage"

### 2.3 Dossier de Fabrication

#### Job Ticket (Document Unique Projet)
```
[Identifiant Projet : P-XXXX-YYYY]

CLIENT : [Nom] | Contact : [Email/Tel]
USAGE : [Destination, durée, contraintes]
SUPPORT : [Matière, dimensions, quantité]
MATIÈRE : [Marque/Référence vinyl/bâche/rigide]
ENCRE : [Système impression - UV/Éco-solv/Résine]
FINITION : [Lamination, vernis, rainage, découpe]
POSE : [Méthode, contraintes, responsable]
PACKAGING : [Bobine, palette, protection]

FICHIERS :
- Version finale validée : [Fichier PDF/X + date]
- BAT signé : [PDF signaturé client + date]
- Archives : [JPG haute résolution + RAW si nécessaire]

VALIDATION :
- Créa (couleur, texte) : [Nom] ✓ [Date]
- Prépresse (PDF, preflights) : [Nom] ✓ [Date]
- Prod (qualité, finition) : [Nom] ✓ [Date]
- Client (acceptation) : [Nom] ✓ [Date]

RISQUES IDENTIFIÉS :
- [Risque 1 + mitigation]
- [Risque 2 + mitigation]

ARCHIVAGE : [Localisation stockage]
```

---

## 🎯 DOMAINE 3 : Compétences "Chef d'Orchestre" (Print Manager)

### 3.1 Sourcing & Sous-Traitance

#### Logique de Sélection Partenaire
1. **Capacité technique** : Techno disponible ? support résiste ? SLA acceptable ?
2. **Qualité** : Track record, certifications (ISO 12647, GWG) ?
3. **Pricing & Volume** : Volume annuel → tarif, volume break, conditions
4. **Résilience** : Délais, aléas, seconde source possible ?
5. **Partenariat** : Contact durable, EDI, communication fluide

#### Points à Challenger en Sourcing
- Prix : "Pourquoi ce prix ? Meilleur marché possible ?"
- Délais : "Combien temps du PDF reçu à livraison ?"
- Qualité : "Tolérance couleur ΔE ? Épreuve incluse ? Retouches ?"
- Emballage : "Protection, traçabilité, écologique ?"
- Flexibilité : "Modifications de last minute ? Urgence ? Rush possible ?"

### 3.2 Gestion de Projet Print Management

#### Timeline Typique (du brief à la pose)

```
J0 : Discovery call → besoin, support, durée, budget
J0-1 : Audit + recommandations matière/techno
J1-3 : Sourcing + devis (3 options : standard/premium/économique)
J3-5 : BAT visuel + approbation client
J5-7 : Fichiers finalisés + preflights
J7-10 : Production (temps varie : vinyl 2-3j, rigide 1-2j, découpe +1-2j)
J10-12 : Contrôle qualité + packaging
J12-15 : Livraison/stockage
J15-30 : Pose + PV réception

RISQUES TYPIQUES & MITIGATION :
- Délai tight → prévoir buffer +3j, sous-traitance parallèle
- Couleur critique → épreuve incluse systématique
- Support complexe → visite terrain, échantillon test
- Multi-sites → centraliser tracking, check-list par site
```

### 3.3 Communication Client (Les 5 Questions Pro)

**Objectif** : Révéler l'usage réel & anticiper 80% des emmerdes.

---

## 🎯 DOMAINE 4 : Méthode en 7 Étapes (Process Core PrimeCenter)

### Étape 1️⃣ : DÉCOUVERTE USAGE
**Sortie** : Fiche usage + durée de vie attendue

**Questions clés** :
- Destination exacte ? (intérieur, extérieur, semi, vitrine, salon, chantier)
- Durée de vie ? (2j, 3m, 1an, 3an, 7an, permanent)
- Temporaire/réutilisable/permanent ?
- Qui pose ? (nous, client, sous-traitant spécialisé)

---

### Étape 2️⃣ : AUDIT SUPPORT & ENVIRONNEMENT
**Sortie** : Checklist support + contraintes physiques

**À évaluer** :
- Support : verre, peinture, métal, plastique, bois, mur brut ?
- Texture : lisse / texturée / poreuse ?
- État : propre, poussière, humidité, saleté ?
- Pose : température ambiante, humidité, UV plein sud, vent, pluie ?
- Abrasion : trafic, nettoyage, vandalisme prévisible ?
- Accessibilité : nacelle, échelle, sol... risques de sécurité ?

**Sortie** : Fiche "Diagnostique Support" + photo site si pertinent

---

### Étape 3️⃣ : RECOMMANDATION TECHNIQUE
**Sortie** : Proposition matière + techno + finition

**Logique** : Usage + Support + Durée → Matière + Encre + Finition

**Exemple 1 - Vitrine verre, temporaire 3 mois, esthétique premium**
- Usage : intérieur, vitrine, pas d'abrasion
- Support : verre lisse
- Durée : 3 mois (court)
- Recommandation : Vinyl adhésif polymère monomère, brillant, techno UV éco-solv → bonne apparence, budget maîtrisé, retrait facile

**Exemple 2 - Parking extérieur, pluie + UV, 3 ans, accès nacelle**
- Usage : extérieur longue durée, exposition intégrale
- Support : béton poreux
- Durée : 3 ans (long)
- Recommandation : Vinyl coulé polymère + lamination mat anti-UV, primaire surface, pose professionnelle nécessaire → stabilité, durabilité, conforme UV

---

### Étape 4️⃣ : SPÉCIFICATIONS FICHIERS (Préflight Formalisation)
**Sortie** : Gabarit + Specs PDF/X + Préflight Rules

**À définir** :
- Dimensions fichier = production + fonds perdus (5mm minimum)
- Format : PDF/X-4 prioritaire (meilleure préservation couleur)
- Résolution : 300 ppi minimum (240 acceptable si recul)
- Noirs : définir si K100 pur ou riche (C30M30Y30K100)
- Surimpressions : lister les éléments qui doivent overprint
- Couleurs : CMYK pur, pas de couleurs spot sauf accord
- Traits : minimum 0.5pt, croix repères incluses

---

### Étape 5️⃣ : ÉPREUVE / BAT
**Sortie** : PDF contractuel + visuel de validation

**Trois niveaux de BAT** :
1. **BAT Standard** : PDF visuel + specs écrites (couleur ≠ contractuelle)
2. **BAT Premium** : PDF + tirage test matière (vinyl échantillon)
3. **BAT Contractuel** : Épreuve couleur certifiée (pour critiques)

**À valider avec client** :
- ✓ Texte (orthographe, contenu)
- ✓ Couleur (comparaison charte)
- ✓ Mise en page (alignements, espacements)
- ✓ Découpe (si pertinent : forme, détourage)
- ✓ Photo avant/après (si modification support)

**Document BAT obligatoire** :
```
Validé par [Client - Nom, Signature] le [Date]
Couleur : Conforme charte / À titre informatif* / Épreuve physique en annexe
(*) La couleur écran peut varier selon éclairage et configuration moniteur
Responsabilités : Client assume risques couleur non contractuelle
```

---

### Étape 6️⃣ : PRODUCTION + CONTRÔLE QUALITÉ
**Sortie** : Produit conforme + PV qualité + photos

**Checklist Production** :
```
☑ Fichier correct confirmé avant lancement
☑ Machine calibrée (profile ICC utilisé)
☑ Test premier tirage OK
☑ Tous les tirage contrôlés (couleur, traits, résolution)
☑ Finition : découpe, rainage, lamination conformes
☑ Emballage : protection, étiquetage, palette stable
☑ Photo qualité finale (avant expédition)
☑ Traçabilité : numéro lot + date production
```

**Tolérance Couleur Standard** :
- ΔE < 2 : Excellent (couleur critique)
- ΔE < 3 : Bon (standard)
- ΔE < 5 : Acceptable si prévu

---

### Étape 7️⃣ : LIVRAISON / POSE / PV
**Sortie** : Procès-verbal + archivage + SAV plan

**À documenter** :
- Photo site avant/après pose
- PV réception (conformité, conditions)
- Conditions à respecter (durée avant passage véhicules, nettoyage délai, etc.)
- Points SAV (contact, durée garantie, conditions retouches)

**Archivage Projet** :
- Fichiers sources + PDFs finaux (3-5 ans minimum)
- Photos avant/après
- BATs signés
- Job ticket complet
- Retours client → amélioration continue

---

## 🎯 DOMAINE 5 : Questions Diagnostiques "Qui Font Pro"

### A. DESTINATION & USAGE

1. **Où exactement le support va se placer ?** (intérieur, extérieur, semi-extérieur, vitrine, salon, chantier, véhicule…)
   → Impact : matière (UV résistance), finition, adhésif, pose

2. **Durée de vie attendue ?** (2 jours, 3 mois, 1 an, 3 ans, 7 ans, permanent…)
   → Impact : qualité encre, lamination, polyvalence vinyl, investissement

3. **Temporaire (démontable) ou définitif ?**
   → Impact : adhésif (repositionnable vs permanent), finition, retrait

4. **Trafic / abrasion prévisible ?** (contact, graffiti, nettoyage fréquent…)
   → Impact : lamination anti-graffiti, résistance surface, finition

---

### B. SUPPORT & POSE

5. **Sur quoi exactement on colle/pose ?** (verre, peinture, métal, plastique, bois, mur brut, carrelage…)
   → Impact : adhésif spécifique, préparation surface, risque arrachement

6. **Surface lisse, texturée ou poreuse ?** (état, grain…)
   → Impact : adhésif (conformable ou non), primaire potentiel

7. **Qui pose ?** (équipe interne, client seul, poseur spécialisé…)
   → Impact : niveau d'exigence, complexité installation, responsabilité

8. **Contraintes logistique/pose ?** (température, humidité, accès, sécurité, délais fixe…)
   → Impact : délais production, méthode pose, pénalités

---

### C. ENVIRONNEMENT & CONTRAINTES PHYSIQUES

9. **Exposition UV/pluie/vent ?** (plein sud, semi-abrité, humidité haute…)
   → Impact : stabilité couleur (résistance UV), lamination, choix matière

10. **Risque vandalisme, graffiti ou nettoyage agressif ?**
    → Impact : lamination anti-graffiti, résistance chimique

11. **Température de pose/utilisation ?** (hivernale, équatoriale, intérieur chauffé…)
    → Impact : dilatation, adhésif, stabilité vinyle

12. **Réglementation applicable ?** (ERP public, M1 inflammabilité, accessibilité, sécurité…)
    → Impact : certifications matière, tests, documentation

---

### D. ATTENDU VISUEL & MARQUE

13. **Couleurs critiques ?** (Pantone, charte logo, match exact demandé…)
    → Impact : épreuve incluse, tolérance ΔE, coût + délai

14. **Distance de lecture principale ?** (lecture proche, moyenne, loin…)
    → Impact : ppi utile (300 proche, 240 moyen, 150 loin), choix techno

15. **Niveau de finition attendu ?** (budget / standard / premium…)
    → Impact : techno (UV vs éco-solv), lamination, support

---

### E. LOGISTIQUE & PLANNING

16. **Date fixe d'installation ? Pénalités ?**
    → Impact : buffer délai, urgence, coût rush

17. **Emballage / contraintes livraison ?** (multi-sites, monte-charge, horaires…)
    → Impact : format découpe, packaging spécial, logistique

18. **Réassorts prévus ?** (série unique ou base pour variations…)
    → Impact : archivage fichiers, modularité BAT, gestion stock

---

## 🎯 DOMAINE 6 : Logique de Choix des Matières

### Règles d'Or
1. **La matière = fonction (durée + usage + support)**
2. **Le support dicte l'adhésif** (surface = énergie de surface → nécessite adhésif adapté)
3. **Extérieur = UV + eau + dilatation** → matière stable + encre + lamination

### Grandes Familles de Matières

#### 1️⃣ VINYLES ADHÉSIFS

**Monomère (Standard)**
- Épaisseur : 100µm
- Adhésif : général, acrylique
- Durée : 2-3 ans en ombre, moins en plein UV
- **Quand proposer** : Campagnes courtes, supports plats standards, budget limité
- Exemples : Signalétique commerciale, promotions, vitrines temporaires
- Prix : Référence (base 100)

**Polymère (Meilleur compromis)**
- Épaisseur : 100-120µm
- Adhésif : polymère acrylic renforcée
- Durée : 3-5 ans en ombre, 2-3 ans en UV modéré
- **Quand proposer** : Durée moyenne, supports variés, encaissement qualité
- Exemples : Signalétique pérenne, véhicules, façades semi-exposées
- Prix : +20-30% vs monomère

**Coulé (Premium + Conformabilité)**
- Épaisseur : 120-150µm
- Adhésif : fort, repositionnable parfois dispo
- Durée : 5-7 ans ombre, 3-5 ans UV modéré, 2-3 ans plein sud
- **Quand proposer** : Surfaces complexes (reliefs, formes), durée longue, finition premium
- Exemples : Véhicules haut de gamme, wrapping architecture, surfaces pointues
- Prix : +50-80% vs monomère

---

#### 2️⃣ FILMS VITRINES

**Film Transparent Standard**
- Transparence : 88-92%
- Adhésif : acrylique doux
- **Quand proposer** : Vitrines, transparence, pas de chauffage
- Exemples : Vitrophanie, signalétique transparente
- Avantage : Discrétion, vision externe maintenue
- Risque : Condensation hivernale

**Film Dépoli / Translucide**
- Transparence : 30-50%
- **Quand proposer** : Intimité tout en légèreté, bureaux, zones d'attente
- Exemples : Cloisons vitrées, zones semi-privées
- Avantage : Intimité, diffusion lumière
- Risque : Nettoyage (dépôts visibles)

**Film Micro-Perforé (One-Way Vision)**
- Voir dehors : OUI / Voir dedans : NON
- Transparence : 50% (from inside), opaque (from outside)
- **Quand proposer** : Vitrines avec affichage interne, buses, véhicules, confidentialité
- Exemples : Fenêtres de bus, stores digitaux, boutiques confidentielles
- Avantage : Affichage HD possible + discrétion
- Risque : Qualité image dépend angle vue

**Film Solaire / Anti-Chaleur**
- Teinte : gris neutre
- Fonction : Bloque UV (80-90%), réduit chaleur
- **Quand proposer** : Locaux très vitrés, surchauffe, confort thermique
- Exemples : Façades sud, vérandas, locaux informatique
- Avantage : Économies énergie, confort
- Risque : Teinte visible même sans décor

---

#### 3️⃣ BÂCHES (Frontlit & Mesh)

**Bâche Frontlit (Standard)**
- Épaisseur : 280-440 µm
- Face : Brillante ou mate
- Dos : Blanc lisse
- **Quand proposer** : Facades temporaires, chantiers, panneaux standards
- Exemples : Hoarding chantier, façades rénovation, signalétique mobile
- Adhésif : Adhésif PVC, costaud
- Avantage : Coût base, poids raisonnable
- Risque : Vent → bâche vibre, bruite

**Bâche Mesh (Aérée)**
- Perforations : 50% surface aérée
- Épaisseur : 390-500 µm
- **Quand proposer** : Façades ventées, échafaudage, lieux à circulation d'air
- Exemples : Hoarding hauteur (vent), barriages temporaires
- Avantage : Réduit traînée vent (moins bruyant), allège charge
- Risque : Moins de densité couleur

**Bâche Blockout (Opacité Double)**
- Épaisseur : 440 µm + coating
- Opacité : 100% (même contrejour)
- **Quand proposer** : Façade opacifiante urgente, cacher travaux, intimité
- Exemples : Fermeture boutiques urgentes, hoarding chalets
- Avantage : Opacité garantie, poids
- Risque : Coût supérieur

**Bâche Textile Enduite (Premium)**
- Base : Polyester tissé
- Enduit : Polyuréthane / PVC
- Flexibilité : Excellente
- **Quand proposer** : Décors intérieurs (esthétique fabric), drapeaux, durée longue
- Exemples : Murs tendus, backlit textile, décors stores
- Avantage : Rendu naturel, poids léger, qualité optique
- Risque : Coût (2-3x bâche standard), délai

---

#### 4️⃣ SUPPORTS RIGIDES

**PVC Expansé (Lightweight)**
- Épaisseur : 1, 2, 3, 5 mm
- Densité : ~200 kg/m³
- Usinage : Facile, découpe et gravure
- **Quand proposer** : Signalétique intérieure, économies poids, géométries complexes
- Exemples : Noms magasins, directionnels, POV
- Avantage : Léger, prix bas, pliable léger
- Risque : Peu de tenue rigide très épais, UV fade en ext longue durée

**Alvéolaire (Coroplast)**
- Épaisseur : 2-10 mm (alvéoles)
- Densité : ~180 kg/m³
- Rigidité : Très bonne rapport poids/rigidité
- **Quand proposer** : Panneaux volumineux, enseignes, posters géants
- Exemples : Panneaux chantier (4-5mm), affichage agence (2-3mm)
- Avantage : Légéreté, rigidité, économie
- Risque : Petits alvéoles peuvent piéger poussière (peinture granitée)

**Dibond / ACP (Premium Rigide)**
- Composition : Alu + polyéthylène + alu (sandwich)
- Épaisseur : 3-6 mm
- Finition : Lisse, brillante possible, bord alu usinable
- **Quand proposer** : Signalétique premium, enseigne pérenne, finition high-end
- Exemples : Enseignes établissements (banques, hôtels), panneaux architecte
- Avantage : Rigidité, finition premium, usinage précis
- Risque : Coût (5-8x PVC), poids, découpe demande lame spéciale

**PMMA / Acrylique (Transparent / Esthétique)**
- Transparence : 92%
- Rigidité : Excellente, rigide froid
- Finition : Brillante naturelle, gravure possible
- **Quand proposer** : Écriteaux transparents premium, plaques gravées, vitrines
- Exemples : Plaques noms or/chrome, vitres déco, protection haut de gamme
- Avantage : Transparence + rigidité + gravure, aspect premium
- Risque : Fragile à choc, coût

**Carton Alvéolaire (Très Court Terme)**
- Épaisseur : 3-5 mm
- Recyclable : 100%
- **Quand proposer** : Exposition, événementiel, 1-3 mois max
- Exemples : PLV, pop-up boutique, décor éphémère
- Avantage : Coût minimal, écolo, personnalisable
- Risque : Humidité → déforme, courte durée

---

#### 5️⃣ TEXTILES POUR DÉCOR INTÉRIEUR

**Murs Tendus (Toile Polyester Enduite)**
- Base : Polyester 140-200 g/m²
- Enduit : PU ou PVC
- Installation : Encastrement profilé alu (SEG ou system similaire)
- **Quand proposer** : Murs décor, bureaux, boutiques, changement facile
- Exemples : Branding intérieur, cloisons visuelles, acoustique (combiné)
- Avantage : Rendu doux, changement facile, qualité optique, léger
- Risque : Coût d'installation (profilés), durée profilé > tissu (5 ans tissu, 10 ans profilé)

**Drapeaux & Textiles**
- Matière : Polyester 150-200 g/m², parfois coton
- Finition : Liseré chaîne, ganse, boucles fixation
- **Quand proposer** : Événementiel, signalétique mobile, personnalisé
- Exemples : Drapeaux marque, textiles événementiel, fanions
- Avantage : Léger, réutilisable, qualité print textile unique
- Risque : Retrait UV faible (polyester coulé pérfère)

**Backlit Textile**
- Matière : Polyester 240-280 g/m² (semi-translucide)
- Illumination : LED intégrée structure
- **Quand proposer** : Enseignes lumineuses intérieures premium, décor nuit
- Exemples : Enseigne salon haut gamme, décor mur éclairé
- Avantage : Qualité lumière, esthétique premium, blanc non surexposé
- Risque : Coût système lumineux + textile, complexité install

---

### Matrice de Recommandation Rapide

| **Situation** | **Durée** | **Support** | **Matière Recommandée** | **Finition** | **Techno Impression** |
|---|---|---|---|---|---|
| Vitrine verre, temporaire | 3 mois | Verre lisse | Film adhésif ou vinyl monomère | Brillant | UV/Éco-solv |
| Devanture magasin pérenne | 3-5 ans | Peinture | Vinyl polymère coulé | Mat ou brillant | Éco-solv |
| Parking extérieur | 3-7 ans | Béton | Vinyl polymère + lamination | Mat anti-UV | Éco-solv |
| Façade chantier | 2-6 mois | Air (accrochage) | Bâche mesh + ragreage | - | Grand format |
| Décor intérieur bureau | 2-3 ans | Mur peint | Mur tendu textile (SEG) | Satin/mat | Sublimation textile |
| Enseigne premium (Dibond) | 5-10 ans | Structure alu | Dibond 3-6mm + vinyl | Mat | UV plat ou éco-solv |
| Pop-up événement | 3-7 jours | Carton | Carton alvéolaire | - | Éco-solv |

---

## 🎯 DOMAINE 7 : Best Practices (Sécuriser Marges & Qualité)

### 1. Préflight Systématique

**Template de Rapport Préflight**
```
[Projet : P-XXXX]
[Date préflight : JJ/MM/YYYY]

FICHIER ANALYSÉ : [Nom fichier] - [Taille] - [PDF version]

✓ CONFORMITÉS
- Dimensions : [X mm × Y mm] ✓
- Résolution : [300 ppi] ✓
- Profil ICC : [Préflight ICC] ✓
- Format : [PDF/X-4] ✓

⚠ REMARQUES / À CORRIGER
1. Transparences détectées : [Liste + localisation]
   → Action : Rasterize transparences avant production
2. Traits fins (< 0.5pt) : [Nombre détecté]
   → Action : Augmenter épaisseur à 0.5pt minimum
3. Image résolution < 300 ppi : [% zones]
   → Appréciation : Acceptable si vue recul [Validation]

✅ VALIDÉ PRODUCTION
- Signé par : [Prépresse] le [Date]
- Prêt pour : [Techno impression, date lancement]
```

### 2. BAT Efficace (Contractuel & Clair)

**Template BAT Standard**
```
═══ PROJET P-XXXX - BAT VISUEL ═══

CLIENT : [Nom] | DATE : [JJ/MM/YYYY]
SUPPORT : [Vinyl polymère Gloss / Dibond 3mm / etc.]
DIMENSIONS : [XXX × YYY mm] + [5mm fonds perdus]

[IMAGE RENDU BAT EN COULEUR]

ÉLÉMENTS À VALIDER :
☐ Contenu texte (orthographe, police, alignements)
☐ Couleur logo vs charte (Note : couleur écran ≠ impression finale)
☐ Mises en page (espacements, géométries)
☐ Découpe / bords (si pertinent)
☐ Reverse / négatif OK ? (si pertinent)

RESPONSABILITÉS :
- Couleur écran : À titre informatif (*non contractuelle*)
  → Client disposera lumière naturelle + comparaison charte papier
- Toute modification après signature → avenant délai +XX jours
- Acceptation BAT = accord qualité et responsabilité

SIGNATURE CLIENT : ________________________ DATE : ___/___/_____

(*) Pour couleur contractuelle, voir "Épreuve de couleur" en option premium
```

### 3. Job Ticket Standardisé (Traçabilité 100%)

**Voir template déjà détaillé en DOMAINE 2.3**

### 4. Questionnaire Sourcing Sous-Traitant

```
AUDIT PARTENAIRE PRODUCTION

Capacités techniques :
□ Techno UV plat / Techno UV roll / Éco-solv / Sublimation ?
□ Supports max ? (dimensions, épaisseurs)
□ Finition : lamination / découpe / rainage / gravure ?
□ Délais : PDF reçu → livraison (combien jours std) ?

Qualité :
□ Préflight systématique ? Normes (GWG / ISO 12647) ?
□ Gestion couleur : profil ICC, épreuve dispo ?
□ Tolérance couleur : ΔE < ? Mesure spectro incluse ?
□ Taux de retouches/défauts (% refusé) ?

Logistique :
□ Emballage : type, protection, traçabilité ?
□ Volume break : prix à Qte 1 / 10 / 100 / 500 ?
□ Délai rush possible ? Surcoût ?
□ Réassorts : stock tampon ?

Partenariat :
□ EDI / API connection possible ? Pour tracking ?
□ Contact dédicacé ? Réactivité (SLA) ?
□ Réunion annuelle review / amélioration continue ?
```

---

## 📋 CONCLUSION : LE "SKILL STACK" FINAL

```
🔵 DÉCOUVERTE (Besoin / Destination)
   ↓
🟢 INGÉNIERIE MATIÈRE/PROCÉDÉ (Choix techno)
   ↓
🟡 SÉCURISATION FICHIERS (Préflight / PDF/X)
   ↓
🔴 PILOTAGE PRODUCTION (Sourcing / suivi)
   ↓
🟣 QUALITÉ / GESTION COULEUR (ISO / GWG standards)
   ↓
🟠 POSE / LOGISTIQUE (Livraison + site)
   ↓
🔵 SAV & RÉASSORTS (Archivage + évolution)
```

Chaque étape est **interdépendante**, mais permet une **modularité évolutive**.
Le "print management" = **orchestration de cette chaîne**.

---

**Version** : 1.0 (Foundation)
**Dernière mise à jour** : 2026-02-13
**Propriétaire** : PrimeCenter Print Management System
