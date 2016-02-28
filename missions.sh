rm -f missions.txt
mkdir -p kml
mkdir -p gml
for ymin in `seq 42 2 50`; do
  ymax=`echo "$ymin+2"|bc`
  for xmin in `seq -5 2 7`; do
    xmax=`echo "$xmin+2"|bc`
    url="http://wxs.ign.fr/search/layers?request=GetFeature&version=1.1.0&typeName=ign:missions&CQL_FILTER=demat_layer_id%20like%20%27%25DEMAT.PVA\$GEOPORTAIL:DEMAT;PHOTOS%25%27%20and%20BBOX(the_geom,$ymin,$xmin,$ymax,$xmax)"
    echo $url
    curl "$url" -H 'Host: wxs.ign.fr' --compressed > temp
    python missions.py temp >> missions.txt
  done
done


