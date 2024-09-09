import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# Function to generate a personalized invitation
def create_invitation(template_pdf, output_pdf, name):
    # Open the template PDF
    reader = PyPDF2.PdfReader(template_pdf)
    writer = PyPDF2.PdfWriter()

    # Create a new PDF with the name
    c = canvas.Canvas("temp.pdf", pagesize=letter)
    c.drawString(100, 750, f"Dear {name},")  # Adjust position as needed
    c.save()

    # Merge the new name PDF with the template
    name_pdf = PyPDF2.PdfReader("temp.pdf")

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        page.merge_page(name_pdf.pages[0])  # Merge on each page
        writer.add_page(page)

    # Save the result
    with open(output_pdf, "wb") as output:
        writer.write(output)

    os.remove("temp.pdf")  # Clean up temporary file

# Function to handle the entire process
def generate_invitations(template_pdf, names):
    for name in names:
        output_filename = f"invitation_for_{name}.pdf"
        create_invitation(template_pdf, output_filename, name)
        print(f"Created: {output_filename}")

# Example usage
if __name__ == "__main__":
    # Replace 'template.pdf' with the path to your invitation PDF template
    template_pdf = "template.pdf"

    # Replace with the list of guest names
    names = ["Alice", "Bob", "Charlie"]

    generate_invitations(template_pdf, names)
