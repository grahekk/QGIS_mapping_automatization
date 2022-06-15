import os
from qgis.core import (QgsVectorLayer)
from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
import processing

path_osnovni = "\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\PRIRODA"
path_POVS = path_osnovni + "\\01_EM\\POP.shp"
path_POP = path_osnovni + "\\01_EM\\POVS.shp"
path_ks = path_osnovni + "\\02_KS\\A - Poligoni\\Kopno-sve"
path_ks_2004 = path_ks + "\\Karta stanista RH 2004.shp"
path_ks_2016 = "\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\PRIRODA\\02_KS\\A - Poligoni\\Kopno-sve\\KS_POLIGONI_2016\\SVE\\Poligoni_fix.shp"

path_ZP_poligoni = path_osnovni + "\\03_ZP\\zasticena_podrucja.shp"
path_ZP_tocke = path_osnovni + "\\03_ZP\\NOVO\\zasticena_podrucja_tocke.shp"
path_MAB = path_osnovni + "\\04_MAB\\MAB.shp"

zahvat = iface.activeLayer()

# EM Natura 2000
#POVS
vlayer = QgsVectorLayer(path_POVS, "Područje očuvanja značajno za vrste i stanišne tipove (POVS)", "ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)

#POP
# Zasticena podrucja
vlayer = QgsVectorLayer(path_POP, "Područje očuvanja značajno za ptice (POP)", "ogr")
QgsProject.instance().addMapLayer(vlayer)

# Kopnena stanista 2004
vlayer = QgsVectorLayer(path_ks_2004, "Kopnena stanista 2004", "ogr")

QgsProject.instance().addMapLayer(vlayer)
    
# Kopnena stanista 2016
vlayer = QgsVectorLayer(path_ks_2016, "Kopnena stanista 2016", "ogr")
QgsProject.instance().addMapLayer(vlayer)

# KS buffer clip
vlayer = QgsVectorLayer(path_ks_2016, "Kopnena stanista 2016", "ogr")
# Buffer
alg_params = {
    'DISSOLVE': True,
    'DISTANCE': 100,
    'END_CAP_STYLE': 0,
    'INPUT': zahvat,
    'JOIN_STYLE': 0,
    'MITER_LIMIT': 2,
    'SEGMENTS': 5,
    'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
bafer = processing.run('native:buffer', alg_params)['OUTPUT']

# Clip
alg_params = {
    'INPUT': vlayer,
    'OVERLAY': bafer,
    'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
clip = processing.run('native:clip', alg_params)['OUTPUT']
clip.loadNamedStyle('\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\PRIRODA\\02_KS\\A - Poligoni\\Kopno-sve\\KS_POLIGONI_2016\\QGis_symbology\\Poligoni_sluzbena.qml')
clip.setName('Clip-buffer_KS')
QgsProject.instance().addMapLayer(clip)

# Zasticena podrucja poligoni
vlayer = QgsVectorLayer(path_ZP_poligoni, "zasticena podrucja poligoni", "ogr")
QgsProject.instance().addMapLayer(vlayer)

# Zasticena podrucja tocke
vlayer = QgsVectorLayer(path_ZP_tocke, "zasticena podrucja tocke", "ogr")
QgsProject.instance().addMapLayer(vlayer)
    
# MAB
vlayer = QgsVectorLayer(path_MAB, "Prekogranični rezervat biosfere", "ogr")
QgsProject.instance().addMapLayer(vlayer)