import re
from qgis.PyQt.QtXml import QDomDocument

project = QgsProject.instance()         
manager = project.layoutManager()

def map_exporter(map_name, main_layer_name):

    #main_layer_name = "Međimurska županija"
    layer = QgsProject.instance().mapLayersByName(main_layer_name)[0]

    gui_use = True
    if gui_use == True:
        iface.setActiveLayer(layer)
        zahvat = iface.activeLayer()

    #command line arguments
    #map_name = 'KS'

    #define parameters - if
    if map_name == "KS":
        RECTSCALE = 1.1
        mapping_layer = ["Karta staništa 2016"]
        template_name = "KS"
    if map_name == "EM":
        RECTSCALE = 5
        mapping_layer = ["Područje očuvanja značajno za vrste i stanišne tipove (POVS)", "Područje očuvanja značajno za ptice (POP)"]
        template_name = "EM"
    if map_name == "ZPP":
        RECTSCALE = 5
        mapping_layer = ["zasticena podrucja prirode poligoni"]
        template_name = "ZPP"
    if map_name == "DOF":
        map_name = "EM"
        RECTSCALE = 1.2
        tempalte_name = "EM"
    if map_name == "Group":
        map_name = "Group"
        RECTSCALE = 1.2
        template_name = "EM"
        group_name = "Range 1x1"
        mapping_layer = [main_layer_name]


    to_remove = manager.layoutByName(map_name)
    manager.removeLayout(to_remove)

    layout = QgsPrintLayout(project)
    template_file = open('C:\\Users\\ngersak\\Documents\\GitHub\\QGIS_mapping_automatization\\' + template_name + '.qpt')
    template_content = template_file.read()
    template_file.close()
    document = QDomDocument()
    document.setContent(template_content)
    layout.loadFromTemplate(document, QgsReadWriteContext())
    layout.setName(map_name)
    manager.addLayout(layout)

    my_table = layout.items()

    map = my_table[3]
    rect = zahvat.extent()
    rect.scale(RECTSCALE)
    map.zoomToExtent(rect)

    scale = my_table[2]
    #set segment size to "fit the segment size"
    scale.setSegmentSizeMode(1)

    legend = my_table[0]
    root = legend.model().rootGroup()
    legendLyr = QgsProject.instance().mapLayersByName(main_layer_name)[0]
    root.addLayer(legendLyr)
    for i in mapping_layer:
        legendLyr = QgsProject.instance().mapLayersByName(i)[0]
        root.addLayer(legendLyr)

    if map_name == 'KS':
        layer_and_nodes = dict()
        m = legend.model()
        idx = m.index(1, 0)
        n = m.index2node(idx)
        nodes = m.layerLegendNodes(n)
        layer_and_nodes[n.name()] = nodes
        print("PRINT 2")

        label_old = ""
        nodes2 = []
        for i in nodes:
            label = i.symbolLabel()
            print(label)
            if "<" in label or ">" in label:
                i.setUserLabel(label_old)
                nodes2.append(i)
                print(i.symbolLabel())
                continue
            print(i.textOnSymbolLabel())
            label_old = label
            nodes2.append(i)
    
    legend.refresh()

    path = QgsProject.instance().readPath("./")
    path = path + '/'

    exporter = QgsLayoutExporter(layout)
    exporter.exportToImage(path + map_name + '.jpg', exporter.ImageExportSettings())

    print(map_name+" layout exported")

#map_exporter("KS", "Zahvat_relevantni")

#group export
root = QgsProject.instance().layerTreeRoot()
mygroup = root.findGroup("Range 1x1")
layer_list= mygroup.findLayers()
layer_list = [layer.name() for layer in mygroup.children()]
print(layer_list)

for i in layer_list:
    print(i)
    map_exporter("Group", i)