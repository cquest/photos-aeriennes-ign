from bs4 import BeautifulSoup
import shapely
from shapely.wkt import dumps, loads

import sys
import json


x = BeautifulSoup(open('temp'),'lxml')
for i in x.find_all('placemark'):
  j = dict(mission=sys.argv[1].replace('.kml',''))
  j.update(id=i.find(id='id').value.string)
  j.update(name=i.find(id='name').value.string)
  j.update(numcli=i.find(id='NUMCLI').value.string)
  j.update(idcliche=i.find(id='IDCLICHE').value.string)
  j.update(res=i.find(id='RES').value.string.strip())
  if i.find(id='ORIENTATION') is not None:
    j.update(orientation=i.find(id='ORIENTATION').value.string)
  j.update(date=i.find(id='DATE').value.string.replace('/','-'))
  j.update(idta=i.find(id='IDTA').value.string)
  j.update(support=i.find(id='SUPPORT').value.string)
  if i.coordinates is not None:
    geo = 'POLYGON(('+i.coordinates.string.replace(',','!').replace(' ',',').replace('!',' ')+'))'
    j.update(wkt=geo)
    centroid = shapely.wkt.loads(geo).centroid
    j.update(lat=round(centroid.y,7))
    j.update(lon=round(centroid.x,7))
  if i.find(id='JP2').value.string is not None:
    j.update(url=i.find(id='JP2').value.string+'.jp2')
    print(json.dumps(j))

