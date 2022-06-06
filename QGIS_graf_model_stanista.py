"""
Model exported as python.
Name : Staniste_bafer_klip
Group : 
With QGIS : 31600
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class Staniste_bafer_klip(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('staniste', 'zahvat', types=[QgsProcessing.TypeVectorLine,QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('FinalniRezultat', 'Finalni rezultat', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(3, model_feedback)
        results = {}
        outputs = {}

        # Fix geometries
        alg_params = {
            'INPUT': 'dzzpnpis_kopnena_stanista_2016_62e245f0_3911_42b3_ad28_50e548f6a24b',
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['FixGeometries'] = processing.run('native:fixgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Buffer
        alg_params = {
            'DISSOLVE': False,
            'DISTANCE': 100,
            'END_CAP_STYLE': 0,
            'INPUT': parameters['staniste'],
            'JOIN_STYLE': 0,
            'MITER_LIMIT': 2,
            'SEGMENTS': 5,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Buffer'] = processing.run('native:buffer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Clip
        alg_params = {
            'INPUT': outputs['FixGeometries']['OUTPUT'],
            'OVERLAY': outputs['Buffer']['OUTPUT'],
            'OUTPUT': parameters['FinalniRezultat']
        }
        outputs['Clip'] = processing.run('native:clip', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['FinalniRezultat'] = outputs['Clip']['OUTPUT']
        return results

    def name(self):
        return 'Staniste_bafer_klip'

    def displayName(self):
        return 'Staniste_bafer_klip'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Staniste_bafer_klip()
