project = QgsProject.instance()         
manager = project.layoutManager() 
layouts_list = manager.printLayouts()
layer = iface.activeLayer()
#manager.clear() #- remove all layouts

checked_layers = [layer.name() for layer in QgsProject().instance().layerTreeRoot().children() if layer.isVisible()]
layersToAdd = [layer for layer in QgsProject().instance().mapLayers().values() if layer.name() in checked_layers]

layout = QgsPrintLayout(project)        
layout.initializeDefaults()
layout.setName("Layout_0")
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
    map.attemptResize(QgsLayoutSize(297, 159.495, QgsUnitTypes.LayoutMillimeters))
    
    root = QgsLayerTree()
    for layer in layersToAdd:
        root.addLayer(layer)
        
    legend = QgsLayoutItemLegend(layout)
    legend.model().setRootGroup(root)
    layout.addLayoutItem(legend)
    legend.attemptMove(QgsLayoutPoint(2, 159.5, QgsUnitTypes.LayoutMillimeters), page = i)
    legend.setTitle("EUNIS Habitat clasification / EUNIS klasifikacija staništa")
    
    legend.setStyleFont(QgsLegendStyle.Title, QFont("Calibri", 14))
    legend.setStyleFont(QgsLegendStyle.Subgroup, QFont("Calibri", 12))
    legend.setStyleFont(QgsLegendStyle.SymbolLabel, QFont("Calibri", 10))
    legend.setTitleAlignment(Qt.AlignCenter)
    
    legend.setAutoUpdateModel(False)
    legend.setLinkedMap(map)
    legend.setLegendFilterByMapEnabled(True)
    legend.setColumnCount(2)
    legend.refresh()
    
    north = QgsLayoutItemPicture(layout)
    north.setPicturePath(":/images/north_arrows/layout_default_north_arrow.svg")
    layout.addLayoutItem(north)
    north.attemptResize(QgsLayoutSize(12, 12, QgsUnitTypes.LayoutMillimeters))
    north.attemptMove(QgsLayoutPoint(283.271,1, QgsUnitTypes.LayoutMillimeters), page = i)
    north.setLinkedMap(map)
    
    scale_bar = QgsLayoutItemScaleBar(layout)
    layout.addLayoutItem(scale_bar)
    scale_bar.attemptResize(QgsLayoutSize(114, 14, QgsUnitTypes.LayoutMillimeters))
    scale_bar.attemptMove(QgsLayoutPoint(0,147.3, QgsUnitTypes.LayoutMillimeters), page = i)
    scale_bar.setLinkedMap(map)
    scale_bar.setNumberOfSegments(4)
    text_format = QgsTextFormat()
    text_format.setFont(QFont("Calibri", 10))
    scale_bar.setTextFormat(text_format)
    scale_bar.setSegmentSizeMode(1)
    scale_bar.setBackgroundEnabled(True)
    scale_bar.setUnits(250)
    
    map_page = QgsLayoutItemLabel(layout)
    map_page.setText(str(i+1))
    map_page.setFont(QFont("Calibri", 12))
    map_page.adjustSizeToText() 
    layout.addLayoutItem(map_page)
    map_page.attemptMove(QgsLayoutPoint(291,203, QgsUnitTypes.LayoutMillimeters), page = i)

    
    