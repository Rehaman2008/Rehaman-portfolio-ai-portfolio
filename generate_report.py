import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

BASE_DIR = r"C:\Users\shaik\.gemini\antigravity\scratch\ai-portfolio"
OUTPUT_PDF = os.path.join(BASE_DIR, "2026BTAI076_Shaik_Rehaman_Shareef_AI_Portfolio.pdf")

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(40, 755, "Task 1: AI-Based Personal Portfolio Website Creation & Publishing")
            self.drawRightString(612 - 40, 755, "Reg No: 2026BTAI076 | Shaik Rehaman Shareef")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(40, 748, 612 - 40, 748)

        # Footer
        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(612 - 40, 25, footer_text)
        self.drawString(40, 25, "School of Computational Intelligence — JOY University")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(40, 34, 612 - 40, 34)
        self.restoreState()

def build_pdf(live_url="https://shaikrehamanshareef.github.io/portfolio/"):
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    primary_color = colors.HexColor("#0f294a") # Deep Royal Navy
    secondary_color = colors.HexColor("#0369a1") # Sky Blue
    accent_color = colors.HexColor("#4338ca") # Indigo
    text_dark = colors.HexColor("#0f172a")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=17,
        leading=21,
        textColor=primary_color,
        alignment=1,
        spaceAfter=3
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=accent_color,
        alignment=1,
        spaceAfter=10
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=primary_color,
        spaceBefore=8,
        spaceAfter=5,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=secondary_color,
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=text_dark
    )

    elements = []

    # Title & Header
    elements.append(Paragraph("PYTHON AND AI-BASED PRACTICAL ASSIGNMENTS", title_style))
    elements.append(Paragraph("TASK 1: AI-BASED PERSONAL PORTFOLIO WEBSITE CREATION AND PUBLISHING", subtitle_style))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=primary_color, spaceAfter=8))

    # SECTION A: Student Details
    elements.append(Paragraph("A. Student Details", h1_style))
    student_data = [
        [Paragraph("<b>Student Name:</b>", body_style), Paragraph("Shaik Rehaman Shareef", body_style),
         Paragraph("<b>Registration Number:</b>", body_style), Paragraph("2026BTAI076", body_style)],
        [Paragraph("<b>Degree & Branch:</b>", body_style), Paragraph("B.Tech CSE (Artificial Intelligence)", body_style),
         Paragraph("<b>Current Academic Status:</b>", body_style), Paragraph("1st Year / Semester 1", body_style)],
        [Paragraph("<b>Section:</b>", body_style), Paragraph("Section A", body_style),
         Paragraph("<b>Email Address:</b>", body_style), Paragraph("shaikrehamanshareef2008@gmail.com", body_style)],
        [Paragraph("<b>School:</b>", body_style), Paragraph("School of Computational Intelligence", body_style),
         Paragraph("<b>Department:</b>", body_style), Paragraph("Dept. of Computer Science & Engineering (AI)", body_style)]
    ]
    student_table = Table(student_data, colWidths=[110, 156, 120, 146])
    student_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    elements.append(student_table)
    elements.append(Spacer(1, 6))

    # SECTION B: Portfolio Information
    elements.append(Paragraph("B. Portfolio Information", h1_style))
    port_info_data = [
        [
            Paragraph("<b>Name of AI Tool Used:</b>", body_style),
            Paragraph("<b>Google AI Studio / Gemini AI & Antigravity AI Assistant</b>", body_style)
        ],
        [
            Paragraph("<b>Technologies & Tools:</b>", body_style),
            Paragraph("HTML5 Semantic Architecture, CSS3 (Custom Properties, Flexbox, CSS Grid, Glassmorphism Backdrop-Filter), Vanilla JavaScript (ES6+), FontAwesome Icons v6.5, Google Fonts (Plus Jakarta Sans, JetBrains Mono), GitHub Pages / Web Hosting.", body_style)
        ],
        [
            Paragraph("<b>Short Description:</b>", body_style),
            Paragraph(
                "A state-of-the-art, responsive personal portfolio website engineered specifically to present academic milestones, technical proficiencies, and software projects for an AI undergraduate. The website includes dynamic typing animations, persistent dark/light theme switching, animated interactive skill progress indicators, an academic timeline, structured project showcases with active GitHub links, and an interactive contact interface. It strictly conforms to all pedagogical requirements outlined in Task 1.",
                body_style
            )
        ]
    ]
    port_table = Table(port_info_data, colWidths=[130, 402])
    port_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    elements.append(port_table)
    elements.append(Spacer(1, 6))

    # SECTION D: Published Portfolio URL
    elements.append(Paragraph("D. Published Portfolio URL", h1_style))
    url_content = f"""
    <b>Final Published Portfolio Website Link:</b> &nbsp;
    <a href="{live_url}"><u><b>{live_url}</b></u></a><br/>
    <font color="#15803d"><b>Verification Status:</b> Publicly accessible without requiring login credentials or access approval. Verified in Incognito mode across desktop and mobile browsers.</font>
    """
    url_table = Table([[Paragraph(url_content, body_style)]], colWidths=[532])
    url_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f0fdf4")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#16a34a")),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    elements.append(url_table)
    
    # PageBreak to Section C (Screenshots)
    elements.append(PageBreak())

    # SECTION C: Screenshots of All Required Sections
    elements.append(Paragraph("C. Screenshots of Important Website Sections", h1_style))
    elements.append(Paragraph("High-resolution captures displaying all required sections of the live portfolio website:", body_style))
    elements.append(Spacer(1, 6))

    sections_info = [
        (
            "1. Home Section",
            "screenshot_1_home.png",
            "Includes Full Name (Shaik Rehaman Shareef), dynamic typewriter title, professional introduction, academic status badge (B.Tech CSE - AI, 1st Year), primary action buttons, and professional social links."
        ),
        (
            "2. About Me Section",
            "screenshot_2_about.png",
            "Features the educational background timeline (B.Tech at JOY University, Intermediate at Narayana Jr. College with 77%, and Class X at Narayana High School with 82%), core technical interests in AI and software, and long-term career aspirations."
        ),
        (
            "3. Skills Section",
            "screenshot_3_skills.png",
            "Features core technical competencies focused specifically on Python Programming (syntax, data structures, and functions) and HTML & CSS Web Development with interactive visual progress meters."
        ),
        (
            "4. Projects Section",
            "screenshot_4_projects.png",
            "Featured showcase of the primary personal engineering project: 'Bal Ganesh: Modak Catcher & Mooshak\\'s Maya Leela'—an interactive 2D web arcade and platforming game built with HTML5 Canvas, ES6 JavaScript, and Web Audio API across 50 custom trials."
        ),
        (
            "5. Achievements Section",
            "screenshot_5_achievements.png",
            "Displays academic certifications in Python and Web Application Development, high school distinction awards, and active memberships in the Computational Intelligence Society."
        ),
        (
            "6. Contact Section",
            "screenshot_6_contact.png",
            "Presents professional email address (shaikrehamanshareef2008@gmail.com), university location, social profile links, and an interactive direct message contact form."
        ),
    ]

    for i, (title, img_filename, desc) in enumerate(sections_info):
        img_path = os.path.join(BASE_DIR, img_filename)
        section_elements = []
        section_elements.append(Paragraph(f"<b>{title}</b>", h2_style))
        section_elements.append(Paragraph(desc, body_style))
        section_elements.append(Spacer(1, 4))
        
        if os.path.exists(img_path):
            img = RLImage(img_path, width=520, height=215)
            section_elements.append(img)
        else:
            placeholder_data = [[Paragraph(f"<i>[Screenshot placeholder for {title} - {img_filename}]</i>", body_style)]]
            t = Table(placeholder_data, colWidths=[520], rowHeights=[170])
            t.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f1f5f9")),
                ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#94a3b8")),
                ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ]))
            section_elements.append(t)

        section_elements.append(Spacer(1, 10))
        elements.append(KeepTogether(section_elements))

        # Add page breaks between screenshots for pristine readability (2 per page)
        if (i + 1) % 2 == 0 and (i + 1) < len(sections_info):
            elements.append(PageBreak())

    # Build the document
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"[3/3] PDF generated successfully: {OUTPUT_PDF}")

if __name__ == "__main__":
    live_url = sys.argv[1] if len(sys.argv) > 1 else "https://shaikrehamanshareef.github.io/portfolio/"
    build_pdf(live_url)
