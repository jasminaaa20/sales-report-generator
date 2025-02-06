# Sales Report PDF Generator

## Overview
The Sales Report PDF Generator is a Python project that processes sales data, calculates revenue per product, and generates a structured PDF report using the `reportlab` library. The report features a header with the company logo and the report title arranged side-by-side, followed by a table displaying the sales data and a summary of the total revenue.

This project demonstrates the use of Python classes, data structures (lists and dictionaries), error handling, and PDF generation.

## Features
- **Sales Data Processing**
  - Calculates revenue for each product (quantity × price).
  - Sorts products by revenue in descending order.
- **PDF Report Generation**
  - Generates a PDF report with a header containing a company logo and title.
  - Displays a table with product sales data and a summary row with total revenue.
- **Future Enhancements**
  - Generate multiple PDFs for different months.
  - Insert bar charts using `matplotlib`.
  - Export the sales data to Excel.

## Prerequisites
- Python 3.6 or higher
- `pip` package manager

## Setup

### 1. Clone the Repository
Clone the GitHub repository to your local machine:
```bash
git clone https://github.com/jasminaaa20/sales-report-generator.git
cd sales-report-generator
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies:
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
- **On Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
All required packages are listed in the `requirements.txt` file. Install them using:
```bash
pip install -r requirements.txt
```

## Running the Project
1. **Configuration (Optional)**
   - Update the path to your company logo in the `main.py` script if needed.
   - Modify the sales data or report title as desired.

2. **Generate the PDF Report**
   Run the main script to generate the PDF report:
   ```bash
   python main.py
   ```
   The script will process the sales data and generate a PDF file named `sales_report.pdf` in the project directory.

## Project Structure
```
sales-report-pdf-generator/
├── company_logo.png         # Company logo image used in the report header (optional)
├── main.py          # Main Python script with classes for data processing and PDF generation
├── requirements.txt         # List of required Python packages
└── README.md                # Project documentation
```

## Contributing
Contributions are welcome! If you have ideas for improvements or find any issues, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
- [ReportLab](https://www.reportlab.com/) for the powerful PDF generation library.
- [Matplotlib](https://matplotlib.org/) (planned) for future chart integration.
