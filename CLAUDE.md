# CLAUDE.md — MSP OS Engine — Launch Site

> Ce fichier est lu automatiquement par Claude Code à chaque session.
> Il décrit l'architecture complète du dépôt pour éviter toute improvisation.
> Format aligné sur le gabarit canonique : `Factory/90_KNOWLEDGE/BUNDLE_PACK__TEAM_TEMPLATE/TEMPLATE__CLAUDE_MD.md`.

---

## 1. IDENTITÉ DU PRODUIT

| Champ | Valeur |
|---|---|
| **Nom** | MSP OS Engine — Launch Site (site de lancement MSP) |
| **Code repo** | `eriqallain-afk/MSP_OS_ENG_LAUNCH_SITE` |
| **Nature** | Site web **statique** (HTML/CSS/JS) — GitHub Pages |
| **Produit présenté** | MSP Intelligence AI (repo `eriqallain-afk/IT`) — produit phare EA\|IA |
| **Produit par** | Factory (repo `eriqallain-afk/Factory`) |
| **Responsable** | EA (validation manuelle obligatoire pour toute mise en ligne) |

MSP OS Engine — Launch Site est le **site de lancement** dédié au produit **MSP Intelligence IT**. Comme `MSP_OS_ENGINE`, il ne contient **pas d'agents IA** (ceux-ci vivent dans le repo `IT`) : il rassemble landing, pages produit et casepages anonymisées pour la campagne de lancement.

> ✅ **Ce dépôt est le site MSP canonique** (acté EA 2026-06-21). `eriqallain-afk/MSP_OS_ENGINE` est le jumeau historique non canonique — tout développement futur se fait ici.

---

## 2. STRUCTURE DU REPO

```
MSP_OS_ENG_LAUNCH_SITE/
├── CLAUDE.md                    ← Ce fichier
├── README.md                    ← Origine, règle d'anonymisation, déploiement
├── index.html                   ← Landing de lancement
├── msp-preview.html             ← Page produit MSP (modules, agents phares, Risk Engine, tarifs)
├── entreprises.html             ← Page équipes TI internes / PME (non-MSP)
├── clarification-copilot-vs-it-os.html ← Clarification sécurité MSP OS vs Copilot Graph
├── it-intelligence-os.html      ← Brouillon autonome — non indexé, non relié au site
├── .nojekyll                    ← Désactive Jekyll (HTML brut)
├── pages/                       ← 20 casepages MSP extraites et anonymisées
│   ├── msp-demos.html           ← Index des casepages
│   └── eaia_case_*.html / msp-case-*.html
├── docs/                        ← Miroir publié + campagne
├── assets/images/, img/         ← Visuels
├── og-image*.png                ← Open Graph (partage social)
├── MSP_OS_ENG_LAUNCH_SITE.zip   ← Archive de la version extraite (artefact)
├── scan-anonymisation.ps1       ← Scan PowerShell (usage local Windows)
├── scripts/scan_anonymisation.py ← Scan portable (Python) — utilisé par la CI
├── scripts/check_image_weight.py ← Garde-fou de poids des images (budget 500 Ko, grandfather)
├── scripts/image_weight_allowlist.txt ← Images actuelles tolérées (cliquet)
└── .github/workflows/            ← CI : anonymisation.yml + image-weight.yml (gates bloquants)
```

---

## 3. COMPOSANTS DU SITE (pas d'agents)

Site statique : **aucune couche d'agents OPS/Métier**. Le tableau remplace la section « Agents » du gabarit.

| Composant | Rôle |
|---|---|
| `index.html` | Landing de lancement MSP Intelligence IT |
| `msp-preview.html` | Page produit MSP — 9 modules, 3 agents phares, Risk Intelligence Engine, tarification |
| `entreprises.html` | Page dédiée aux équipes TI internes et PME (non-MSP) |
| `clarification-copilot-vs-it-os.html` | Clarification sécurité : MSP OS vs Copilot Graph |
| `it-intelligence-os.html` | Brouillon autonome — non indexé, non relié au site |
| `pages/msp-demos.html` | Index des 20 casepages |
| `pages/*.html` | Casepages : interventions réelles **anonymisées** |

> Le moteur métier (38 agents) est dans `eriqallain-afk/IT`. Ce dépôt **présente** le produit.

---

## 4. STRUCTURE D'UNE CASEPAGE

Page HTML autonome : en-tête (titre/contexte/sévérité), corps symptôme → diagnostic → résolution → preuve, **toujours anonymisée** (voir §5).

---

## 5. RÈGLES ABSOLUES

### Anonymisation (règle n°1, non négociable)
Aucun motif de billet réel : `17xxxxx`, `#17xxxxx`, `T17xxxxx`, `Billet #17xxxxx`, `Ticket #17xxxxx`, `Service Ticket #17xxxxx`.
→ Exécuter le scan après toute extraction/ajout — **0 occurrence** attendue :
   `python scripts/scan_anonymisation.py` (portable, = celui de la CI) ou `scan-anonymisation.ps1` (local Windows).
→ Un **gate CI bloquant** (`.github/workflows/anonymisation.yml`) le rejoue sur chaque push/PR vers `main`.
→ Aucun nom client, IP, hostname ou donnée identifiante.

### Poids des images (budget 500 Ko)
Pour éviter d'alourdir le site, un **garde-fou de poids** (`scripts/check_image_weight.py`, gate `image-weight`) échoue sur toute **nouvelle** image > 500 Ko. Les images actuelles trop lourdes sont *grandfathered* (`scripts/image_weight_allowlist.txt`) et ne doivent que **rétrécir** — alléger en local (WebP/Squoosh) puis retirer de l'allowlist. Le garde-fou **ne modifie aucune image**.

### Cohérence avec le produit IT (source de vérité)

Les compteurs affichés sur les pages publiques proviennent de `IT/FACTORY_MANIFEST_IT.yaml`.
Valeurs en vigueur : **38 agents · 97 runbooks actifs · 94 templates · 46 scripts · 29 playbooks actifs · 20 casepages**.
Formulation retenue : chiffre exact dans les tuiles de métriques, formulation arrondie
(« près de 100 runbooks », « 90+ templates », « 45+ scripts ») dans la prose et les bandeaux,
pour éviter une retouche du site à chaque ajout côté IT.

> Tout changement du compteur d'agents côté IT (activation, archivage) doit être répercuté ici
> **et** dans le `README.md` — sinon le site annonce un périmètre qui n'existe pas.

### Tarification affichée

Grille de relancement (CAD, avant taxes), décidée par EA le 2026-09-15 :

| Version | Prix affiché |
|---|---|
| Starter | 219 $/mois |
| Pro | 499 $/mois |
| MSP | 749 $/mois |
| Enterprise | 995 $/mois |
| Implantation | 345 $ (frais unique) |
| Remise annuelle | −15 % |

Prix d'appel affiché sur `index.html` et `entreprises.html` : « à partir de 219 $ ».
La grille canonique est **celle du site** tant que `IT/00_DOCS/DOCUMENTATION_PRODUIT_MSP_Intelligence_AI.md`
et `IT/00_DOCS/MATRICE_COUT_MSP_Intelligence_IT_V1.md` n'ont pas été resynchronisés (voir `[DOC_SYNC]` du rapport de sync).

### Avant toute mise en ligne
1. Lancer le scan d'anonymisation (0 occurrence)
2. Vérifier le rendu local (`index.html` + casepages)
3. Ne jamais repartir d'une ancienne branche EA\|IA — partir de la source propre de ce repo

### Conventions
- Casepages : `eaia_case_{sujet}.html` ou `msp-case-{sujet}.html`
- `.nojekyll` doit rester présent
- Le `.zip` est un artefact d'archive — ne pas le servir comme page

### Git
- **Branche de développement : `claude/{description-courte}`** (branche courante : `claude/relaxed-keller-ed7c9c`)
- Jamais de push direct sur `main` sans PR + validation EA

---

## 6. DÉPLOIEMENT — GitHub Pages

Site statique servi par GitHub Pages (`.nojekyll` actif).

```
Settings → Pages → Source : branche publiée / racine (ou /docs)
```

Vérifier dans les Settings quelle source est active. Ce dépôt dispose de **deux** workflows GitHub Actions bloquants : le gate d'anonymisation (`.github/workflows/anonymisation.yml`) et le garde-fou de poids des images (`.github/workflows/image-weight.yml`). Les workflows de normalisation de `MSP_OS_ENGINE` (`normalize-casepage-headers`, `update-contact-email`) ne sont pas (encore) portés ici.

---

## 7. MSP_OS_ENGINE — repo non canonique

`MSP_OS_ENGINE` est le jumeau historique, non canonique. Ce repo-ci est la référence.
Les workflows `normalize-casepage-headers` et `update-contact-email` de l'autre repo peuvent être portés ici si nécessaire — mais l'initiative appartient à ce dépôt, pas à l'autre.

---

## 8. QUALITÉ ATTENDUE

- **0 donnée identifiante** — l'anonymisation prime sur tout
- Pages directement publiables — pas de placeholder, pas de lien mort
- Cohérence visuelle avec la charte EA\|IA (or `#EDAF45`, fond noir)
- Casepages : preuve > promesse

---

*CLAUDE.md v1.1 — MSP OS Engine Launch Site — Mis à jour le 2026-09-15*
*v1.1 : révision du contenu des pages de lancement — compteurs resynchronisés sur le manifest IT (24 → 38 agents), nouvelle grille tarifaire de relancement (219/499/749/995 $), MODULE_RISK_ENGINE présenté comme actif en production, ajout d'IT-CoachTECH, inventaire réel des pages (entreprises.html, clarification), 2 gates CI documentés.*
*Format dérivé de : Factory/90_KNOWLEDGE/BUNDLE_PACK__TEAM_TEMPLATE/TEMPLATE__CLAUDE_MD.md v1.0 (adapté site statique)*
