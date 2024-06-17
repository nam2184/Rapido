import PyPDF2

# Open the PDF file
def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    number_of_pages = len(reader.pages)
    text = ""
    
    # Extract text from each page
    for page_number in range(number_of_pages):
        page = reader.pages[page_number]
        text += page.extract_text()
    return text

