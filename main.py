from ExcelReportGenerator import ExcelReportGenerator
from PDFReportGenerator import PDFReportGenerator
from SalesDataProcessor import SalesDataProcessor


sales_data = {
    "Mouse": {"quantity": 10, "price": 20},
    "Laptop": {"quantity": 5, "price": 800},
    "Keyboard": {"quantity": 7, "price": 50},
    "Monitor": {"quantity": 3, "price": 300},
    "USB Drive": {"quantity": 15, "price": 10}
}

processor = SalesDataProcessor(sales_data)
sorted_data, total_revenue = processor.process_data()

output_pdf = "sales_report.pdf"
output_excel = "sales_report.xlsx"
logo_image = "company_logo.png"

pdf_generator = PDFReportGenerator(output_pdf, logo_image, "Sales Report 2024")
pdf_generator.generate_report(sorted_data, total_revenue)

excel_generator = ExcelReportGenerator(output_excel, "Sales Report 2024")
excel_generator.generate_report(sorted_data, total_revenue)