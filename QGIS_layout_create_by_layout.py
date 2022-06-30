project = QgsProject.instance()         
manager = project.layoutManager() 
layouts_list = manager.printLayouts()
layer = iface.activeLayer()
manager.clear() #- remove all layouts

#for i, f in zip(popis_layouta, layer.getFeatures()):
for i, f in enumerate(layer.getFeatures()): 
    ime = "layout"+str(i)
    layout = QgsPrintLayout(project)        
    layoutName = ime

    layout.initializeDefaults()
    layout.setName(layoutName)
    manager.addLayout(layout)
    
    map = QgsLayoutItemMap(layout)
    map.setRect(20, 20, 20, 20)                                     
    
    geom = f.geometry()
    point = geom.asPoint()

    x_min = point.x()-50
    x_max = point.x()+50
    y_min = point.y()-50
    y_max = point.y()+50
    
    rectangle = QgsRectangle(x_min, y_min, x_max, y_max)
    map.setExtent(rectangle)
    layout.addLayoutItem(map)
    
    map.attemptMove(QgsLayoutPoint(5, 27, QgsUnitTypes.LayoutMillimeters))
    map.attemptResize(QgsLayoutSize(239, 178, QgsUnitTypes.LayoutMillimeters))
    
    checked_layers = [layer.name() for layer in QgsProject().instance().layerTreeRoot().children() if layer.isVisible()]
    layersToAdd = [layer for layer in QgsProject().instance().mapLayers().values() if layer.name() in checked_layers]
    
    root = QgsLayerTree()
    for layer in layersToAdd:
    #add layer objects to the layer tree
        root.addLayer(layer)
        
    legend = QgsLayoutItemLegend(layout)
    legend.model().setRootGroup(root)
    layout.addLayoutItem(legend)
    legend.attemptMove(QgsLayoutPoint(246, 5, QgsUnitTypes.LayoutMillimeters))
    
    north = QgsLayoutItemPicture(layout)
    north.setPicturePath(":/images/north_arrows/layout_default_north_arrow.svg")
    layout.addLayoutItem(north)
    north.attemptResize(QgsLayoutSize(15, 15, QgsUnitTypes.LayoutMillimeters))
    north.attemptMove(QgsLayoutPoint(5,7.638, QgsUnitTypes.LayoutMillimeters))
    
    scale_bar = QgsLayoutItemScaleBar(layout)
    layout.addLayoutItem(scale_bar)
    scale_bar.attemptResize(QgsLayoutSize(15, 15, QgsUnitTypes.LayoutMillimeters))
    scale_bar.attemptMove(QgsLayoutPoint(5,20, QgsUnitTypes.LayoutMillimeters))
    