from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader

# Output PDF file
pdf_file = "User_Manual.pdf"

# Create canvas
c = canvas.Canvas(pdf_file, pagesize=letter)
width, height = letter

# Title
c.setFont("Helvetica-Bold", 16)
c.drawCentredString(width / 2, height - 1 * inch, "CSV Cleanup Tool – Quick Start Guide")

# Purpose
c.setFont("Helvetica-Bold", 12)
c.drawString(1 * inch, height - 1.5 * inch, "Purpose:")
c.setFont("Helvetica", 10)
c.drawString(1.2 * inch, height - 1.7 * inch,
             "Merge, clean, and standardize CSV files into Excel-ready datasets.")
c.drawString(1.2 * inch, height - 1.85 * inch,
             "Designed for non-technical users.")

# Step 1
c.setFont("Helvetica-Bold", 12)
c.drawString(1 * inch, height - 2.2 * inch, "Step 1: Open the Tool")
c.setFont("Helvetica", 10)
c.drawString(1.2 * inch, height - 2.4 * inch, "Double-click 'csv_cleanup_gui.exe' in the dist folder.")

# Step 2
c.setFont("Helvetica-Bold", 12)
c.drawString(1 * inch, height - 2.7 * inch, "Step 2: Select CSV Folder")
c.setFont("Helvetica", 10)
c.drawString(1.2 * inch, height - 2.9 * inch,
             "Click 'Browse' and select the folder containing your CSV files.")

# Step 3
c.setFont("Helvetica-Bold", 12)
c.drawString(1 * inch, height - 3.2 * inch, "Step 3: Clean Your Data")
c.setFont("Helvetica", 10)
c.drawString(1.2 * inch, height - 3.4 * inch,
             "Click 'Clean Data'. The tool merges, trims, removes duplicates,")
c.drawString(1.2 * inch, height - 3.55 * inch, "and standardizes your data automatically.")

# Step 4
c.setFont("Helvetica-Bold", 12)
c.drawString(1 * inch, height - 3.8 * inch, "Step 4: Find Your Cleaned File")
c.setFont("Helvetica", 10)
c.drawString(1.2 * inch, height - 4.0 * inch,
             "Check the 'cleaned' folder in the project directory.")
c.drawString(1.2 * inch, height - 4.15 * inch, "Open 'clean_data.xlsx' to view results.")

# Tips
c.setFont("Helvetica-Bold", 12)
c.drawString(1 * inch, height - 4.5 * inch, "Tips:")
c.setFont("Helvetica", 10)
c.drawString(1.2 * inch, height - 4.7 * inch, "- Place all CSVs in one folder before running")
c.drawString(1.2 * inch, height - 4.85 * inch, "- No Python knowledge required")
c.drawString(1.2 * inch, height - 5.0 * inch, "- Double-click executable for future use")

# Add GUI screenshot
try:
    gui_img = ImageReader("gui_screenshot.png")
    c.drawImage(gui_img, 1 * inch, height - 7.0 * inch, width=3.5*inch, height=2*inch)
except:
    print("GUI screenshot not found, skipping...")

# Add Success screenshot
try:
    success_img = ImageReader("success_screenshot.png")
    c.drawImage(success_img, 4.5 * inch, height - 7.0 * inch, width=3.5*inch, height=2*inch)
except:
    print("Success screenshot not found, skipping...")

# Save PDF
c.save()
print("User_Manual.pdf created successfully!")
