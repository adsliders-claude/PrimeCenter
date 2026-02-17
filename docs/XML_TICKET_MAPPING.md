# XML Ticket Mapping — Nomenclature ↔ PrimeCenter
**Système:** PrimeCenter V4 PRO → MAX (upgrade futur)
**Version:** 1.0 — Fév 2026
**Référence doc:** Structure XML Officielle Caldera PrimeCenter V4.3+

---

## 🎯 Principe

```
NOMENCLATURE FICHIER:
  012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf

         ↓ Python script: parse_nomenclature.py

TICKET XML D'ENTRÉE (pour PrimeCenter MAX ou hotfolder):
  ticket.xml

         ↓ PrimeCenter traite

TICKET XML DE SORTIE (généré par PrimeCenter):
  012345_001_Vitrine_Orange02_1210x650mm_20ex.xml
```

---

## 📊 Mapping Complet Nomenclature ↔ XML

| Segment Filename | Valeur Exemple | XML Tag | Parent |
|-----------------|----------------|---------|--------|
| `OrderId` | `012345` | `<orderID>` | `<job><info>` |
| `jobId` | `001` | `<jobID>` | `<job><info>` |
| `jobName` | `Vitrine` | `<jobName>` | `<job><info>` |
| `gangName` | `Orange02` | `<customerID>` + `<gang>` | `<job><info>` + `<process>` |
| `formatWidth` | `1210` | `<width unit="mm">` | `<job><media>` |
| `formatHeight` | `650` | `<height unit="mm">` | `<job><media>` |
| `copies` | `20` | `<copies>` | `<job><source>` |
| `recette` | calculé | `<recipe>` | `<job><process>` |

---

## 📄 Ticket XML d'ENTRÉE (pour MAX)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ticket version="1">
  <job creationTime="2026-02-17T14:30:00">

    <!-- SOURCE: Fichier à traiter -->
    <source>
      <filespec>file:////obelix_nascp/Boite de transferts/KARIM/PRIMECENTER/TEST Mise en place/01_INPUT_FILES/012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf</filespec>
      <pages>1</pages>           <!-- ← page 1 uniquement (1 jobId = 1 page) -->
      <copies>20</copies>        <!-- ← copie_ex extrait du filename -->
    </source>

    <!-- MEDIA: Dimensions du visuel (sans fond perdu) -->
    <media>
      <width unit="mm">1210</width>   <!-- ← formatWidth extrait -->
      <height unit="mm">650</height>  <!-- ← formatHeight extrait -->
    </media>

    <!-- PROCESS: Recette à appliquer -->
    <process>
      <recipe>IMPRESSION_VITRINE_PROD</recipe>  <!-- ← déterminé par Agent LLM -->
      <gang by="customerID"/>                   <!-- ← groupage par matière (gangName) -->
    </process>

    <!-- INFO: Métadonnées du travail -->
    <info>
      <orderID>012345</orderID>         <!-- ← orderId extrait -->
      <jobID>001</jobID>                <!-- ← jobId extrait -->
      <jobName>Vitrine</jobName>        <!-- ← jobName extrait -->
      <customerID>Orange02</customerID> <!-- ← gangName = matière = "client" dans PrimeCenter -->
      <comment>BatchAuto_2026-02-17</comment>
    </info>

  </job>
</ticket>
```

---

## 📤 Ticket XML de SORTIE (généré par PrimeCenter)

### Ticket par image (sortie par visuel):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<ticket version="1" lastEvent="2026-02-17T15:00:00">

  <!-- PARTIE JOB (identique à l'entrée) -->
  <job creationTime="2026-02-17T14:30:00">
    <source>
      <filespec>file:////obelix_nascp/.../01_INPUT_FILES/012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf</filespec>
      <copies>20</copies>
    </source>
    <media>
      <width unit="mm">1210</width>
      <height unit="mm">650</height>
    </media>
    <info>
      <orderID>012345</orderID>
      <jobID>001</jobID>
      <jobName>Vitrine</jobName>
      <customerID>Orange02</customerID>
    </info>
  </job>

  <!-- PARTIE AMALGAME (ajoutée par PrimeCenter) -->
  <layout name="Nest_Orange02_001" lastEvent="2026-02-17T15:00:00">

    <!-- Méta de l'amalgame -->
    <info>
      <fillRatio>78</fillRatio>     <!-- ← % couverture du média -->
      <stats>
        <area unit="m2">1.573</area>      <!-- Surface visuels -->
        <waste unit="m2">0.441</waste>    <!-- Perte matière -->
      </stats>
      <mediaName>Orange02</mediaName>     <!-- ← gangName utilisé -->
      <gang>Orange02</gang>               <!-- ← groupe de ganging -->
      <width>1300.000000</width>          <!-- ← largeur média réel -->
      <height>1870.000000</height>        <!-- ← hauteur amalgame -->
      <cropped>false</cropped>
    </info>

    <!-- Chemins des fichiers générés -->
    <paths>
      <output timeStamp="2026-02-17T15:00:00">
        file:////obelix_nascp/.../04 - OUTPUT_PRINTFILES/012345_001_Vitrine_Orange02_1210x650mm_20ex_PRINT.pdf
      </output>
      <cut timeStamp="2026-02-17T15:00:00">
        file:////obelix_nascp/.../04 - OUTPUT_CUTFILES/012345_001_Vitrine_Orange02_1210x650mm_20ex_CUT.zcc
      </cut>
    </paths>

    <!-- Position du visuel dans l'amalgame -->
    <contents>
      <job id="001" items="20">
        <item page="1" x="100.0" y="50.0" w="1220.0" h="660.0" angle="0"/>
        <!-- w et h incluent le fond perdu (1210+5+5=1220, 650+5+5=660) -->
      </job>
    </contents>

  </layout>
</ticket>
```

### Ticket par amalgame (sortie globale):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<ticket version="1" lastEvent="2026-02-17T15:00:00">

  <!-- SEULEMENT LA PARTIE LAYOUT (pas de job) -->
  <layout name="Nest_Orange02_001" lastEvent="2026-02-17T15:00:00">
    <info>
      <fillRatio>78</fillRatio>
      <stats>
        <area unit="m2">1.573</area>
        <waste unit="m2">0.441</waste>
      </stats>
      <mediaName>Orange02</mediaName>
      <gang>Orange02</gang>
      <width>1300.000000</width>
      <height>1870.000000</height>
    </info>
    <paths>
      <output>file:////obelix_nascp/.../04 - OUTPUT_PRINTFILES/Nest_Orange02_001_PRINT.pdf</output>
      <cut>file:////obelix_nascp/.../04 - OUTPUT_CUTFILES/Nest_Orange02_001_CUT.zcc</cut>
    </paths>
    <contents>
      <job id="001" items="20">
        <item page="1" x="100.0" y="50.0" w="1220.0" h="660.0" angle="0"/>
      </job>
      <job id="002" items="50">
        <item page="1" x="1350.0" y="50.0" w="510.0" h="510.0" angle="0"/>
        <!-- Sticker 500x500mm + 5mm fond perdu -->
      </job>
    </contents>
  </layout>
</ticket>
```

---

## 🔧 Script Python — Génération Automatique des Tickets XML

Voir: `scripts/windows/create_xml_ticket.py`

### Exemple d'utilisation:
```python
from scripts.windows.create_xml_ticket import create_entry_ticket

# Parse le filename automatiquement
ticket_xml = create_entry_ticket(
    filename="012345_001_Vitrine_Orange02_1210x650mm_20ex.pdf",
    nas_input_path=r"\\obelix_nascp\Boite de transferts\KARIM\PRIMECENTER\TEST Mise en place\01_INPUT_FILES",
    recipe="IMPRESSION_VITRINE_BAT"
)

# Sauvegarde le ticket XML
with open("012345_001_Vitrine_Orange02_1210x650mm_20ex.xml", "w") as f:
    f.write(ticket_xml)
```

---

## 📁 Structure des Fichiers XML dans le NAS

```
\\obelix_nascp\Boite de transferts\KARIM\PRIMECENTER\TEST Mise en place\

06 - RAPPORTS PRIMECENTER\
  ├── 2026-02-17\                                     ← Par date
  │   ├── 012345_001_Vitrine_Orange02_1210x650mm_20ex_ENTREE.xml    ← Ticket entrée créé
  │   ├── 012345_001_Vitrine_Orange02_1210x650mm_20ex_SORTIE.xml    ← Ticket sortie PrimeCenter
  │   └── Nest_Orange02_001_AMALGAME.xml                            ← Ticket amalgame complet
  └── INDEX.csv                                       ← Index tous les traitements
```

---

## 📊 Index CSV — Tracking de Production

PrimeCenter génère les XML, le script Python génère un CSV d'index:

```csv
Date,OrderId,JobId,JobName,GangName,Width,Height,Copies,Recette,Statut,FillRatio,PrintFile,CutFile
2026-02-17,012345,001,Vitrine,Orange02,1210,650,20,IMPRESSION_VITRINE_BAT,OK,78,012345_001_...PRINT.pdf,012345_001_...CUT.zcc
2026-02-17,012345,002,Sticker,Vitro200,500,500,50,VITROPHANIE_STICKERS_BAT,OK,85,012345_002_...PRINT.pdf,012345_002_...CUT.zcc
```

Ce CSV est utilisé par l'Agent LLM pour:
- Suivre l'avancement des commandes
- Générer des rapports de production
- Alimenter le dashboard web

---

## 🚀 Migration PRO → MAX (V3 Future)

```
MAINTENANT (PRO):
  → Pas de lecture des tickets XML d'entrée
  → Extraction depuis NOM DU FICHIER uniquement
  → XML de sortie généré automatiquement par PrimeCenter

FUTUR (MAX):
  → Tickets XML d'entrée LUS par PrimeCenter
  → Plus besoin de convention de nommage stricte
  → PrimeCenter applique recette depuis <recipe> dans XML
  → Paramètres avancés via XML (<preflight> profiles, etc.)

Plan de migration:
1. Scripts Python créent déjà les tickets XML d'entrée (prêt pour MAX)
2. Format XML défini → transition transparente
3. Upgrade MAX → activer lecture XML → tout fonctionne immédiatement
```

---

**Session:** https://claude.ai/code/session_017yhksCaj1YoCEk79BwGw1G
