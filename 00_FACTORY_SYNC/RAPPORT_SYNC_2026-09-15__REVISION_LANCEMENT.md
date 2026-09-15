## Rapport de sync — MSP_OS_ENG_LAUNCH_SITE → Factory
**Date :** 2026-09-15 | **Version site :** CLAUDE.md v1.1 | **Branche :** `claude/relaxed-keller-ed7c9c`

> Ce dépôt est un **site vitrine** (aucun agent). La remontée porte sur l'alignement
> du discours public avec le produit IT et sur une décision tarifaire prise par EA.

### Nature du changement
Révision du contenu des pages publiques de lancement : resynchronisation des compteurs
sur le manifest IT, nouvelle grille tarifaire de relancement, et mise à niveau du statut
des modules produit.

### Nouveaux agents
- *(aucun — ce dépôt n'héberge pas d'agents)*

### Agents modifiés
- *(aucun)*

### Agents archivés
- *(aucun)*

### Contenu public modifié

| Élément | Avant (site) | Après (site) | Source |
|---|---|---|---|
| Agents affichés | 24 | 38 | `IT/FACTORY_MANIFEST_IT.yaml` → `stats.total_agents: 38` |
| Runbooks affichés | 123 / 163 / 168 (3 valeurs contradictoires) | 97 (tuiles) · « près de 100 » (prose) | `stats.total_runbooks: 97` |
| Templates affichés | 90 / 93 / 98 | 94 (tuiles) · « 90+ » (prose) | `stats.total_templates: 94` |
| Scripts affichés | 45 | 46 (tuiles) · « 45+ » (prose) | `stats.total_scripts: 46` |
| Playbooks affichés | 29 | 29 (inchangé, vérifié) | `stats.active_playbooks: 29` |
| MODULE_RISK_ENGINE | « module en validation — MSP pilotes » | actif en production, 5 agents nommés | activation EA 2026-06-25 |
| IT-CoachTECH | absent du site | 3ᵉ agent phare sur `msp-preview.html` | activation EA 2026-06-26 |
| Modules produit | 8 | 9 (ajout « Risk Intelligence ») | — |

### Tarification — décision EA du 2026-09-15

Relancement à la baisse (CAD, avant taxes) :

| Version | Ancien prix site | Nouveau prix site |
|---|---|---|
| Starter | 295 $/mois | **219 $/mois** |
| Pro | 695 $/mois | **499 $/mois** |
| MSP | 995 $/mois | **749 $/mois** |
| Enterprise | 1 295 $/mois | **995 $/mois** |
| Implantation (unique) | 445 $ | **345 $** |
| Remise annuelle | −15 % | −15 % (inchangée) |

Le prix d'appel affiché sur `index.html` et `entreprises.html` passe de **349 $** à **219 $**
(il était incohérent avec le palier Starter du site, qui était à 295 $).

### Divergence à arbitrer côté produit IT

Trois grilles tarifaires coexistaient dans l'écosystème avant cette révision :

| Source | Starter | Pro | MSP | Enterprise |
|---|---|---|---|---|
| Site (avant) | 295 $ | 695 $ | 995 $ | 1 295 $ |
| `IT/00_DOCS/DOCUMENTATION_PRODUIT_MSP_Intelligence_AI.md` §8 | 249 $ | 549 $ | 999 $ | 1 799 $ |
| `IT/00_DOCS/MATRICE_COUT_MSP_Intelligence_IT_V1.md` §A1 | 249 $ | 549 $ | 999 $ | 1 799 $ |
| **Site (après cette révision)** | **219 $** | **499 $** | **749 $** | **995 $** |

Le site fait désormais foi pour le prix public. Les deux documents IT restent à resynchroniser
(y compris les prix annuels 2 540 / 5 600 / 10 190 / 18 350 $ et les calculs de ROI et de marge
qui en découlent). **Aucune modification n'a été appliquée au repo IT** — décision EA requise.

### Actions requises côté Factory
- [ ] Prendre acte de la nouvelle grille tarifaire publique (219 / 499 / 749 / 995 $).
- [ ] Arbitrer la resynchronisation des documents tarifaires du produit IT (voir `next_actions`).
- [ ] Vérifier que les autres supports de lancement (github.io, EAIA) n'affichent pas l'ancienne grille ni l'ancien compteur d'agents.

### next_actions
```yaml
next_actions:
  - "[DOC_SYNC] IT — resynchroniser §8 Niveaux de service de DOCUMENTATION_PRODUIT_MSP_Intelligence_AI.md sur la grille 219/499/749/995 $ (mensuel + annuel)"
  - "[DOC_SYNC] IT — resynchroniser §A1 de MATRICE_COUT_MSP_Intelligence_IT_V1.md, ainsi que les marges (§ coût réel/marge) et le ROI Pro qui citent 549 $/mois"
  - "[DOC_SYNC] IT — la documentation produit annonce 33 agents et 120 runbooks ; le manifest en compte 38 et 97. Aligner le document sur le manifest."
  - "[DOC_SYNC] Site — les repères marché d'entreprises.html (80 000 $/an pour un spécialiste, 3 000 $+/mois pour un MSP externe) ne sont pas sourcés ; à valider ou à sourcer par EA."
  - "[SYNC_FACTORY] Soumettre ce rapport à EA pour validation avant mise à jour de l'index produits de la Factory"
```

**Validation EA requise avant exécution côté Factory.**
