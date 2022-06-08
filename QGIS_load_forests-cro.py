import os
from qgis.core import QgsVectorLayer
from qgis.core import QgsProcessingAlgorithm
import processing

path_osnovni = "\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\SUME\\SUME-DRZAVNO"
path_drz_odsj = path_osnovni + "\\odsjeci_drzavne.shp"
path_drz_gj = path_osnovni + "\\gj.shp"
path_drz_sumarija = path_osnovni + "\\sumarije.shp"
path_priv_gj = "\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\SUME\\SUME-PRIVATNO\\granice_gj_2017.shp"
path_lovista = "\\\\server\\Pomoc\\24 GIS\\LOV\\NE_POSTOJI\\lovista_htrs.shp"

zahvat = iface.activeLayer()

# odsjeci
vlayer = QgsVectorLayer(path_drz_odsj, "Odsjeci drzavnih suma", "ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
vlayer.loadNamedStyle('\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\SUME\\SUME-DRZAVNO\\odsjeci-drzavne.qml')

# lovista
vlayer = QgsVectorLayer(path_lovista, "Lovista", "ogr")
alg_params = {
            'INPUT': vlayer,
            'INTERSECT': zahvat,
            'PREDICATE': [0],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }

lovista = processing.run('native:extractbylocation', alg_params)['OUTPUT']
lovista.setName('Lovista zahvat')
lovista.loadNamedStyle('\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\LOV\\lovista.qml')
QgsProject.instance().addMapLayer(lovista)

# GJ drz
vlayer = QgsVectorLayer(path_drz_gj, "GJ_drz", "ogr")
alg_params = {
            'INPUT': vlayer,
            'INTERSECT': zahvat,
            'PREDICATE': [0],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }

gj_drz = processing.run('native:extractbylocation', alg_params)['OUTPUT']
gj_drz.setName('GJ drzavna')
gj_drz.loadNamedStyle('\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\SUME\\SUME-DRZAVNO\\gj.qml')
QgsProject.instance().addMapLayer(gj_drz)
    
# sumarija
vlayer = QgsVectorLayer(path_drz_sumarija, "Sumarije", "ogr")
alg_params = {
            'INPUT': vlayer,
            'INTERSECT': zahvat,
            'PREDICATE': [0],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }

sumarije = processing.run('native:extractbylocation', alg_params)['OUTPUT']
sumarije.setName('Sumarije na podrucju zahvata')
sumarije.loadNamedStyle('\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\SUME\\SUME-DRZAVNO\\sumarije.qml')
QgsProject.instance().addMapLayer(sumarije)

#GJ priv
vlayer = QgsVectorLayer(path_priv_gj, "GJ_priv", "ogr")
alg_params = {
            'INPUT': vlayer,
            'INTERSECT': zahvat,
            'PREDICATE': [0],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }

gj_priv_zahvat = processing.run('native:extractbylocation', alg_params)['OUTPUT']
gj_priv_zahvat.loadNamedStyle('\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\SUME\\SUME-PRIVATNO\\granice_gj_2017.qml')
gj_priv_zahvat.setName('GJ priv zahvat')
QgsProject.instance().addMapLayer(gj_priv_zahvat)

#wfs privatne
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

layer = QgsVectorLayer(uri2, "WFS_Layer - Odsjeci privatnih suma", "WFS")
QgsProject.instance().addMapLayer(layer)
layer.loadNamedStyle('\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\SUME\\SUME-PRIVATNO\\odsjeci_privatne_2017.qml')
