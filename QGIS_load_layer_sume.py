import os
from qgis.core import (QgsVectorLayer)

path_osnovni = "\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\SUME\\SUME-DRZAVNO"
path_odsj_drz = path_osnovni + "\\odsjeci_drzavne.shp"
path_lovista = "\\\\server\\Pomoc\\24 GIS\\LOV\\NE_POSTOJI\\lovista_htrs.shp"

vlayer = QgsVectorLayer(path_odsj_drz, "Odsjeci drzavnih suma", "ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
vlayer = QgsVectorLayer(path_lovista, "Lovista", "ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
import urllib

params = {
    'service': 'WFS',
    'version': '2.0.0',
    'request': 'GetFeature',
    'typename': 'privsume:priv_ods',
    'srsname': "EPSG:3765"
}

uri = 'http://gis.hrsume.hr/privsume/wfs?layers=priv_gj'
uri2 = 'http://gis.hrsume.hr/privsume/wfs?layers=priv_gj' + urllib.parse.unquote(urllib.parse.urlencode(params))

layer = QgsVectorLayer(uri2, "WFS_Layer", "WFS")
if not layer.isValid():
    print ("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(layer)