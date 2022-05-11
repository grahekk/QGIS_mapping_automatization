from qgis.core import QgsProject
from qgis.gui import (
    QgsLayerTreeMapCanvasBridge,
)
# path to qgis
QgsApplication.setPrefixPath('C:\\Program Files\\QGIS 3.16\\bin', True)
# disable gui
qgs = QgsApplication([], False)
# start
qgs.initQgis()

project = QgsProject.instance()
bridge = QgsLayerTreeMapCanvasBridge( \
         QgsProject.instance().layerTreeRoot(), canvas)

project.write('my_new_qgis_project.qgs')

# stop
qgs.exitQgis()