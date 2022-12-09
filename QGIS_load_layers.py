import os
from qgis.core import QgsVectorLayer
import pandas as pd

def load_layer(layer):
    #group = nature, forests, basic, all
    #layers = POVS, POP, ZPP, KS, MAB, private_forests, state forests, hunting grounds, DOF, HOK, TK
    #style = T,F

    path = 'C:\\Users\\ngersak\\Documents\\GitHub\\QGIS_mapping_automatization\\qgis_layer_paths.csv'
    df = pd.read_csv(path, encoding = "iso8859_16", index_col = "key")
    path = df.loc[layer, 'path']
    path_style = df.loc[layer, 'style_path']

    if layer == 'POVS':
        vlayer = QgsVectorLayer(path, "Područje očuvanja značajno za vrste i stanišne tipove (POVS)", "WFS")
        vlayer.loadNamedStyle(path_style)
        QgsProject.instance().addMapLayer(vlayer)

    if layer == 'POP':
        vlayer = QgsVectorLayer(path, "Područje očuvanja značajno za ptice (POP)", "WFS")
        vlayer.loadNamedStyle(path_style)
        QgsProject.instance().addMapLayer(vlayer)

    if layer == 'KS2004':
        vlayer = QgsVectorLayer(path, "Kopnena stanista 2004", "ogr")
        QgsProject.instance().addMapLayer(vlayer)

    if layer == 'KS2016':
        vlayer = QgsVectorLayer(path, "Kopnena stanista 2016", "ogr")
        vlayer.loadNamedStyle('\\\\server.intranet.dvokut-ecro.hr\\Pomoc\\24 GIS\\PRIRODA\\02_KS\\A - Poligoni\\Kopno-sve\\KS_POLIGONI_2016\\QGis_symbology\\Poligoni_sluzbena.qml')
        QgsProject.instance().addMapLayer(vlayer)

    if layer == 'ZPP':
        vlayer = QgsVectorLayer(path, "zasticena podrucja prirode poligoni", "ogr")
        QgsProject.instance().addMapLayer(vlayer)

    if layer == 'ZPP_point':
        vlayer = QgsVectorLayer(path, "zasticena podrucja tocke", "ogr")
        QgsProject.instance().addMapLayer(vlayer)

    if layer == 'MAB':
        vlayer = QgsVectorLayer(path, "Prekogranični rezervat biosfere", "ogr")
        QgsProject.instance().addMapLayer(vlayer)

    if layer == 'DOF':
        urlWithParams = "contextualWMSLegend=0&crs=EPSG:3765&dpiMode=7&featureCount=10&format=image/png&layers=DOF&styles&url=http://geoportal.dgu.hr/wms?layers%3DDOF"
        DOF = QgsRasterLayer(urlWithParams, 'DOF', 'wms')
        QgsProject.instance().addMapLayer(DOF)

    print("layers loaded!")
    return(layer)

load_layer("POVS")