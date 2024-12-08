#!/usr/bin/env python3
import argparse
import pdfkit
import os
from datetime import datetime

def create_pdf_from_markdown(markdown_path, output_dir='output'):
    """Convert markdown file to PDF"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    filename = os.path.basename(markdown_path)
    pdf_filename = f"{os.path.splitext(filename)[0]}.pdf"
    pdf_path = os.path.join(output_dir, pdf_filename)
    
    # Configure pdfkit to use wkhtmltopdf in headless mode
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    
    options = {
        'page-size': 'A4',
        'margin-top': '20mm',
        'margin-right': '20mm',
        'margin-bottom': '20mm',
        'margin-left': '20mm',
        'encoding': 'UTF-8',
        'custom-header': [('Accept-Encoding', 'gzip')],
        'no-outline': None,
        'quiet': ''
    }
    
    try:
        # Try using xvfb-run if available
        os.system(f'xvfb-run -- wkhtmltopdf {markdown_path} {pdf_path}')
    except:
        # Fallback to regular pdfkit if xvfb-run fails
        with open(markdown_path, 'r') as md_file:
            markdown_content = md_file.read()
        pdfkit.from_string(markdown_content, pdf_path, options=options, configuration=config)
    
    return pdf_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert markdown to PDF')
    parser.add_argument('markdown_file', help='Path to markdown file')
    parser.add_argument('--output-dir', default='output', help='Output directory for PDF')
    
    args = parser.parse_args()
    
    try:
        pdf_path = create_pdf_from_markdown(args.markdown_file, args.output_dir)
        print(f"PDF generated successfully: {pdf_path}")
    except Exception as e:
        print(f"Error generating PDF: {str(e)}")
