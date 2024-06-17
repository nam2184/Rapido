import PyPDF2
from pdfreader import PDFDocument, SimplePDFViewer
import os

current_dir= os.getcwd()
parent_dir = os.path.dirname(current_dir)

file1 = f"{parent_dir}/UTS-Hackathon/MAN_32-40_IMO_TierIII–Marine_.pdf"
file2 = f"{parent_dir}/UTS-Hackathon/MAN_32-40_Troubleshooting_Guide.pdf"


# Open the PDF file
with open(file1, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    number_of_pages = len(reader.pages)
    text = ""
    
    # Extract text from each page
    for page_number in range(number_of_pages):
        page = reader.pages[page_number]
        text += page.extract_text()
        
print(text)

