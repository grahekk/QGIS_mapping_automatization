project = QgsProject.instance()         
manager = project.layoutManager() 
layouts_list = manager.printLayouts()
layer = iface.activeLayer()
#manager.clear() #- remove all layouts

checked_layers = [layer.name() for layer in QgsProject().instance().layerTreeRoot().children() if layer.isVisible()]
layersToAdd = [layer for layer in QgsProject().instance().mapLayers().values() if layer.name() in checked_layers]

layout = QgsPrintLayout(project)        
layout.initializeDefaults()
layout.setName("Karta stanista automatik")
manager.addLayout(layout)

for i, f in enumerate(layer.getFeatures()): 
    if i>0:
        page = QgsLayoutItemPage(layout)
        page.setPageSize('A4', QgsLayoutItemPage.Orientation.Landscape)
        layout.pageCollection().addPage(page)
    
    map = QgsLayoutItemMap(layout)
    map.setRect(20, 20, 20, 20)
    
    geom = f.geometry()
    point = geom.asPoint()

    x_min = point.x()-1515
    x_max = point.x()+1515
    y_min = point.y()-802
    y_max = point.y()+802
    
    rectangle = QgsRectangle(x_min, y_min, x_max, y_max)
    map.setExtent(rectangle)
    layout.addLayoutItem(map)
    
    map.attemptMove(QgsLayoutPoint(0, 0, QgsUnitTypes.LayoutMillimeters), page = i)
    map.attemptResize(QgsLayoutSize(297, 210, QgsUnitTypes.LayoutMillimeters))
    
    root = QgsLayerTree()
    for layer in layersToAdd:
        root.addLayer(layer)
        
    
    north = QgsLayoutItemPicture(layout)
    north.setPicturePath("C:/Users/ngersak/Documents/sjever.png")
    layout.addLayoutItem(north)
    north.attemptResize(QgsLayoutSize(12, 12, QgsUnitTypes.LayoutMillimeters))
    north.attemptMove(QgsLayoutPoint(283.271,1, QgsUnitTypes.LayoutMillimeters), page = i)
    north.setLinkedMap(map)
    
    scale_bar = QgsLayoutItemScaleBar(layout)
    layout.addLayoutItem(scale_bar)
    scale_bar.attemptResize(QgsLayoutSize(114, 14, QgsUnitTypes.LayoutMillimeters))
    scale_bar.attemptMove(QgsLayoutPoint(0,196, QgsUnitTypes.LayoutMillimeters), page = i)
    scale_bar.setLinkedMap(map)
    scale_bar.setNumberOfSegments(4)
    text_format = QgsTextFormat()
    text_format.setFont(QFont("Calibri", 10))
    scale_bar.setTextFormat(text_format)
    scale_bar.setSegmentSizeMode(1)
    scale_bar.setBackgroundEnabled(True)
    scale_bar.setUnits(250)

print("done")
    