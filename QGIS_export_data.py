layers = QgsProject.instance().mapLayers().values()

for layer in layers:
    print(layer.name())
    
root = QgsProject.instance().layerTreeRoot()
mygroup = root.findGroup("Fauna")

print(mygroup)