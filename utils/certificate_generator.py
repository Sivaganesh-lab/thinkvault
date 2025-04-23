from fpdf import FPDF
import os

def generate_certificate(idea_hash: str, timestamp: str, output_path: str = "output/certificate.pdf"):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font("Arial", 'B', 20)
    pdf.cell(200, 20, txt="ThinkVault Certificate", ln=True, align='C')

    # Add space
    pdf.ln(10)

    # Details
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="This certifies that the following idea existed at the given time:", ln=True, align='L')
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=f"Idea Hash: {idea_hash}")
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Timestamp (UTC): {timestamp}", ln=True)

    # Save PDF
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf.output(output_path)
    return output_path
