# MSP_OS_ENG_LAUNCH_SITE — site de lancement MSP (canonique)

Site statique de lancement du produit **MSP Intelligence OS / MSP Intelligence AI**
(moteur métier : repo `eriqallain-afk/IT`). Ce dépôt est le **site MSP canonique**
(acté EA 2026-06-21) ; `eriqallain-afk/MSP_OS_ENGINE` est le jumeau historique à ne plus maintenir.

## Contenu

| Fichier | Rôle |
|---|---|
| `index.html` | Landing de lancement — MSP Intelligence OS |
| `msp-preview.html` | Page produit MSP : modules, agents phares, Risk Engine, tarification |
| `entreprises.html` | Page dédiée aux équipes TI internes et PME (non-MSP) |
| `clarification-copilot-vs-it-os.html` | Clarification sécurité : MSP OS vs Copilot Graph |
| `it-intelligence-os.html` | Brouillon autonome, non indexé et non relié au site |
| `pages/msp-demos.html` | Index des casepages |
| `pages/*.html` | 20 casepages anonymisées (interventions réelles) |
| `assets/images/`, `img/`, `og-image*.png` | Visuels et Open Graph |

## Chiffres affichés — source de vérité

Les compteurs des pages publiques reflètent `IT/FACTORY_MANIFEST_IT.yaml` :
**38 agents · 97 runbooks actifs · 94 templates · 46 scripts · 29 playbooks actifs**.
Toute mise à jour du manifest IT doit être répercutée ici (voir `CLAUDE.md` §5).

## Tarification affichée

Grille de relancement (CAD, avant taxes) : **Starter 219 $ · Pro 499 $ · MSP 749 $ ·
Enterprise 995 $ par mois**, implantation 345 $ (frais unique), remise annuelle −15 %.
Prix d'appel affiché sur `index.html` et `entreprises.html` : « à partir de 219 $ ».

## Gates CI (bloquants)

| Workflow | Contrôle |
|---|---|
| `.github/workflows/anonymisation.yml` | 0 donnée identifiante, 0 billet réel |
| `.github/workflows/image-weight.yml` | Budget 500 Ko par nouvelle image |

À exécuter en local avant tout push :

```bash
python scripts/scan_anonymisation.py     # doit afficher 0 occurrence
python scripts/check_image_weight.py
```

Sur Windows, `scan-anonymisation.ps1` fait l'équivalent du premier.

## Règles

- **Anonymisation = règle n°1** : aucun nom client, IP, hostname ou billet réel.
- Ne jamais repartir d'une ancienne branche EA|IA — partir de la source propre de ce repo.
- Jamais de push direct sur `main` : PR + validation EA.
- `.nojekyll` doit rester présent (GitHub Pages sert le HTML brut).
