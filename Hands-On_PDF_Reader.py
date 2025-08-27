from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader

# Step 1: Create a PDF called "intro.pdf"
c = canvas.Canvas("intro.pdf")
c.drawString(100, 750, "Hello Noor! This is a test PDF file.")
c.drawString(100, 730, "You can now open and read me with PyPDF2.")
c.save()

print("PDF created successfully: intro.pdf")

# Step 2: Reading PDF
new_pdf = open('intro.pdf', 'rb')  # file object creation
reading_pdf = PdfReader(new_pdf)   # pdf reader object
print("Number of pages in PDF:", len(reading_pdf.pages))  # number of pages

pdf_page = reading_pdf.pages[0]  # page object creation
print("Extracted text from page 1:")
print(pdf_page.extract_text())

# Close PDF File
new_pdf.close()
