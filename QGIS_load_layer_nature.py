import os
from qgis.core import (QgsVectorLayer)
from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
import processing
import pandas as pd

#paths = pd.read_csv()

#POVS
vlayer = QgsVectorLayer(path_POVS, "Područje očuvanja značajno za vrste i stanišne tipove (POVS)", "WFS")
vlayer.loadNamedStyle(path_POVS_stil)
QgsProject.instance().addMapLayer(vlayer)

#POP
vlayer = QgsVectorLayer(path_POP, "Područje očuvanja značajno za ptice (POP)", "WFS")
vlayer.loadNamedStyle(path_POP_stil)
QgsProject.instance().addMapLayer(vlayer)

# Kopnena stanista 2004
vlayer = QgsVectorLayer(path_ks_2004, "Kopnena stanista 2004", "ogr")
QgsProject.instance().addMapLayer(vlayer)
    
# Kopnena stanista 2016
vlayer = QgsVectorLayer(path_ks_2016, "Kopnena stanista 2016", "ogr")
vlayer.loadNamedStyle('\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\PRIRODA\\02_KS\\A - Poligoni\\Kopno-sve\\KS_POLIGONI_2016\\QGis_symbology\\Poligoni_sluzbena.qml')
QgsProject.instance().addMapLayer(vlayer)

# Zasticena podrucja prirode poligoni
vlayer = QgsVectorLayer(path_ZPP_poligoni, "zasticena podrucja prirode poligoni", "ogr")
QgsProject.instance().addMapLayer(vlayer)

# Zasticena podrucja tocke
vlayer = QgsVectorLayer(path_ZP_tocke, "zasticena podrucja tocke", "ogr")
QgsProject.instance().addMapLayer(vlayer)
    
# MAB
vlayer = QgsVectorLayer(path_MAB, "Prekogranični rezervat biosfere", "ogr")
QgsProject.instance().addMapLayer(vlayer)

print("Nature layers loaded!")
