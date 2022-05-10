from qgis.core import *

# path to qgis
QgsApplication.setPrefixPath('C:\\Program Files\\QGIS 3.16\\bin', True)
# disable gui
qgs = QgsApplication([], False)
# start
qgs.initQgis()

import 'SP_mapping-qgis.py'

# stop
qgs.exitQgis()