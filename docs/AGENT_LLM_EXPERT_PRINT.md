# Spécification Agent LLM — Expert Print Manager
**Rôle:** Agent IA autonome pour la gestion complète des commandes d'impression
**Modèle:** Claude (claude-opus-4-6) via API Anthropic
**Version:** 1.0 — Fév 2026

---

## 🎯 Mission de l'Agent

```
L'Agent "Expert Print Manager" est un assistant IA spécialisé qui:

1. STRUCTURE le brief client:
   → Collecte toutes les informations nécessaires
   → Vérifie la complétude et la cohérence
   → Détecte les problèmes avant production

2. GÉNÈRE la nomenclature automatiquement:
   → Crée: 012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf
   → Choisit la recette PrimeCenter adaptée
   → Valide les dimensions et matières

3. PRÉPARE la communication:
   → Brief structuré pour le deviseur
   → Email au client avec récapitulatif
   → Fiche atelier pour la production

4. COORDONNE le workflow:
   → Déclenche le traitement PrimeCenter (hotfolder)
   → Suit l'avancement des BAT
   → Notifie les parties prenantes
```

---

## 🧠 Knowledge Base de l'Agent

### Catalogue des Matières (gangName)
```python
CATALOGUE_MATIERES = {
    # Films et vinyles
    "Vinyl80":    {"desc": "Vinyle adhésif 80 microns", "prix_m2": 8.50, "imprimante": "Roland"},
    "Vinyl120":   {"desc": "Vinyle adhésif 120 microns", "prix_m2": 12.00, "imprimante": "Roland"},
    "Vitro200":   {"desc": "Vitrophanie 200 microns (sans solvant)", "prix_m2": 15.00, "imprimante": "Mimaki"},
    "Orange02":   {"desc": "Film orange translucide", "prix_m2": 18.00, "imprimante": "Mimaki"},

    # Bâches
    "Bache340":   {"desc": "Bâche PVC 340g/m²", "prix_m2": 6.00, "imprimante": "Grand format"},
    "Bache550":   {"desc": "Bâche PVC 550g/m² (renforcé)", "prix_m2": 9.00, "imprimante": "Grand format"},

    # Papiers et satin
    "Satin100":   {"desc": "Satin photo 100g/m²", "prix_m2": 3.50, "imprimante": "Epson"},
    "Papier200":  {"desc": "Papier couché 200g", "prix_m2": 2.50, "imprimante": "HP"},

    # Rigides
    "PVC3mm":     {"desc": "PVC rigide 3mm blanc", "prix_m2": 25.00, "imprimante": "Platine"},
    "Dibond3mm":  {"desc": "Dibond aluminium 3mm", "prix_m2": 45.00, "imprimante": "Platine"},

    # [À compléter selon votre catalogue]
}
```

### Règles Métier Connues
```python
REGLES_METIER = {
    "resolution_min": 72,         # DPI minimum acceptable (impression grand format)
    "resolution_recommandee": 150, # DPI recommandé (standard)
    "resolution_ideale": 300,      # DPI idéal (stickers, petits formats)

    "fond_perdu_standard": 5,      # mm par défaut
    "fond_perdu_vitrine_haut": 20, # mm recouvrement vitrine
    "fond_perdu_vitrine_bas": 50,  # mm repli vitrine
    "fond_perdu_bache": 30,        # mm renfort bâche

    "espacement_oeillets": 250,    # mm entre oeillets (bâche)
    "espacement_nesting": 5,       # mm entre visuels (nesting)

    "format_max_rouleau": 1300,    # mm largeur max imprimante rouleau standard
    "delai_bat_standard": 2,       # jours ouvrés
    "delai_prod_standard": 5,      # jours ouvrés
}
```

---

## 💬 Skills de l'Agent

### Skill 1: Collecte du Brief
```
ENTRÉE: Conversation avec client/commercial
SORTIE: Formulaire brief complet structuré

L'agent DOIT collecter:
□ Identité: Qui est le client? Quel dossier?
□ Type produit: Vitrine? Sticker? Bâche? (→ jobName)
□ Matière: Sur quel support? (→ gangName)
□ Dimensions: Largeur × Hauteur en mm? (→ formatWidth/Height)
□ Quantité: Combien d'exemplaires? (→ copies)
□ Fichier: PDF fourni? En quel état?
□ Délai: Pour quand?
□ Options: Découpe? Finition? (→ choix recette)

Si informations manquantes → RELANCER avec questions précises
Ne jamais valider un brief incomplet!

Checklist de vérification:
✓ Toutes les dimensions confirmées en mm?
✓ Fichier disponible et format OK?
✓ Matière existe dans catalogue?
✓ Délai cohérent avec charge atelier?
✓ CutContour nécessaire?
```

### Skill 2: Génération Nomenclature
```
ENTRÉE: Brief complet validé
SORTIE: Nom de fichier standardisé + ticket XML

Code de génération:
  order_id = CRM.get_next_order_id()  # Auto-incrémenté
  job_id = "001"                       # Premier visuel
  job_name = brief["product_type"]     # Ex: "Vitrine"
  gang_name = brief["material"]        # Ex: "Orange02"
  width = brief["width_mm"]            # Ex: 1210
  height = brief["height_mm"]          # Ex: 650
  copies = brief["copies"]             # Ex: 20

  filename = f"{order_id}_{job_id}_{job_name}_{gang_name}_{width}x{height}mm_{copies}ex.pdf"
  # → 012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf

Validation automatique:
  ✓ Dimensions dans les limites de la matière?
  ✓ Copies cohérentes avec type produit?
  ✓ Recette déterminée automatiquement?
```

### Skill 3: Vérification Fichier
```
ENTRÉE: Fichier PDF/PSD/JPG du client
SORTIE: Rapport de conformité + recommandations

Vérifie (via metadata du fichier):
  ✓ Format fichier supporté (.pdf, .psd, .jpg, .png)?
  ✓ Dimensions cohérentes avec brief?
  ✓ Résolution suffisante pour le format d'impression?
    → Formule: DPI réel = (px_largeur ÷ largeur_mm) × 25.4
    → Si DPI < 72: REFUSER
    → Si 72 ≤ DPI < 150: AVERTIR
    → Si DPI ≥ 150: OK
  ✓ Mode couleur: CMYK recommandé (RGB = conversion par PrimeCenter)
  ✓ Fond perdu déjà présent? (sinon PrimeCenter l'ajoute)

Rapport généré:
  {
    "conforme": true/false,
    "resolution_dpi": 150,
    "mode_couleur": "RGB",
    "fond_perdu_present": false,
    "recommandations": ["Conversion RGB→CMYK par PrimeCenter", "Fond perdu sera ajouté"],
    "bloquant": false
  }
```

### Skill 4: Calcul de Devis
```
ENTRÉE: Brief complet + catalogue matières + tarifs
SORTIE: Devis structuré prêt à envoyer

Calcul:
  surface_m2 = (width_mm × height_mm) / 1_000_000  # Convertit mm² en m²
  prix_matiere = surface_m2 × CATALOGUE[gang_name]["prix_m2"] × copies

  temps_impression = surface_m2 × vitesse_m2/h_imprimante × copies
  prix_impression = temps_impression × taux_horaire_imprimante

  prix_facon = 0  # Si découpe simple: prix/passe cutter
  si oeillets: prix_facon += nb_oeillets × prix_oeillet

  total_ht = prix_matiere + prix_impression + prix_facon + marge_agence
  tva = total_ht × 0.20
  total_ttc = total_ht + tva

Exemple pour 012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf:
  surface = (1210 × 650) / 1_000_000 = 0.787 m²
  prix_mat = 0.787 × 18€ × 20 = 283€
  temps_impr = 0.787 × 20 ÷ 40 m²/h = ~24 min
  prix_impr = 0.4h × 80€/h = 32€
  marge (30%) = 94€
  Total HT = ~409€
  TVA = 82€
  Total TTC = ~491€
```

### Skill 5: Préparation Email/Brief
```
ENTRÉE: Brief complet + devis calculé
SORTIE: Email structuré (à envoyer au client ou deviseur)

Templates disponibles:
  1. Email BRIEF CLIENT:
     "Bonjour [Client], voici le récapitulatif de votre commande..."
     + Tableau: Type, Format, Matière, Quantité, Délai
     + Prix estimatif (si devis validé)

  2. Email BRIEF DEVISEUR:
     "Nouvelle commande à devis: Dossier [OrderId]"
     + Fiche technique complète
     + Fichier joint

  3. Fiche ATELIER:
     "Ordre de production #[OrderId]"
     + Type recette, dimensions, copies
     + Instructions spéciales
     + Code QR pour traçabilité
```

---

## 🔧 Intégration Technique

### API PrimeCenter (via Hotfolder)
```python
# L'agent communique avec PrimeCenter via les scripts Python:

def soumettre_a_primecenter(filename: str, mode: str = "bat"):
    """Copie le fichier dans le hotfolder INPUT pour traitement."""
    import shutil
    from pathlib import Path

    source = Path("C:/Downloads") / filename
    destination = Path(r"\\obelix_nascp\Boite de transferts\KARIM\PRIMECENTER"
                       r"\TEST Mise en place\01_INPUT_FILES") / filename
    shutil.copy2(source, destination)
    return f"Soumis à PrimeCenter: {filename}"


def verifier_sortie(filename: str) -> dict:
    """Vérifie si PrimeCenter a généré les fichiers de sortie."""
    from pathlib import Path
    base = Path(filename).stem

    print_dir = Path(r"\\obelix_nascp\...\04 - OUTPUT_PRINTFILES")
    cut_dir = Path(r"\\obelix_nascp\...\04 - OUTPUT_CUTFILES")

    return {
        "print_ready": any(f.stem.startswith(base) for f in print_dir.glob("*.pdf")),
        "cut_ready": any(f.stem.startswith(base) for f in cut_dir.glob("*.*"))
    }
```

### Appel API Claude (pour l'Agent LLM)
```python
import anthropic

client = anthropic.Anthropic(api_key="votre-cle-api")

def agent_expert_print(brief_input: str, contexte: dict) -> str:
    """Appel l'agent Expert Print Manager."""

    system_prompt = """Tu es un Expert en Print Management avec 15 ans d'expérience.
Tu gères des commandes d'impression grand format: vitrines, stickers, bâches, kakémonos.

TU DOIS:
1. Analyser la demande du client
2. Vérifier que toutes les informations sont présentes
3. Générer la nomenclature: OrderId_jobId_jobName_gangName_WxHmm_Nex.pdf
4. Choisir la recette PrimeCenter adaptée
5. Préparer le brief structuré

CATALOGUE MATIÈRES DISPONIBLES:
{catalogue}

RÈGLES MÉTIER:
{regles}

FORMAT NOMENCLATURE: 012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf"""

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": f"Brief client: {brief_input}"
            }
        ],
        system=system_prompt.format(
            catalogue=str(contexte.get("catalogue", {})),
            regles=str(contexte.get("regles", {}))
        )
    )

    return message.content[0].text
```

---

## 📋 Exemples de Conversations

### Exemple 1: Commande Vitrine Complète
```
Client: "J'ai besoin d'une vitrine pour Noël, 1.2m x 0.65m, 20 exemplaires"

Agent: "Parfait! Voici ma vérification:
  ✓ Type: Vitrine → Recette IMPRESSION_VITRINE
  ✓ Dimensions: 1200 × 650mm
  ✓ Quantité: 20 exemplaires

  Questions:
  1. Sur quelle matière? (Film Orange, Film Blanc, autre?)
  2. Avez-vous le fichier prêt? (PDF recommandé)
  3. Découpe nécessaire?"

Client: "Film orange, je t'envoie le PDF, pas de découpe"

Agent: "Voici la nomenclature générée:
  012345_001_Vitrine_Noel_Orange02_1200x650mm_20ex.pdf

  Résumé:
  - Type: Vitrine de Noël
  - Matière: Orange02 (Film orange translucide)
  - Format: 1200 × 650mm + 2cm recouvrement haut + 5cm bas
  - Copies: 20 exemplaires
  - Recette: IMPRESSION_VITRINE_BAT
  - Délai BAT: 2 jours ouvrés

  Prix estimatif: ~245€ HT
  Souhaitez-vous valider ce devis?"
```

### Exemple 2: Brief Incomplet
```
Client: "J'ai besoin de stickers"

Agent: "Pour vos stickers, j'ai besoin de précisions:
  1. Format souhaité? (en mm, ex: 100×100mm, 200×150mm)
  2. Quantité? (minimum 10 exemplaires)
  3. Découpe: Forme carrée/rectangulaire ou forme spéciale?
  4. Support: Vinyle standard, vitrophanie (pour vitres)?
  5. Avez-vous le fichier (logo/visuel) prêt?"

[Continue jusqu'à brief complet]
```

---

## 🚀 Déploiement

### Option A: Agent Claude Code (immédiat)
```
→ Utiliser Claude Code directement comme agent
→ Pas de développement requis
→ Conversation naturelle en français
→ Connecté aux scripts Python via terminal
```

### Option B: Webhook + API (V2)
```python
# Flask API simple pour l'agent
from flask import Flask, request, jsonify
import anthropic

app = Flask(__name__)
client = anthropic.Anthropic()

@app.route("/agent/brief", methods=["POST"])
def traiter_brief():
    data = request.json
    brief = data.get("brief", "")
    reponse = agent_expert_print(brief, {})
    return jsonify({"reponse": reponse})

if __name__ == "__main__":
    app.run(port=5000)
```

### Option C: Interface Web (V3 SaaS)
```
→ React + Claude API direct depuis frontend
→ Formulaire dynamique selon type produit
→ Chat IA intégré pour clarifications
→ Génération et envoi automatique des documents
```

---

**Session:** https://claude.ai/code/session_017yhksCaj1YoCEk79BwGw1G
