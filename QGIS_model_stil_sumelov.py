"""
Model exported as python.
Name : Davanje_stilova_sumelov
Group : 
With QGIS : 31600
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class Davanje_stilova_sumelov(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('Slojzahvata', 'Sloj zahvata', types=[QgsProcessing.TypeVectorLine,QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('LovistaNaPodrucjuZahvata', 'Lovista na podrucju zahvata', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(4, model_feedback)
        results = {}
        outputs = {}

        # Extract by location
        alg_params = {
            'INPUT': 'Lovista_50995c6f_534b_4291_af4f_e5a1abd720fe',
            'INTERSECT': parameters['Slojzahvata'],
            'PREDICATE': [0],
            'OUTPUT': parameters['LovistaNaPodrucjuZahvata']
        }
        outputs['ExtractByLocation'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['LovistaNaPodrucjuZahvata'] = outputs['ExtractByLocation']['OUTPUT']

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Set layer style - Drzavme sume
        alg_params = {
            'INPUT': 'Odsjeci_drzavnih_suma_5622c67c_be42_4d6a_8329_475437608045',
            'STYLE': '\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\SUME\\SUME-DRZAVNO\\odsjeci-drzavne.qml'
        }
        outputs['SetLayerStyleDrzavmeSume'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Lovista style
        alg_params = {
            'INPUT': outputs['ExtractByLocation']['OUTPUT'],
            'STYLE': '\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\LOV\\lovista.qml'
        }
        outputs['LovistaStyle'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Privatne sume stil
        alg_params = {
            'INPUT': 'WFS_Layer_d47d9604_ab8d_4572_a0c6_3c24b8dfe656',
            'STYLE': '\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\SUME\\SUME-PRIVATNO\\odsjeci_privatne_2017.qml'
        }
        outputs['PrivatneSumeStil'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results

    def name(self):
        return 'Davanje_stilova_sumelov'

    def displayName(self):
        return 'Davanje_stilova_sumelov'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Davanje_stilova_sumelov()
