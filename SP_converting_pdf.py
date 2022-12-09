import os
import fitz

def pdf_export(path_files):

    files = [f for f in os.listdir(path_files) if f.endswith('pdf')]

    for f in files:
        pdffile = path_files + "\\" + f
        doc = fitz.open(pdffile)
        zoom = 12
        mat = fitz.Matrix(zoom, zoom)
        count = 0
        # Count variable is to get the number of pages in the pdf
        for p in doc:
            count += 1
        for i in range(count):
            #val = f"image_{i+1}.png"
            val = path_files + "\\"+ f + ".jpg"
            page = doc.load_page(i)
            pix = page.get_pixmap(matrix=mat)
            pix.save(val)
        doc.close()
        print("pdf " + f + " converted!")
    print("all files converted!")

current_path = r"\\server.intranet.dvokut-ecro.hr\Ecro\2_StrucneUsluge\1_PUOP\2_PUO\SUO_GOEM_Oikon_plinovodix3\Osijek-Vukovar\2_radno\PP dok\PP_Materijali\proba"
pdf_export(current_path)