from bs4 import BeautifulSoup
import sys

x = BeautifulSoup(open(sys.argv[1]),'lxml')
for m in x.find_all('ign:missions'):
  print(m.find('ign:kml_layer_id').string)

