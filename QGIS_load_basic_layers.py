import os
from qgis.core import QgsCoordinateReferenceSystem
from qgis.core import QgsProject
from qgis.core import QgsRasterLayer

#set the project scrs
my_crs=QgsCoordinateReferenceSystem(3765)
QgsProject.instance().setCrs(my_crs)

#DOF layer
urlWithParams = "contextualWMSLegend=0&crs=EPSG:3765&dpiMode=7&featureCount=10&format=image/png&layers=DOF&styles&url=http://geoportal.dgu.hr/wms?layers%3DDOF"
DOF = QgsRasterLayer(urlWithParams, 'DOF', 'wms')
QgsProject.instance().addMapLayer(DOF)

#HOK layer
urlWithParams = "contextualWMSLegend=0&crs=EPSG:3765&dpiMode=7&featureCount=10&format=image/png&layers=HOK&styles&url=http://geoportal.dgu.hr/wms?layers%3DDOF"
HOK = QgsRasterLayer(urlWithParams, 'HOK', 'wms')
QgsProject.instance().addMapLayer(HOK)

#TK25 layer
urlWithParams = "contextualWMSLegend=0&crs=EPSG:3765&dpiMode=7&featureCount=10&format=image/png&layers=TK25&styles&url=http://geoportal.dgu.hr/wms?layers%3DDOF"
TK25 = QgsRasterLayer(urlWithParams, 'TK25', 'wms')
QgsProject.instance().addMapLayer(TK25)