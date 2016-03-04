# photos-aeriennes-ign

Ce projet contient des scripts d'extraction des données sur les photos aériennes anciennes disponibles sur le géoportail.
L'extraction des données a été réalisée début mars 2016 pour la métropole. 3.1 millions de clichés ont été répertoriés.

Ils génèrent une liste des clichés disponibles au format geojson (un fichier par année) avec les métadonnées suivantes:
- idcliche: identifiant du cliché (unique)
- mission: identifiant de la mission
- numcli: numéro du cliché
- idta: composé de annee _ nom mission _ type de photo (type) _ numéro du cliché (numcli) 
- date: date de prise de vue (format ISO)... les dates au 1er janvier semble indiquer uniquement l'année
- res: résolution (en échelle pour les photos argentiques, en cm/pixel pour les numériques)
- support: Ag pour argentique, Nu pour numérique
- type: type de photo P=noir et blanc, C=couleur, IR=infrarouge, IRC=infrarouge couleur ?
- surface: couverture en km2 du cliché
- lon: longitude du centroide de l'emprise
- lat: latitude du centroide de l'emprise
- orientation: orientation en degrés du cliché
- url: nom du fichier JPEG2000 téléchargeable, peut être NULL si non téléchargeable

Ces images aériennes sont librement réutilisables (voir http://professionnels.ign.fr/pva) conformément à la loi n°78-753 du 17 juillet 1978, y compris pour des usages commerciaux.
