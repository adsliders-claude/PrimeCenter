# Matrice de Décision Matières PrimeCenter

**Objectif** : Recommander la matière optimale en fonction de 6 critères clés.

**Mode d'emploi** : Remplir les colonnes, suivre la logique décisionnelle.

---

## 🎯 LES 6 CRITÈRES CLÉS (Dans cet ordre)

| Critère | Description | Impact |
|---|---|---|
| **1. DURÉE** | Durée de vie requise | Élimine les solutions inadaptées |
| **2. USAGE** | Destination + exposition | Détermine famille matière |
| **3. SUPPORT** | Surface d'application | Élimine incompatibilités adhésif |
| **4. COMPLEXITÉ GÉOMÉTRIQUE** | Forme, détourage, courbes | Détermine rigidité / conformabilité |
| **5. BUDGET** | Enveloppe client | Affine techno impression |
| **6. ESTHÉTIQUE** | Finition attendue (brillant, mat, textile…) | Sélectionne finition finale |

---

## 🚀 ARBRE DE DÉCISION RAPIDE

```
START: Découverte > Diagnostic complet réalisé

QUESTION 1 : DURÉE ?
├─ < 7 jours (événement court)
│  └─ → Carton alvéolaire (ÉCONO) ou Vinyl monomère (standard)
│
├─ 1-3 mois (promo courte)
│  ├─ Intérieur ? → Vinyl monomère ✓ (simple, budget)
│  └─ Extérieur léger ? → Vinyl monomère + lamination simple ✓
│
├─ 3-12 mois (saison / moyen terme)
│  ├─ Intérieur → Vinyl monomère ✓ OU Mur tendu textile (premium)
│  └─ Extérieur → Vinyl polymère ✓ + lamination adapté
│
├─ 1-3 ans (standard)
│  ├─ Intérieur → Vinyl monomère OK, Dibond recommandé (premium)
│  ├─ Extérieur semi → Vinyl polymère ✓ + lamination mat
│  └─ Extérieur plein UV → Vinyl coulé ✓ + lamination anti-UV
│
└─ 3-7+ ans (longue durée / pérenne)
   ├─ Intérieur → Dibond ✓ (premium) ou Mur tendu SEG (changement facile)
   ├─ Extérieur → Vinyl coulé ✓✓ + lamination anti-UV (OBLIGATOIRE)
   └─ Véhicule → Vinyl coulé polymère ✓✓ (cast, meilleure stabilité thermique)

QUESTION 2 : SUPPORT + ADHÉSION ?
├─ Verre lisse → Vinyl adhésif OU film transparent ✓ (énergie surface haute)
├─ Peinture lisse → Vinyl adhésif ✓ (OK si surface propre)
├─ Peinture texturée / crépis → Vinyl polymère/coulé ✓ (conformabilité)
├─ Béton brut → Primaire + Vinyl polymère ✓ (porosité)
├─ Plastique PVC/polycarbonate → Adhésif spécifique ✓ (faible énergie)
├─ Métal galvanisé / inox → Vinyl adhésif ✓ (OK, adhésion facile)
└─ Bois → Préparation + Vinyl adhésif ✓ (si peint) OU Dibond fixation mécanique

QUESTION 3 : GÉOMÉTRIE + FORME ?
├─ Forme simple + surface plane → Vinyl monomère ✓, PVC, Dibond OK
├─ Forme complexe + reliefs modérés → Vinyl polymère/coulé ✓ (conformable)
├─ Reliefs importants / courbes → Vinyl coulé ✓✓ (seul choix fiable)
├─ Détourage fin / découpe complexe → Vinyl rigide OK mais nécessite
│                                      poseur expérimenté
└─ Assemblage pièces → Contrecollage + bridage alu (Dibond + alu recommandé)

QUESTION 4 : BUDGET ?
├─ ÉCONO (min) → Carton / Vinyl monomère / PVC 1mm
├─ STANDARD (moyen) → Vinyl polymère / Alvéolaire / PVC 3mm
├─ PREMIUM (max) → Vinyl coulé / Dibond / Mur tendu SEG / Textile backlit
└─ [Budget détermine aussi techno impression : éco-solv vs UV vs sublimation]

QUESTION 5 : ESTHÉTIQUE + FINITION ?
├─ Brillant → Vinyl adhésif standard (brillant naturel) OU Dibond laqué
├─ Mat discret → Vinyl + lamination mat ✓ OU PVC mat
├─ Satin/soyeux → Vinyl polymère + lamination satin ✓
├─ Texture grainée → Vernis spécialisé (sur Dibond)
├─ Textile naturel → Mur tendu / drapeaux / backlit textile ✓✓
└─ Antireflet (museum) → Lamination antireflet (coût premium)

RÉSULTAT : Matière + Techno + Finition + Budget + Délai → RECOMMANDATION ✓
```

---

## 📊 MATRICE DÉCISION COMPLÈTE (Format Consultation)

**Remplir le tableau ci-dessous avec les critères du projet :**

### Template Décision Projet

```
╔════════════════════════════════════════════════════════════════╗
║ DÉCISION MATIÈRE - [Nom Projet] [Date]
╠════════════════════════════════════════════════════════════════╣
║ CRITÈRE | RÉPONSE CLIENT | ANALYSE | FAMILLE PROPOSÉE
╠════════════════════════════════════════════════════════════════╣

1. DURÉE
   └─ Client : [Ex: 3-5 ans]
   └─ Analyse : [Ex: Durée moyenne = vinyl polymère ou coulé]
   └─ Recommandation : [Ex: Vinyl polymère pour coût, coulé pour premium]

2. USAGE (DESTINATION)
   └─ Client : [Ex: Façade extérieur plein sud]
   └─ Analyse : [Ex: UV max + pluie = stabilité couleur critique]
   └─ Recommandation : [Ex: Lamination anti-UV obligatoire]

3. SUPPORT
   └─ Client : [Ex: Béton brut poreux, humide]
   └─ Analyse : [Ex: Adhésion risque = préparation + adhésif polymère]
   └─ Recommandation : [Ex: Primaire + Vinyl polymère OK]

4. GÉOMÉTRIE
   └─ Client : [Ex: Relief important, formes courbes]
   └─ Analyse : [Ex: Besoin conformabilité = vinyl rigide impossible]
   └─ Recommandation : [Ex: Vinyl coulé OBLIGATOIRE]

5. BUDGET
   └─ Client : [Ex: Budget serré]
   └─ Analyse : [Ex: Limite options premium]
   └─ Recommandation : [Ex: Vinyl monomère/polymère + éco-solv]

6. ESTHÉTIQUE
   └─ Client : [Ex: Premium discret, mat, haut de gamme]
   └─ Analyse : [Ex: Finition importante = impacte techno]
   └─ Recommandation : [Ex: Vinyl coulé + lamination mat satin]

╠════════════════════════════════════════════════════════════════╣
║ SYNTHÈSE RECOMMANDATION
╠════════════════════════════════════════════════════════════════╣

✓ MATIÈRE PROPOSÉE : [Ex: Vinyl polymère coulé 100µm]
✓ ADHÉSIF : [Ex: Polymère acrylique fort]
✓ FINITION : [Ex: Lamination mat anti-UV]
✓ TECHNO IMPRESSION : [Ex: UV éco-solv]
✓ SUPPORT RIGIDE (si besoin) : [Ex: PVC 3mm ou Dibond si premium]
✓ POSE SPÉCIALE : [Ex: Primaire + séchage 24h]
✓ DÉLAI ESTIMÉ : [Ex: 5 jours production + 2 jours pose]
✓ BUDGET ESTIMATION : [Ex: 1500€ HT]

⚠ RISQUES IDENTIFIÉS :
• [Risque 1]
• [Risque 2]

MITIGATION :
→ [Plan d'action]

✅ VALIDATION : [Nom] le [Date]
╚════════════════════════════════════════════════════════════════╝
```

---

## 🎯 CAS D'USAGE FRÉQUENTS (Exemples Décision)

### CAS 1 : Vitrine Verre, Temporaire 3 mois, Esthétique Premium

**Données Entrée:**
- Durée : 3 mois
- Support : Verre lisse
- Usage : Intérieur vitrine
- Géométrie : Simple (rectangulaire)
- Budget : Standard

**Processus Décision:**
```
Q1. Durée 3 mois? → Vinyl monomère POSSIBLE, polymère MIEUX
Q2. Vitrine intérieur? → Pas d'UV critique
Q3. Support verre lisse? → Adhésion facile, adhésif standard OK
Q4. Géométrie simple? → Vinyl monomère OK
Q5. Budget standard? → Vinyl polymère pour durée+qualité
Q6. Esthétique? → Brillant naturel, vinyl adhésif OK
```

**RECOMMANDATION FINALE:**
```
✓ Vinyl polymère 100µm, adhésif standard, brillant
✓ Techno : Éco-solv (qualité, coût optimisé)
✓ Finition : Brillant naturel (pas de lamination sauf demande)
✓ Délai : 2-3 jours production
✓ Coût : €€ (standard)
```

---

### CAS 2 : Façade Béton, Extérieur 5 ans Plein Sud, Premium

**Données Entrée:**
- Durée : 5 ans
- Support : Béton brut poreux
- Usage : Extérieur plein UV
- Géométrie : Formes courbes légères
- Budget : Premium

**Processus Décision:**
```
Q1. Durée 5 ans? → Vinyl coulé polymère RECOMMANDÉ
Q2. Extérieur plein sud? → UV max = lamination anti-UV OBLIGATOIRE
Q3. Support béton brut? → Porosité + humidité = primaire + adhésif fort
Q4. Géométrie courbes? → Vinyl coulé NÉCESSAIRE (seule solution)
Q5. Budget premium? → Coulé OK, lamination anti-UV incluse
Q6. Esthétique? → Mat discret = lamination mat anti-UV
```

**RECOMMANDATION FINALE:**
```
✓ Vinyl coulé polymère 100µm + lamination mat anti-UV
✓ Adhésif : Polymère fort, spécial béton porosité
✓ Préparation : Primaire béton + nettoyage complet
✓ Techno : Éco-solv (qualité UV, conformabilité)
✓ Finition : Lamination satin mat anti-UV (protection + esthétique)
✓ Délai : 5-7 jours (production + lamination)
✓ Coût : €€€ (premium, justifié durée+qualité)
✓ RISQUES : Humidité béton = audit site OBLIGATOIRE + séchage 48h min avant pose
```

---

### CAS 3 : Magasin Murs, Intérieur, Déco Changeante, Premium, 2 ans

**Données Entrée:**
- Durée : 2 ans (mais changeant régulièrement)
- Support : Mur peint lisse
- Usage : Intérieur décoration
- Géométrie : Formes standards
- Budget : Premium
- Besoin : Changeabilité + rendu textile

**Processus Décision:**
```
Q1. Durée 2 ans? → Vinyl polymère OK ou mur tendu
Q2. Intérieur décor? → Pas d'UV critique, esthétique important
Q3. Support mur peint? → OK adhésion facile
Q4. Géométrie standard? → Vinyl adhésif OK
Q5. Budget premium + changeabilité? → Mur tendu SEG RECOMMANDÉ
Q6. Esthétique texture? → Textile rendu naturel premium
```

**RECOMMANDATION FINALE:**
```
✓ Mur tendu textile (SEG system) = changeabilité facile
✓ Matière : Polyester enduit 150g/m², rendu textile naturel
✓ Support : Profilé alu romain SEG (réutilisable)
✓ Installation : Encastrement toile dans profilé (professionnel)
✓ Techno : Sublimation textile (qualité, rendu unique)
✓ Esthétique : Satin naturel, tactile textile
✓ Durée profilé : 10 ans / Durée toile : 2-3 ans (changeant)
✓ Coût : €€€ (system installation + textile)
✓ AVANTAGE : Changements faciles, zéro résidu, stockage toiles anciennes
```

---

### CAS 4 : Enseigne Commerciale, Dibond Extérieur, 7 ans, Premium

**Données Entrée:**
- Durée : 7 ans (pérenne)
- Support : Structure alu fixation mécanique
- Usage : Extérieur façade pérenne
- Géométrie : Enseigne carrée plaque
- Budget : Premium (établissement haut de gamme)
- Esthétique : Premium, finish haut de gamme

**Processus Décision:**
```
Q1. Durée 7 ans? → Matière rigide durable = Dibond
Q2. Extérieur pérenne? → Stability maximum
Q3. Support alu fixation mécanique? → Dibond ideal (collage + rivet)
Q4. Géométrie simple enseigne? → Dibond OK, usinage possible
Q5. Budget premium? → Dibond 6mm + finition haute
Q6. Esthétique premium? → Dibond laqué brillant OU mat haut de gamme
```

**RECOMMANDATION FINALE:**
```
✓ Dibond 6mm (alu sandwich 3-3)
✓ Vinyl adhésif polymère coulé OU impression directe Dibond
✓ Finition : Lamination brillant HD OU vernis mat premium
✓ Fixation : Rivet + adhésif (combiné)
✓ Techno : UV plat (qualité max, Dibond + UV plat = premium)
✓ Bords : Chant alu anodisé noir/argent
✓ Usinage : Possibilité découpe, gravure, bord arrondi
✓ Durée : 7+ ans extérieur (très stable)
✓ Coût : €€€€ (premium, but enseigne pérenne haute gamme)
✓ MAINTENANCE : Nettoyage régulier possible (résiste chimie)
```

---

## 🎯 TABLEAU COMPARATIF MATIÈRES (Quick Ref)

| Matière | Durée Ext | Coût | Complexité Géom | Esthétique | Meilleur Usage |
|---|---|---|---|---|---|
| Carton Alvéolaire | 7j-1m | € | Haute | Basique | Événement court |
| Vinyl Monomère | 1-3 mois | € | Faible | Standard | Promo courte |
| Vinyl Polymère | 1-3 ans | €€ | Moyenne | Bon | Standard commercial |
| Vinyl Coulé | 3-7 ans | €€€ | Haute | Premium | Longue durée + courbes |
| PVC 1mm | 1-2 ans | € | Moyenne | Basique | Budget intérieur |
| PVC 3mm | 2-3 ans | €€ | Moyenne | Bon | Signalétique |
| Dibond 3mm | 5-10 ans | €€€ | Moyenne | Premium | Enseigne standard |
| Dibond 6mm | 10+ ans | €€€€ | Moyenne | Premium+ | Enseigne pérenne |
| Mur Tendu SEG | 2-5 ans toile | €€€ | Haute | Premium texture | Déco intérieur changeant |
| Textile Backlit | 3-5 ans | €€€ | Moyenne | Premium éclairé | Affichage intérieur luxury |

---

**Version** : 1.0
**Date** : 2026-02-13
