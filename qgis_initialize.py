#Step 2: Init QGIS libraries in Python Script before using its Algorithms
import os
import sys
import json
import pandas as pd

# set up system paths
qspath = './qgis_sys_paths.csv' 
# provide the path where you saved this file.
paths = pd.read_csv(qspath).paths.tolist()
sys.path += paths
# set up environment variables
qepath = './qgis_env.json'
js = json.loads(open(qepath, 'r').read())
for k, v in js.items():
    os.environ[k] = v

# qgis library imports
import PyQt5.QtCore
import qgis.PyQt.QtCore
from qgis.core import *
from qgis.analysis import QgsNativeAlgorithms

feedback = QgsProcessingFeedback()
# initializing processing module
QgsApplication.setPrefixPath(js['HOME'], True)
qgs = QgsApplication([], False)
qgs.initQgis() # use qgs.exitQgis() to exit the processing module at the end of the script.
# initialize processing algorithms
from processing.core.Processing import Processing
Processing.initialize()
import processing
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

print("imported")

#which algs do I have?
algs = dict()
for alg in QgsApplication.processingRegistry().algorithms():
    algs[alg.displayName()] = alg.id()
#print(algs)


#from qgis.core import *

# path to qgis
#QgsApplication.setPrefixPath('C:\\Program Files\\QGIS 3.16\\bin', True)
# disable gui
#qgs = QgsApplication([], False)
# start

from qgis.gui import (
    QgsLayerTreeMapCanvasBridge,
)
from qgis.core import QgsProject
project = QgsProject.instance()
project.write('my_new_qgis_project.qgs')

import runpy
#runpy.run_path("QGIS_load_basic_layers.py")

from qgis.core import QgsCoordinateReferenceSystem

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

from QGIS_load_basic_layers import *
from qgis.core import QgsRasterLayer
load_basic_layers()
from QGIS_export_map import *
map_exporter("DOF","DOF")

import re
from qgis.PyQt.QtXml import QDomDocument


# stop
qgs.exitQgis()