# Architecture SaaS — Print Management Platform
**Nom:** PrintFlow SaaS (proposition)
**Version:** Architecture V1.0 — Fév 2026
**Objectif:** Automatiser la chaîne complète de production print (brief → devis → BAT → validation → atelier)

---

## 🎯 Vision Globale

```
┌──────────────────────────────────────────────────────────────────────┐
│                    PrintFlow SaaS — Vue Globale                       │
├──────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  CLIENT                 AGENCE                    ATELIER             │
│  ──────                 ──────                    ───────             │
│                                                                        │
│  [Formulaire Brief] → [Agent LLM Expert Print] → [PrimeCenter V4]   │
│         ↓                      ↓                       ↓             │
│  [Devis en ligne]    [Génère nomenclature]    [Traite + Corrige]     │
│         ↓                      ↓                       ↓             │
│  [Signature elec.]   [Crée tickets XML]       [Output Print + Cut]   │
│         ↓                      ↓                       ↓             │
│  [Reçoit BAT PDF]    [Envoie par email]       [Archive + Rapport]    │
│         ↓                                                             │
│  [Valide + Signe]                                                     │
│         ↓                                                             │
│  [Prod. Atelier]                                                      │
│                                                                        │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 📋 Les 4 Modules de l'Application

### Module 1 — BRIEF INTELLIGENT
**Rôle:** Agent LLM "Expert Print Manager" qui structure le brief client

```
ENTRÉE:          → Formulaire dynamique web (selon type produit)
                    Champs: ClientID, Type produit, Matière, Format, Copies
                    + Upload fichier client (PDF, PSD, JPG, PNG)

TRAITEMENT:      → Agent LLM vérifie complétude du brief
                    - Résolution suffisante?
                    - Mode couleur correct (CMYK)?
                    - Données manquantes?
                    - Incohérences (format trop grand pour matière)?
                    → Génère NOMENCLATURE automatique:
                    012345_001_Vitrine_Orange02_1210x650mm_20ex

SORTIE:          → Brief structuré (email ou PDF)
                    - Prêt pour deviseur
                    - Prêt pour atelier
                    - Données utilisables pour chiffrage automatique
```

**Types de formulaires par produit:**
| Type | Champs spécifiques |
|------|-------------------|
| Vitrine | Dimensions, nombre de lés, recouvrement |
| Sticker/Vitrophanie | Dimensions, fond blanc?, miroir? |
| Bâche | Dimensions, type d'oeillets, renfort |
| Impression directe | Dimensions, finition |
| Kakémono/Roll-up | Hauteur, largeur, type de pied |

---

### Module 2 — DEVIS EN LIGNE
**Rôle:** Générer et envoyer un devis professionnel avec signature électronique

```
ENTRÉE:          → Brief validé par Agent LLM
                    + Grille tarifaire (base de données prix matières, main d'œuvre)
                    + Données client (CRM)

TRAITEMENT:      → Calcul automatique:
                    - Prix matière (gangName × surface × copies)
                    - Forfait impression (temps machine × taux horaire)
                    - Façonnage si besoin
                    - Marge agence
                    → Génère PDF devis formaté

SORTIE:          → Devis envoyé par email avec lien de signature
                    - Signature électronique (ex: YouSign, Docusign, HelloSign)
                    - Notification à la réception de la signature
                    - Archivage automatique
```

---

### Module 3 — CRÉATION BAT (Bon À Tirer)
**Rôle:** Traitement automatique du fichier via PrimeCenter, envoi BAT pour validation

```
ENTRÉE:          → Devis signé
                    + Fichier client (uploadé lors du brief)
                    + Nomenclature générée (012345_001_Vitrine_Orange02_...)

TRAITEMENT PrimeCenter:
    ↓ Copie fichier → NAS Hotfolder (01_INPUT_FILES)
    ↓ PrimeCenter traite automatiquement:
       → Recette sélectionnée selon type produit:
          - PREFLIGHT_PAO       → BAT validation
          - IMPRESSION_DIRECTE  → Print direct
          - IMPRESSION_VITRINE  → Vitrine multi-lés
          - VITROPHANIE_STICKERS → Stickers + blanc
          - IMPRESSION_BACHE   → Bâche + oeillets
       → Corrections automatiques (RGB→CMYK, DPI, fonts)
       → Fond perdu ajouté selon recette
       → Contours découpe générés
    ↓ Output:
       → NAS: 02_OUTPUT_PREFLIGHT_FIXUP (BAT corrigé)
       → NAS: 04 - OUTPUT_PRINTFILES (fichier impression)
       → NAS: 04 - OUTPUT_CUTFILES (fichier découpe)

SORTIE:          → BAT PDF envoyé client par email
                    - Interface web de validation en ligne
                    - Outils de commentaire et annotation
                    - Signature électronique validation BAT
                    - Si corrections → retour fichier → cycle repris
```

---

### Module 4 — PRODUCTION ATELIER
**Rôle:** Transmettre les fichiers validés à l'atelier avec tous les détails de production

```
ENTRÉE:          → BAT signé par client
                    + Fichiers de production (PRINT + CUT)
                    + Ticket XML de sortie PrimeCenter (métadonnées)

TRAITEMENT:      → Création fiche de travail atelier:
                    - Matière: gangName (Orange02, Vinyl80, etc.)
                    - Format: 1210x650mm
                    - Copies: 20ex
                    - Type: Vitrine
                    - Découpe: DXF joint
                    - Instructions spéciales: recouvrement 2cm, etc.

SORTIE:          → Dashboard atelier:
                    - File de production organisée par matière (gangName)
                    - Amalgames optimisés (même matière groupée)
                    - Bon de livraison généré
                    - Suivi en temps réel
```

---

## 🏗️ Architecture Technique

### Stack Recommandé

```
Frontend (Interface Web):
  ├── Framework: React.js / Next.js
  ├── UI: Tailwind CSS + Shadcn/UI
  ├── PDF viewer: PDF.js (visualisation BAT)
  ├── Annotations: Konva.js ou Fabric.js (commentaires BAT)
  └── Signature: YouSign API / Docusign API

Backend (API + Agent):
  ├── Langage: Python (FastAPI)
  ├── Agent LLM: Claude API (Anthropic)
  │   └── Modèle: claude-opus-4-6 (le plus capable)
  ├── Gestion fichiers: Python + watchdog (hotfolder monitor)
  ├── Email: SendGrid / Mailgun
  └── Base de données: PostgreSQL

Intégration PrimeCenter:
  ├── V1/V2 (PRO): Hotfolder NAS
  │   ├── Input: \\obelix_nascp\...\01_INPUT_FILES
  │   └── Output: \\obelix_nascp\...\04 - OUTPUT_PRINTFILES
  ├── V3 (MAX): XML tickets bidirectionnels
  └── Monitoring: Python watchdog (surveille dossiers NAS)

Signature Électronique:
  ├── YouSign (français, RGPD, API simple)
  ├── ou Docusign (international)
  └── Recommandation: YouSign (RGPD + simple)

Stockage:
  ├── Fichiers actifs: NAS \\obelix_nascp\...
  ├── Archive: Cloud (Infomaniak kDrive)
  └── Métadonnées: PostgreSQL
```

---

## 🔄 Flux de Données Complet

```
BRIEF COMPLET:
[Client] → Formulaire Web
         → [Agent LLM] Vérifie + Structure
         → Génère nomenclature: 012345_001_Vitrine_Orange02_1210x650mm_20ex
         → Crée ticket XML d'entrée PrimeCenter

DEVIS:
[Agent] → Calcule prix depuis:
          - Base matières (gangName → prix/m²)
          - Base main d'œuvre (type → temps machine)
          - Base client (remises, conditions)
        → PDF devis généré + envoyé
        → [Client] signe en ligne
        → Statut: "Devis signé" → déclenche création BAT

BAT:
[Script Python Windows] → Copie fichier client dans hotfolder NAS
                          → Crée ticket XML d'entrée (nomenclature)
[PrimeCenter] → Détecte hotfolder → Applique recette
              → Génère BAT corrigé
              → Génère ticket XML de sortie
[Script Python] → Détecte output → Upload vers interface web
[Client] → Reçoit BAT → Valide ou commente
         → Si corrections → Retour au début BAT
         → Si OK → Signe → Production

PRODUCTION:
[Atelier] → Reçoit fiche production automatique
          → Files de travail organisées par matière
          → Fichiers Print + Cut prêts
```

---

## 📅 Roadmap

### Phase 1 — Aujourd'hui/Demain: Fondations
```
✅ PrimeCenter V4 PRO opérationnel
✅ Structure NAS définie
☐ Recettes configurées (5 types)
☐ Nomenclature validée
☐ Scripts Python Windows pour hotfolder
☐ Test manuel V1 validé
```

### Phase 2 — Semaine 1-2: Automatisation Hotfolder
```
☐ Scripts Windows pour:
    - Parse nomenclature ← hotfolder
    - Monitor NAS (input/output)
    - Créer tickets XML entrée (V3 MAX)
    - Renommer fichiers sortie selon nomenclature
☐ Agent LLM: Brief → Nomenclature
☐ 100 BAT/jour traités
```

### Phase 3 — Mois 1-2: Interface Web
```
☐ Formulaire brief en ligne
☐ Génération devis automatique
☐ Envoi BAT par email
☐ Interface validation client (PDF + commentaires)
☐ Tableau de bord atelier
```

### Phase 4 — Mois 3-6: SaaS Complet
```
☐ Multi-clients (plusieurs agences)
☐ Signature électronique (YouSign)
☐ CRM intégré
☐ ERP basique (stock matières, planning machines)
☐ Rapports et statistiques
☐ API publique
```

### Phase 5 — Futur: Upgrade MAX + AI
```
☐ PrimeCenter MAX → XML tickets bidirectionnels
☐ IA: suggestion de correction, détection problèmes
☐ Optimisation automatique amalgames
☐ Prédiction délais et coûts
```

---

## 🔧 Outil d'Automatisation PC: pyautogui

**Pourquoi pyautogui?**
```
✅ Python (même langage que le reste)
✅ Gratuit et open source
✅ Windows natif
✅ Simple: screenshot + click + type
✅ Utilisé uniquement si hotfolder insuffisant

Installation:
pip install pyautogui Pillow pywin32

Usage typique:
import pyautogui
pyautogui.click(x=100, y=200)       # Cliquer
pyautogui.typewrite('texte')        # Taper
pyautogui.screenshot('screen.png') # Screenshot
```

**IMPORTANT:** Pour PrimeCenter, on utilise PRIORITAIREMENT le hotfolder.
pyautogui = seulement pour configurer PrimeCenter UI (actions manuelles rares).

---

## 📞 Intégrations Externes Recommandées

| Besoin | Outil recommandé | Prix | API |
|--------|-----------------|------|-----|
| Signature élec. | YouSign | ~20€/mois | Oui, simple |
| Email transac. | SendGrid | Gratuit 100/j | Oui |
| PDF viewer | PDF.js | Gratuit | - |
| Annotations | Konva.js | Gratuit | - |
| Base de données | Supabase | Gratuit tier | Oui |
| Hosting | Vercel + Railway | Gratuit tier | - |
| LLM | Anthropic Claude API | Usage | claude-opus-4-6 |

---

**Session:** https://claude.ai/code/session_017yhksCaj1YoCEk79BwGw1G
