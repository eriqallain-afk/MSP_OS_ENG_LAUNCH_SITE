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

MSP OS Engine — Launch Site est le **site de lancement** dédié au produit **MSP Intelligence IT**. Comme `MSP_OS_ENGINE`, il ne contient **pas d'agents IA** (ceux-ci vivent dans le repo `IT`) : il rassemble landing, page produit et casepages anonymisées pour la campagne de lancement.

> ✅ **Ce dépôt est le site MSP canonique** (acté EA 2026-06-21). `eriqallain-afk/MSP_OS_ENGINE` est le jumeau historique non canonique — tout développement futur se fait ici.

---

## 2. STRUCTURE DU REPO

```
MSP_OS_ENG_LAUNCH_SITE/
├── CLAUDE.md                    ← Ce fichier
├── README.md                    ← Origine, règle d'anonymisation, déploiement
├── index.html                   ← Landing de lancement
├── it-intelligence-os.html      ← Page produit IT Intelligence OS
├── msp-preview.html             ← Alias produit MSP
├── .nojekyll                    ← Désactive Jekyll (HTML brut)
├── pages/                       ← 21 casepages MSP extraites et anonymisées
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
| `it-intelligence-os.html` | Page dédiée « IT Intelligence OS » |
| `msp-preview.html` | Page preview/alias du produit |
| `pages/msp-demos.html` | Index des 21 casepages |
| `pages/*.html` | Casepages : interventions réelles **anonymisées** |

> Le moteur métier (33 agents) est dans `eriqallain-afk/IT`. Ce dépôt **présente** le produit.

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

### Avant toute mise en ligne
1. Lancer le scan d'anonymisation (0 occurrence)
2. Vérifier le rendu local (`index.html` + casepages)
3. Ne jamais repartir d'une ancienne branche EA\|IA — partir de la source propre de ce repo

### Conventions
- Casepages : `eaia_case_{sujet}.html` ou `msp-case-{sujet}.html`
- `.nojekyll` doit rester présent
- Le `.zip` est un artefact d'archive — ne pas le servir comme page

### Git
- **Branche de développement : `claude/keen-curie-OIgRs`**
- Jamais de push direct sur `main` sans PR + validation EA

---

## 6. DÉPLOIEMENT — GitHub Pages

Site statique servi par GitHub Pages (`.nojekyll` actif).

```
Settings → Pages → Source : branche publiée / racine (ou /docs)
```

Vérifier dans les Settings quelle source est active. Ce dépôt dispose désormais d'**un** workflow GitHub Actions : le gate d'anonymisation (`.github/workflows/anonymisation.yml`). Les workflows de normalisation de `MSP_OS_ENGINE` (`normalize-casepage-headers`, `update-contact-email`) ne sont pas (encore) portés ici.

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

*CLAUDE.md v1.0 — MSP OS Engine Launch Site — Mis à jour le 2026-06-01*
*Format dérivé de : Factory/90_KNOWLEDGE/BUNDLE_PACK__TEAM_TEMPLATE/TEMPLATE__CLAUDE_MD.md v1.0 (adapté site statique)*
