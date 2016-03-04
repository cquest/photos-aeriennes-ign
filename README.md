# photos-aeriennes-ign

Ce projet contient des scripts d'extraction des données sur les photos aériennes anciennes disponibles sur le géoportail ainsi que les données extraites et remises en forme pour en faciliter la ré-utilisation.

**Les données sont directement disponibles dans le dossier data, voir la description ci-dessous.**
L'extraction des données a été réalisée début mars 2016 pour la métropole.
3.1 millions de clichés ont ainsi été répertoriés entre 1919 et 2011.

Ces images aériennes sont librement réutilisables (voir http://professionnels.ign.fr/pva) conformément à la loi n°78-753 du 17 juillet 1978, y compris pour des usages commerciaux.
Ces fichiers de métadonnées ont pour but de faciliter l'accès et la ré-utilisation de ce formidable patrimoine.

## Métadonnées des missions (dans /data/missions/)
- **mission**: identifiant de la mission
- **annee**: année extraite de l'idta des clichés
- **date_debut**: date de début (extrait des métadonnées des clichés)
- **date_fin**: date de fin (extrait des métadonnées des clichés)
- **res**: résolution des clichés de la mission (extrait de l'idta)
- **support**: Ag pour argentique, Nu pour numérique
- **type**: type de photo P=noir et blanc, C=couleur, IR=infrarouge, IRC=infrarouge couleur ? (extrait de l'idta)
- **nbcliches**: nombre de clichés pris pour cette mission
- **surface**: surface couvertue par la mission
- **somme_surface**: somme des surfaces des clichés (avec recouvrement)
- **tx_recouvrement**: taux de recouvrement des clichés
- la géométrie correspond à l'emprise globale des clichés de la mission

### Métadonnées des clichés (dans /data/pva/)
- **idcliche**: identifiant du cliché (unique)
- **mission:** identifiant de la mission
- **numcli**: numéro du cliché
- **idta**: composé de annee _ nom mission _ type de photo (type) _ numéro du cliché (numcli) 
- **date**: date de prise de vue (format ISO)... les dates au 1er janvier semble indiquer uniquement l'année
- **res**: résolution (en échelle pour les photos argentiques, en cm/pixel pour les numériques)
- **support**: Ag pour argentique, Nu pour numérique
- **type**: type de photo P=noir et blanc, C=couleur, IR=infrarouge, IRC=infrarouge couleur ?
- **surface**: couverture en km2 du cliché
- **lon**: longitude du centroide de l'emprise
- **lat**: latitude du centroide de l'emprise
- **orientation**: orientation en degrés du cliché
- **url**: nom du fichier JPEG2000 téléchargeable, peut être NULL si non téléchargeable
- le polygone de la géométrie contenu dans le geojson correspond à celle de la couverture du cliché

### Statistiques et data-visualisations

Un tableau permet de visualiser le nombre de clichés pris jour après jour: http://cquest.github.io/pva/pva_par_date.html
