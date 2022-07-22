import os
from qgis.core import (QgsVectorLayer)
from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
import processing

zahvat = iface.activeLayer()
path_ks_2016 = "\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\PRIRODA\\02_KS\\A - Poligoni\\Kopno-sve\\KS_POLIGONI_2016\\SVE\\Poligoni_fix.shp"

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
QgsProject.instance().addMapLayer(bafer)

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