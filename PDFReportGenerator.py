from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


import os


class PDFReportGenerator:
    def __init__(self, output_filename: str, logo_path: str = None, title: str = "Sales Report 2024"):
        self.output_filename = output_filename
        self.logo_path = logo_path
        self.title = title
        self.styles = getSampleStyleSheet()

    def generate_report(self, sorted_data, total_revenue):
        # Create the PDF document
        doc = SimpleDocTemplate(self.output_filename, pagesize=letter)
        elements = []

        # Create the header with logo and title in one row
        header_data = []
        if self.logo_path and os.path.exists(self.logo_path):
            try:
                logo = Image(self.logo_path, width=100, height=50)
            except Exception as e:
                print(f"Error loading logo: {e}")
                logo = Paragraph("", self.styles["Normal"])
        else:
            logo = Paragraph("", self.styles["Normal"])

        title_paragraph = Paragraph(self.title, self.styles["Title"])
        header_data.append([logo, title_paragraph])

        header_table = Table(header_data, colWidths=[110, 400])
        header_table.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (1, 0), (1, 0), "CENTER")
        ]))
        elements.append(header_table)
        elements.append(Spacer(1, 24))

        # Prepare table data with header
        table_data = []
        table_data.append(["Product", "Quantity", "Price ($)", "Revenue ($)"])

        # Modified: Access ProductSale object attributes directly
        for item in sorted_data:
            table_data.append([
                item.product,
                item.quantity,
                f"{item.price:.2f}",
                f"{item.revenue:.2f}"
            ])

        # Append the summary row with total revenue
        table_data.append(["Total Revenue:", "", "", f"{total_revenue:.2f}"])

        table = Table(table_data, hAlign="LEFT")
        style = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (1, 1), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -2), colors.beige),
            ("GRID", (0, 0), (-1, -1), 1, colors.black)
        ])
        style.add("FONTNAME", (0, len(table_data)-1), (-1, len(table_data)-1), "Helvetica-Bold")
        table.setStyle(style)

        elements.append(table)

        try:
            doc.build(elements)
            print(f"PDF report generated successfully: {self.output_filename}")
        except Exception as e:
            print(f"Error generating PDF: {e}")