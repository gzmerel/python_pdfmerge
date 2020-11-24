import csv
import os 
from PyPDF4 import PdfFileMerger
from tkinter.filedialog import askopenfilename
qty=0 
filename = askopenfilename()    
def search_item():
    items = []
    with open (filename,"r") as file:
        reader = csv.reader(file)

        for row in reader:
            items.append(row[1]) 
    
    return items  

def search_file():
    item = search_item()
    pdf = []
    directory = "C:\\Users\\Gizem\\Desktop\\cv\\Resumes"
    qty = len(item)
    for i in range(1,qty):
        for filename in os.listdir(directory):
            if item[i] in filename and filename.endswith(".pdf") :
                
                pdf.append(os.path.join(directory, filename))
    return pdf


pdfs = search_file()
print(pdfs)


merger = PdfFileMerger()

for k in pdfs:
    merger.append(k)

merger.write("C:\\Users\\Gizem\\Desktop\\result.pdf")
merger.close()