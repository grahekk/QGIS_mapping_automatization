import os
from qgis.core import (QgsVectorLayer)
from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
import processing

path_POVS = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:3765' typename='dzzpnpis:direktiva_o_stanistima_natura2000_hr_2019_' url='http://services.bioportal.hr/wms' version='auto'"
path_POVS_stil = os.getcwd() + "\GitHub\QGIS_mapping_automatization\styles_layouts\POVS.qml"
path_POP = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:3765' typename='dzzpnpis:direktiva_o_pticama_natura2000_hr_2019_' url='http://services.bioportal.hr/wms' version='auto'"
path_POP_stil = os.getcwd() + "\GitHub\QGIS_mapping_automatization\styles_layouts\POP.qml"
path_ks_2004 = r"pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:3765' typename='dzzpnpis:kopnena_stanista' url='http://services.bioportal.hr/wms' version='auto'"
path_ks_2016_stil = os.getcwd() + "\GitHub\QGIS_mapping_automatization\styles_layouts\Habitats_styles_ks_2016.qml"
path_ks_2016 = r"pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:3765' typename='dzzpnpis:kopnena_stanista_2016' url='http://services.bioportal.hr/wms' version='auto'"
path_ks_2004_stil = os.getcwd() + "\GitHub\QGIS_mapping_automatization\styles_layouts\Habitats_styles_ks_2004.qml"
path_ZPP_polygons = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:3765' typename='dzzpnpis:zasticeno_podrucje_poligoni' url='http://services.bioportal.hr/wms' version='auto'"
path_ZPP_stil = os.getcwd() + "\GitHub\QGIS_mapping_automatization\styles_layouts\ZPP.qml"
path_ZPP_points = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:3765' typename='dzzpnpis:zasticeno_podrucje_tocke' url='http://services.bioportal.hr/wms' version='auto'"
path_ZPP_point_stil = os.getcwd() + "\GitHub\QGIS_mapping_automatization\styles_layouts\ZPP_point.qml"
path_MaB = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:3765' typename='dzzpnpis:unesco_mab' url='http://services.bioportal.hr/wms' version='auto'"
path_MaB_stil = os.getcwd() + "\GitHub\QGIS_mapping_automatization\styles_layouts\MaB.qml"

#POVS
vlayer = QgsVectorLayer(path_POVS, "Područje očuvanja značajno za vrste i stanišne tipove (POVS)", "WFS")
vlayer.loadNamedStyle(path_POVS_stil)
QgsProject.instance().addMapLayer(vlayer)

#POP
vlayer = QgsVectorLayer(path_POP, "Područje očuvanja značajno za ptice (POP)", "WFS")
vlayer.loadNamedStyle(path_POP_stil)
QgsProject.instance().addMapLayer(vlayer)

# Kopnena stanista 2004
vlayer = QgsVectorLayer(path_ks_2004, "Kopnena stanista 2004", "WFS")
vlayer.loadNamedStyle(path_ks_2004_stil)
QgsProject.instance().addMapLayer(vlayer)
    
# Kopnena stanista 2016
vlayer = QgsVectorLayer(path_ks_2016, "Kopnena stanista 2016", "WFS")
vlayer.loadNamedStyle(path_ks_2016_stil)
QgsProject.instance().addMapLayer(vlayer)

# Zasticena podrucja prirode poligoni
vlayer = QgsVectorLayer(path_ZPP_polygons, "zasticena podrucja prirode poligoni", "WFS")
vlayer.loadNamedStyle(path_ZPP_stil)
QgsProject.instance().addMapLayer(vlayer)

# Zasticena podrucja tocke
vlayer = QgsVectorLayer(path_ZPP_points, "zasticena podrucja tocke", "WFS")
vlayer.loadNamedStyle(path_ZPP_point_stil)
QgsProject.instance().addMapLayer(vlayer)
    
# MAB
vlayer = QgsVectorLayer(path_MaB, "Prekogranični rezervat biosfere", "WFS")
vlayer.loadNamedStyle(path_MaB_stil)
QgsProject.instance().addMapLayer(vlayer)

print("Nature layers loaded!")
