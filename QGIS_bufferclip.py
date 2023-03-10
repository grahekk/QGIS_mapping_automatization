from PyQt5.QtCore import QVariant
from qgis.core import (QgsVectorLayer)
from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
import processing

map_year = "2016"
export_as_excel_shp = True
buffer_dist = 50

zahvat = iface.activeLayer()
path_ks_2004 = r"\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\PRIRODA\\02_KS\\A - Poligoni\\Kopno-sve\\KS_2004_fix.shp"
path_ks_2016 = r"\\server.intranet.dvokut-ecro.hr\Pomoc\24 GIS\PRIRODA\02_KS\A - Poligoni\Kopno-sve\KS_POLIGONI_2016\SVE\Poligoni_fix.shp"

if map_year == "2016":
    path = path_ks_2016
if map_year == "2004":
    path = path_ks_2004

# KS buffer clip
vlayer = QgsVectorLayer(path, "Kopnena stanista ", "ogr")
QgsProject.instance().addMapLayer(vlayer)

# Buffer
alg_params = {
    'DISSOLVE': True,
    'DISTANCE': buffer_dist,
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
if map_year == "2016":
    clip.loadNamedStyle('\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\PRIRODA\\02_KS\\A - Poligoni\\Kopno-sve\\KS_POLIGONI_2016\\QGis_symbology\\Poligoni_sluzbena.qml')

name = "Karta staništa " + map_year
clip.setName(name)
QgsProject.instance().addMapLayer(clip)

#adding area field
provider = clip.dataProvider()
area_field = QgsField("Area", QVariant.Double)
provider.addAttributes([area_field])
#also, deleting the unnecessarry field
if map_year == "2016":
    clip.dataProvider().deleteAttributes([18])
clip.updateFields()

#calculating area
idx = provider.fieldNameIndex('Area')
for feature in clip.getFeatures():
    attrs = {idx : round(feature.geometry().area()/10000,3)}
    clip.dataProvider().changeAttributeValues({feature.id() : attrs})
    
path = QgsProject.instance().readPath("./")
path = path + '/' + clip.name()

if export_as_excel_shp == True:
    #export as excel table
    QgsVectorFileWriter.writeAsVectorFormat(clip, path + '.xlsx', "utf-8", driverName='xlsx')
    #export as shp
    QgsVectorFileWriter.writeAsVectorFormat(clip, path, "utf-8", driverName='shp')

QgsProject.instance().removeMapLayer(vlayer)
QgsProject.instance().removeMapLayer(bafer)

print("buffer-clipped!")