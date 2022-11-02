from PyQt5.QtCore import QVariant

zahvat = iface.activeLayer()
path_POVS = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:3765' typename='dzzpnpis:direktiva_o_stanistima_natura2000_hr_2019_' url='http://services.bioportal.hr/wms' version='auto'"
path_POP = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:3765' typename='dzzpnpis:direktiva_o_pticama_natura2000_hr_2019_' url='http://services.bioportal.hr/wms' version='auto'"

# KS buffer clip
vlayer = QgsVectorLayer(path_POVS, "POVS", "WFS")
QgsProject.instance().addMapLayer(vlayer)

# Buffer
alg_params = {
    'DISSOLVE': True,
    'DISTANCE': 5000,
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
clip.setName('Clip-buffer_EM')
QgsProject.instance().addMapLayer(clip)

#onda ide point along geometry x2
# Points along geometry
alg_params = {
    'DISTANCE': 10,
    'END_OFFSET': 0,
    'START_OFFSET': 0,
    'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
}
outputs['PointsAlongGeometry'] = processing.run('native:pointsalonglines', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
    
#onda distance matrix
alg_params = {
    'INPUT': 'Interpolated_points_e6fea0c5_ef5f_4c2d_b4d8_f5db7ad6dab0',
    'INPUT_FIELD': 'sitename',
    'MATRIX_TYPE': 0,
    'NEAREST_POINTS': 1,
    'TARGET': 'Interpolated_points_e9d45406_fa05_41ff_a749_a29f9aa8a464',
    'TARGET_FIELD': 'id',
    'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
}
outputs['DistanceMatrix'] = processing.run('qgis:distancematrix', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

#onda field calc minimum(min(Distance), InputID)

#onda unique

QgsProject.instance().removeMapLayer(vlayer)
QgsProject.instance().removeMapLayer(bafer)

print("done")