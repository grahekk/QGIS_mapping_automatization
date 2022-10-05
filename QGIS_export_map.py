project = QgsProject.instance()         
manager = project.layoutManager() 
zahvat = iface.activeLayer()

ime = 'KS'
to_remove = manager.layoutByName(ime)
manager.removeLayout(to_remove)

layout = QgsPrintLayout(project)
template_file = open('C:\\Users\\ngersak\\Documents\\pitonac_backup\\Kartiranje plinovoda\\' + ime + '.qpt')
template_content = template_file.read()
template_file.close()
document = QDomDocument()
document.setContent(template_content)
layout.loadFromTemplate(document, QgsReadWriteContext()) 
layout.setName('KS')
manager.addLayout(layout)

my_table = layout.items()
map = my_table[3]
rect = zahvat.extent()
rect.scale(1.1)
map.zoomToExtent(rect)

path = QgsProject.instance().readPath("./")
path = path + '/'

exporter = QgsLayoutExporter(layout)
exporter.exportToImage(path + ime + '.jpg', exporter.ImageExportSettings())

print("Layout exported")