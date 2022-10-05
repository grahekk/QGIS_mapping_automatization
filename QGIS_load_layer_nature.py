import os
from qgis.core import (QgsVectorLayer)
from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
import processing

path_osnovni = "\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\PRIRODA"
path_POVS = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:3765' typename='dzzpnpis:direktiva_o_stanistima_natura2000_hr_2019_' url='http://services.bioportal.hr/wms' version='auto'"
path_POVS_stil = "\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\PRIRODA\\01_EM\\POVS.qml"
path_POP = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:3765' typename='dzzpnpis:direktiva_o_pticama_natura2000_hr_2019_' url='http://services.bioportal.hr/wms' version='auto'"
path_POP_stil = "\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\PRIRODA\\01_EM\\POP.qml"

path_ks = path_osnovni + "\\02_KS\\A - Poligoni\\Kopno-sve"
path_ks_2004 = path_ks + "\\KS_2004_fix.shp"
path_ks_2016 = "\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\PRIRODA\\02_KS\\A - Poligoni\\Kopno-sve\\KS_POLIGONI_2016\\SVE\\Poligoni_fix.shp"
path_ZPP_poligoni = path_osnovni + "\\03_ZP\\zasticena_podrucja.shp"
path_ZP_tocke = path_osnovni + "\\03_ZP\\NOVO\\zasticena_podrucja_tocke.shp"
path_MAB = path_osnovni + "\\04_MAB\\MAB.shp"

zahvat = iface.activeLayer()

# EM Natura 2000
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