from fpdf import FPDF
import os

class PDFReport(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'AI Resume Analysis Report', 0, 0, 'C')
        # Line break
        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

def generate_pdf_report(analysis_data, filename="resume_report.pdf"):
    """
    Generates a PDF report based on the analysis data.
    """
    pdf = PDFReport()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    # Ensure fonts are standard, FPDF default is Arial (maps to Helvetica)
    pdf.set_font('Arial', 'B', 12)
    
    # ATS Score and Match
    pdf.cell(0, 10, f"ATS Score: {analysis_data.get('ats_score', 0)} / 100", ln=True)
    pdf.cell(0, 10, f"Role Match: {analysis_data.get('match_percentage', 0)}%", ln=True)
    pdf.ln(5)
    
    # Summary
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "Summary", ln=True)
    pdf.set_font('Arial', '', 10)
    # Using multi_cell for text that might wrap
    pdf.multi_cell(0, 7, str(analysis_data.get('summary', '')))
    pdf.ln(5)
    
    # Strengths
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "Strengths", ln=True)
    pdf.set_font('Arial', '', 10)
    for strength in analysis_data.get('strengths', []):
        pdf.cell(0, 7, f"- {strength}", ln=True)
    pdf.ln(5)
    
    # Weaknesses
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "Areas for Improvement", ln=True)
    pdf.set_font('Arial', '', 10)
    for weakness in analysis_data.get('weaknesses', []):
        pdf.cell(0, 7, f"- {weakness}", ln=True)
    pdf.ln(5)
    
    # Missing Skills
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "Missing Skills for Target Role", ln=True)
    pdf.set_font('Arial', '', 10)
    for skill in analysis_data.get('missing_skills', []):
        pdf.cell(0, 7, f"- {skill}", ln=True)
    pdf.ln(5)
    
    # Suggestions
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "Actionable Suggestions", ln=True)
    pdf.set_font('Arial', '', 10)
    for sug in analysis_data.get('suggestions', []):
        pdf.multi_cell(0, 7, f"[{sug.get('category', 'General')}] {sug.get('advice', '')}")
        pdf.ln(2)
        
    output_path = os.path.join("E:\\ai_resume_analyzer", filename)
    pdf.output(output_path)
    return output_path
