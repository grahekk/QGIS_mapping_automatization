   
root = QgsProject.instance().layerTreeRoot()
path = QgsProject.instance().readPath("./") + '/data_export/'

group_list = ['Flora', 'Fauna', 'crvene knjige i popisi']

for i in group_list:
    print(i)
    mygroup = root.findGroup(i)
    layer_list= mygroup.findLayers()
    layer_list = [layer.name() for layer in mygroup.children()]
    print(layer_list)

    for vLayer in QgsProject.instance().mapLayers().values():
        if vLayer.name() in layer_list:
            #print(vLayer.name())
            QgsVectorFileWriter.writeAsVectorFormat( vLayer,  path+ vLayer.name() + ".csv", "utf-8", vLayer.crs(), driverName="CSV" )

print('data exported')