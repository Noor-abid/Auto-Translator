from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import red, blue, green
from PyPDF2 import PdfReader

# Step 1: Create a styled PDF
pdf_filename = "styled_intro.pdf"
c = canvas.Canvas(pdf_filename, pagesize=A4)

# Title (big and bold, centered)
c.setFont("Helvetica-Bold", 24)
c.setFillColor(blue)
c.drawCentredString(300, 800, "Welcome to Noor's PDF ")

#Subtitle
c.setFont("Helvetica", 16)
c.setFillColor(green)
c.drawCentredString(300, 770, "Created with ReportLab + PyPDF2")

# Body text
c.setFont("Times-Roman", 12)
c.setFillColor(red)
c.drawString(100, 720, "This PDF shows fonts, colors, and positioning.")
c.drawString(100, 700, " You can even add multiple pages!")

# Add a second page
c.showPage()
c.setFont("Courier-Bold", 18)
c.setFillColor(blue)
c.drawString(100, 750, "This is Page 2")
c.drawString(100, 720, "You can keep adding as many pages as you like!")
 # Save the PDF
c.save()
print("PDF created successfully: styled_intro.pdf")

# Step 2: Read the styled PDF
with open(pdf_filename, "rb") as pdf_file:
    reader = PdfReader(pdf_file)

    print("Number of pages:", len(reader.pages))

    # Loop through all pages and extract text
    for i, page in enumerate(reader.pages):
        print(f"\n--- Page {i+1} ---")
        print(page.extract_text())