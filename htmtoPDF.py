# htmtoPDF.py
# Converts a list of URLs from a text file into a single merged PDF document.
import os
import pdfkit
from pypdf import PdfWriter
import time
import sys

# --- Configuration ---
# IMPORTANT: Update this path to where wkhtmltopdf is installed on your system.
# Windows example: r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
# macOS (if installed with Homebrew): '/usr/local/bin/wkhtmltopdf'
# Linux (if installed with apt): '/usr/bin/wkhtmltopdf'
# If wkhtmltopdf is in your system's PATH, you might be able to leave this as just 'wkhtmltopdf'

WKHTMLTOPDF_PATH = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'

INPUT_FILE = 'Htm\\Links.txt' # Text file location with URLs (one per line)
OUTPUT_PDF = 'Converted_do.pdf'
TEMP_DIR = 'temp_pdfs'

def initialize_converter():
    """Checks for wkhtmltopdf and returns a pdfkit configuration."""
    try:
        return pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
    except OSError:
        print("--- ERROR ---")
        print(f"Could not find wkhtmltopdf at the specified path: {WKHTMLTOPDF_PATH}")
        print("Please install wkhtmltopdf and/or update the WKHTMLTOPDF_PATH variable in this script.")
        print("See README.md for installation instructions.")
        sys.exit(1) 

def read_links_from_file(filename):
    """Reads URLs from a text file, one URL per line."""
    if not os.path.exists(filename):
        print(f"Error: Input file '{filename}' not found.")
        print("Please create it and add your URLs, one per line.")
        return []
        
    with open(filename, 'r') as f:
        links = [line.strip() for line in f if line.strip()]
    
    print(f"Found {len(links)} link(s) in '{filename}'.")
    return links
def convert_urls_to_pdfs(urls, config):

    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)
        print(f"Created temporary directory: '{TEMP_DIR}'")

    pdf_files = []
    failed_urls = []
    for i, url in enumerate(urls):
        try:
            output_filename = os.path.join(TEMP_DIR, f'output_{i}.pdf')
            print(f"({i+1}/{len(urls)}) Converting {url} ...")
            
            options = {
                '--load-error-handling': 'skip',
                '--no-stop-slow-scripts': '',
                '--enable-javascript': '',
                '--javascript-delay': '2000',
                '--quiet': ''
            }
            
            pdfkit.from_url(url, output_filename, configuration=config, options=options)
            pdf_files.append(output_filename)
            print(f" -> Successfully created '{output_filename}'")
            time.sleep(1) 
        except Exception as e:
            print(f" -> ERROR: Could not convert {url}. Reason: {e}")
            failed_urls.append(url)
            
    return pdf_files, failed_urls

def merge_pdfs(pdf_list, output_filename):
    """Merges a list of PDF files into a single PDF."""
    if not pdf_list:
        print("No PDFs were created to merge. Exiting.")
        return

    merger = PdfWriter()
    print("\nMerging individual PDFs...")
    for pdf in pdf_list:
        try:
            merger.append(pdf)
            print(f"- Appending {pdf}")
        except Exception as e:
            print(f"- ERROR appending {pdf}. Reason: {e}")
    
    try:
        with open(output_filename, 'wb') as f_out:
            merger.write(f_out)
        print(f"\nSuccessfully merged {len(pdf_list)} files into '{output_filename}'")
    except Exception as e:
        print(f"\nERROR: Failed to write final PDF. Reason: {e}")
    finally:
        merger.close()

def cleanup(files_to_clean):
    """Removes temporary files and the directory."""
    print("\nCleaning up temporary files...")
    for f in files_to_clean:
        try:
            os.remove(f)
        except OSError as e:
            print(f"Error removing file {f}: {e}")
            
    if os.path.exists(TEMP_DIR):
        try:
            os.rmdir(TEMP_DIR)
            print(f"Removed temporary directory: '{TEMP_DIR}'")
        except OSError as e:
            print(f"Error removing directory {TEMP_DIR}: {e}")

def main():
    """Main function to run the conversion and merging process."""
    start_time = time.time()
  
    config = initialize_converter()
    urls = read_links_from_file(INPUT_FILE)
    
    if not urls:
        return
        
    individual_pdfs, failed_links = convert_urls_to_pdfs(urls, config)
    
    if failed_links:
        print("\n--- Summary of Failed Links ---")
        for link in failed_links:
            print(f"- {link}")
        print("---------------------------------")
        
    merge_pdfs(individual_pdfs, OUTPUT_PDF)
    cleanup(individual_pdfs)
    
    end_time = time.time()
    print(f"\nProcess finished in {end_time - start_time:.2f} seconds.")

if __name__ == '__main__':
    main()
