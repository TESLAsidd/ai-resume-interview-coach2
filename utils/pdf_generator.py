from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_report_pdf(report_text, output_path):

    doc = SimpleDocTemplate(output_path)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Resume & Interview Coach Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            report_text.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    doc.build(content)
