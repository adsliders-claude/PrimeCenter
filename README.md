# PrimeCenter — Automation Workflow Setup

**Projet:** Automatisation de la préparation des BAT (Bon À Tirer)
**Système:** Caldera PrimeCenter V4 — Version PRO
**Objectif:** Traiter 500 BAT/jour avec vérification, correction et préparation pour impression/découpe
**Status:** V1 (Test manuel demain) → V2 (Automatisation production)

---

## 📦 Structure du Projet

```
PrimeCenter/
├── README.md (ce fichier)
├── docs/
│   ├── PREFLIGHT_PAO_RECIPE.md         # Documentation complète de la recette
│   ├── FILENAME_CONVENTION.md          # Convention de nommage des fichiers d'entrée
│   ├── MANUAL_TEST_GUIDE_V1.md         # Guide de test manuel (demain)
│   └── AUTOMATION_SETUP_V2.md          # Guide d'automatisation hotfolder (production)
├── recipes/
│   └── PREFLIGHT_PAO_PRO_CONFIGURATION.md  # Configuration détaillée des 8 modules
├── hotfolder/
│   ├── INPUT/                          # Dossier d'entrée (fichiers à traiter)
│   ├── OUTPUT_PRINT/                   # Sortie impression (PDF)
│   ├── OUTPUT_CUT/                     # Sortie découpe (DXF, etc)
│   └── ARCHIVE/                        # Archive des fichiers traités
└── .git/                               # Repository git
```

---

## 🎯 La Recette PREFLIGHT_PAO_PRO

**Objectif:** Automatiser la chaîne de prépresse avec 4 étapes:
1. ✅ **Contrôler** — Vérification PDF (Preflight Check)
2. ✅ **Corriger** — Correction automatique (Preflight Fix)
3. ✅ **Ajouter FP 5mm** — Fond perdu (Bleed Canvas Extend)
4. ✅ **Ajouter CutContour** — Contours de découpe automatiques

**Paramètres clés:**
- **Paquet:** Pro
- **Mode:** Semi-automatisé (V1: manuel, V2: hotfolder auto)
- **Formats entrée:** PDF, PSD, JPG, PNG
- **Formats sortie:** PDF (impression) + DXF/PDF (découpe)
- **Métadonnées:** Extraction depuis noms de fichiers

---

## 📅 Timeline

### **V1 — Demain (Test Manuel)**
- [ ] Créer la recette dans PrimeCenter V4 UI
- [ ] Configurer les 8 modules de la recette
- [ ] Tester avec fichiers d'exemple
- [ ] Valider output impression + découpe
- [ ] Documenter le processus

### **V2 — Production (Automatisation)**
- [ ] Configurer hotfolder d'entrée
- [ ] Setup extraction métadonnées
- [ ] Tests volume (100+ BAT/jour)
- [ ] Monitoring + logs
- [ ] Atteindre 500 BAT/jour

---

## 🚀 Pour Demain

**Fichiers à lire en priorité:**
1. `docs/FILENAME_CONVENTION.md` — Comment nommer les fichiers BAT
2. `recipes/PREFLIGHT_PAO_PRO_CONFIGURATION.md` — Configuration des 8 modules
3. `docs/MANUAL_TEST_GUIDE_V1.md` — Steps de test dans PrimeCenter

**Avant de commencer:**
- ✅ PrimeCenter V4 PRO installé
- ✅ Cutters configurés (si découpe nécessaire)
- ✅ Fichiers d'exemple PDF/PSD/JPG prêts

---

## 📚 Documentation Caldera Intégrée

Ce projet utilise la documentation officielle Caldera PrimeCenter V4 compilée en décembre 2026.
Référence: https://helpdesk.caldera.com

---

## 📞 Support

Pour questions ou issues:
- Consulter la documentation dans `docs/`
- Vérifier la configuration dans `recipes/`
- Tester avec le guide dans `docs/MANUAL_TEST_GUIDE_V1.md`

---

**Session:** https://claude.ai/code/session_017yhksCaj1YoCEk79BwGw1G
