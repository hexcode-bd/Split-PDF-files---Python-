import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter.filedialog import askopenfilename

# Use Tkinter for Python 3.x

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

pdf_file_path = filename

file_base_name = pdf_file_path.replace('.pdf', '') # Select Extension
output_folder_path = os.path.join(os.getcwd(), 'Output') # Must Select Output Name
pdf = PdfFileReader(pdf_file_path)

for page_num in range(pdf.numPages):
    pdfWriter = PdfFileWriter()
    pdfWriter.addPage(pdf.getPage(page_num))

    with open(os.path.join(output_folder_path, '{0}_Page{1}.pdf'.format(file_base_name, page_num+1)), 'wb') as f:
        pdfWriter.write(f)     
        f.close()

    
