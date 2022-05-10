project = QgsProject.instance()         
manager = project.layoutManager() 
layer = iface.activeLayer()
manager.clear() #- remove all layouts

lista_imena_PP = ["PPŠKŽ 1  - Korištenje i namjena zemljišta",
"PPŠKŽ 2 - infrastrukturni sustavi - energetika",
"PPŠKŽ 3 - Posebni uvjeti korištenja, uređenja i zaštite prostora",
"PPUG Knin 1 - Korištenje i namjena prostora",
"PPUG Knin 2 - Infrastrukturni sustavi - energetika",
"PPUG Knin 3.1 - Uvjeti korištenja - Područja posebnih uvjeta korištenja",
"PPUG Knin 3.2 - Uvjeti korištenja - područja posebnih ograničenja u korištenju",
"PPUG Knin 3.3 - Područja primjene posebnih mjera uređenja i zaštite",
"PPUO Ervenik 1 - Korištenje i namjena prostora",
"PPUO Ervenik 2 - Infrastrukturni sustavi i mreže"]

templejt_a3 = QgsPrintLayout(project)
template_file = open('C:\\Users\\ngersak\\Documents\\pitonac_backup\\Kartiranje plinovoda\\oton_template_a3.qpt')
template_content = template_file.read()
template_file.close()
document = QDomDocument()
document.setContent(template_content)
templejt_a3.loadFromTemplate(document, QgsReadWriteContext()) 
manager.addLayout(templejt_a3)

sastavnica_path = '\\\\server\\Ecro\\2_StrucneUsluge\\1_PUOP\\2_PUO\\SUO_GOEM_Novaenergija_VE_Oton\\2_Radno\\EUPP\\graficki\\Materijali\\4_Sastavnice'
tumac_path = '\\\\server\\Ecro\\2_StrucneUsluge\\1_PUOP\\2_PUO\\SUO_GOEM_Novaenergija_VE_Oton\\2_Radno\\EUPP\\graficki\\Materijali\\5_Tumaci'

for i, f in enumerate(lista_imena_PP): 
    ime = '0'+ str(i+1)+ '_' + lista_imena_PP[i]
    layout = QgsPrintLayout(project)        
    layoutName = ime
    layout = manager.duplicateLayout(templejt_a3,ime)
    
    my_table = layout.items()
    broj_str = my_table[0]
    broj_str.setText(str(i+1))
    
    naziv_priloga = my_table[1]
    naziv_priloga.setText("Planirani zahvat na podlozi " + f)
    
    izvor_podloga = my_table[2]
    izvor_podloga.setText("Idejni projekt VE Oton i " + f)
    
    map = my_table[4]
    mjerilo = my_table[3]
    if re.match(r"PPŠKŽ",f):
        mjerilo.setText("1:100 000")
    if re.match(r"PPUG",f):
        mjerilo.setText("1:25 000")
        map.setScale(25000)
    if re.match(r"PPUO",f):
        mjerilo.setText("1:25 000")
        map.setScale(25000)
    
    sastavnica = my_table[5]
    sastavnica.setPicturePath(str(sastavnica_path + "\\Sastavnica_" + f + ".jpg"))
    sastavnica.setMode(1)
    
    tumac_1 = my_table[6]
    tumac_1.setPicturePath(str(tumac_path + "\\Tumac_" + f + "_1.jpg"))
    tumac_2 = my_table[7]
    tumac_2.setPicturePath(str(tumac_path + "\\Tumac_" + f + "_2.jpg"))
    tumac_3 = my_table[8]
    tumac_3.setPicturePath(str(tumac_path + "\\Tumac_" + f + "_3.jpg"))

print("done")