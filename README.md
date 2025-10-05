<div align="center">

# PAGEBINDER

**A URL to PDF Converter**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.md)
[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![wkhtmltopdf](https://img.shields.io/badge/wkhtmltopdf-Required-orange.svg)](https://wkhtmltopdf.org/)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](https://github.com/FoldedOdin/PageBinder)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](https://github.com/FoldedOdin/PageBinder)

</div>

##  About

A **simple yet powerful Python script** that fetches a list of URLs from a text file, converts each web page to a PDF, and merges them into a single, clean document. Perfect for archiving web content, creating offline documentation, or compiling research materials.

##  Features

###  Batch Processing
- **Bulk Conversion** - Process multiple URLs in one operation
- **Fast Processing** - Efficient handling of large URL lists
- **Simple Input** - Just a text file with URLs

###  Smart Merging
- **Single Output** - Combines all PDFs into one document
- **Clean Results** - Professional-looking merged PDFs
- **Organized** - Maintains URL order from input file

### Robust Error Handling
- **Graceful Failures** - Continues processing even if URLs fail
- **Detailed Summary** - Shows which URLs failed and why
- **Error Logging** - Tracks issues for troubleshooting
- **Auto Cleanup** - Removes temporary files automatically

### Simple & Lightweight
- **Minimal Dependencies** - Only 2 Python packages required
- **Easy Setup** - Quick installation and configuration
- **Cross-Platform** - Works on Windows, macOS, and Linux

## Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![wkhtmltopdf](https://img.shields.io/badge/wkhtmltopdf-orange?style=for-the-badge&logo=pdf&logoColor=white)

**Libraries Used:**
![pdfkit](https://img.shields.io/badge/pdfkit-Latest-blue?logo=python&logoColor=white)
![pypdf](https://img.shields.io/badge/pypdf-Latest-green?logo=python&logoColor=white)

</div>

## Getting Started

### Prerequisites

Before you begin, ensure you have:

- ![Python](https://img.shields.io/badge/Python-3.7+-3776AB?logo=python&logoColor=white) (v3.7 or higher)
- ![wkhtmltopdf](https://img.shields.io/badge/wkhtmltopdf-Required-orange.svg) (command-line tool)

### Installation

#### Step 1: Install wkhtmltopdf (MANDATORY)

This script uses `wkhtmltopdf` to render HTML into PDF. **You must install this dependency first.**

<details>
<summary><b>Windows Installation</b></summary>

1. Download the installer from [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html)
2. Run the installer (default: `C:\Program Files\wkhtmltopdf`)
3. Find the executable path: `C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe`
4. **Update `WKHTMLTOPDF_PATH` in the script** with this full path

```python
WKHTMLTOPDF_PATH = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
```

</details>

<details>
<summary><b>macOS Installation (Homebrew)</b></summary>

1. Install Homebrew if you haven't already:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Install wkhtmltopdf:
```bash
brew install wkhtmltopdf
```

3. Update the script:
```python
WKHTMLTOPDF_PATH = '/usr/local/bin/wkhtmltopdf'
```

</details>

<details>
<summary><b>Linux Installation (Debian/Ubuntu)</b></summary>

1. Update package list and install:
```bash
sudo apt-get update
sudo apt-get install wkhtmltopdf
```

2. Update the script:
```python
WKHTMLTOPDF_PATH = '/usr/bin/wkhtmltopdf'
```

</details>

#### Step 2: Install Python Libraries

Install the required Python packages:

```bash
pip install pdfkit pypdf
```

Or use requirements.txt:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

1️⃣ **Create input file**: Create a `links.txt` file in the same directory as the script

2️⃣ **Add URLs**: Add your desired URLs to the file, **one URL per line**

```text
https://example.com/page1
https://example.com/page2
https://example.com/page3
```

3️⃣ **Run the script**:

```bash
python html_to_pdf_converter.py
```

4️⃣ **Get your PDF**: Find your merged PDF as `combined_output.pdf` in the project directory

### Output

The script will:
- ✅ Create a `temp_pdfs` directory for temporary files
- 🔄 Process each URL and convert to PDF
- 📊 Display progress in the console
- 📄 Merge all PDFs into `combined_output.pdf`
- 🧹 Clean up temporary files automatically
- 📋 Show summary of failed URLs (if any)

### Example Output

```bash
Processing: https://example.com/page1
✓ Successfully converted: page1.pdf
Processing: https://example.com/page2
✓ Successfully converted: page2.pdf
Processing: https://example.com/page3
✗ Failed to convert: page3.pdf (Timeout)

=================================
Conversion Summary
=================================
✓ Successful: 2
✗ Failed: 1
📄 Output: combined_output.pdf
```

## 🏗️ Project Structure

```
📦 PageBinder/
├── 📄 html_to_pdf_converter.py    # Main script
├── 📄 links.txt                   # Input URLs (create this)
├── 📄 requirements.txt            # Python dependencies
├── 📄 combined_output.pdf         # Final merged PDF (generated)
├── 📁 temp_pdfs/                  # Temporary PDF storage (auto-cleaned)
├── 📄 LICENSE                     # MIT License
└── 📄 README.md                   # You are here
```

## ⚙️ Configuration

### Script Variables

You can customize these variables in `html_to_pdf_converter.py`:

```python
# Path to wkhtmltopdf executable
WKHTMLTOPDF_PATH = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

# Input file location containing URLs 
INPUT_FILE = 'links.txt'

# Output PDF filename
OUTPUT_PDF = 'combined_output.pdf'

# Temporary directory for individual PDFs
TEMP_DIR = 'temp_pdfs'
```

### PDF Options

Customize PDF conversion options:

```python
options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None
}
```

## 🔧 Troubleshooting

### Common Issues

<details>
<summary><b>❌ "wkhtmltopdf not found" error</b></summary>

**Solution**: Make sure you've installed wkhtmltopdf and updated the `WKHTMLTOPDF_PATH` variable with the correct path to the executable.

</details>

<details>
<summary><b>❌ "No module named 'pdfkit'" error</b></summary>

**Solution**: Install the required Python libraries:
```bash
pip install pdfkit pypdf
```

</details>

<details>
<summary><b>⚠️ Some URLs fail to convert</b></summary>

**Possible causes**:
- URL requires authentication
- Website blocks automated access
- Page has JavaScript that doesn't load properly
- Network timeout

**Solution**: Check the failed URLs list at the end of execution. You may need to manually download these pages.

</details>

<details>
<summary><b>🐌 Slow conversion speed</b></summary>

**Solution**: Large pages with many images take longer. Consider:
- Processing fewer URLs at once
- Using a faster internet connection
- Disabling image loading in options (if text-only is acceptable)

</details>

## 🧪 Testing

Test with a small sample first:

```bash
# Create a test file with 2-3 URLs
echo "https://example.com" > test_links.txt
echo "https://wikipedia.org" >> test_links.txt

# Update INPUT_FILE in script to 'test_links.txt'
python html_to_pdf_converter.py
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

<div align="center">

[![Issues](https://img.shields.io/github/issues/yourusername/pagebinder)](https://github.com/yourusername/pagebinder/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/yourusername/pagebinder)](https://github.com/yourusername/pagebinder/pulls)

</div>

### How to Contribute

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 📥 Open a Pull Request

## 📝 Roadmap

- [ ] Add progress bar for batch conversions
- [ ] Support for custom page sizes and orientations
- [ ] GUI interface for easier use
- [ ] Docker container for easy deployment
- [ ] Support for authentication-required URLs
- [ ] Custom headers and footers
- [ ] Table of contents generation

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE.md) file for details.

<div align="center">

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

##  Acknowledgments

<div align="center">

Special thanks to these amazing projects:

[![Python](https://img.shields.io/badge/Thanks-Python%20Community-3776AB?logo=python&logoColor=white)](https://python.org)
[![wkhtmltopdf](https://img.shields.io/badge/Thanks-wkhtmltopdf%20Team-orange?logo=pdf&logoColor=white)](https://wkhtmltopdf.org)
[![pdfkit](https://img.shields.io/badge/Thanks-pdfkit%20Maintainers-blue?logo=python&logoColor=white)](https://pypi.org/project/pdfkit/)

</div>

## Connect & Support

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?logo=github&logoColor=white)](https://github.com/FoldedOdin)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?logo=gmail&logoColor=white)](mailto:karthikkpradeep123@gmail.com)

</div>

### Need Help?

- 💬 **Issues**: [Open an issue](https://github.com/FoldedOdin/PageBinder/issues)
- 📖 **Wiki**: [Check documentation](https://github.com/FoldedOdin/PageBinder/wiki)

---

<div align="center">

**🎯 Built with ❤️ for web content archiving**

![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red.svg)
![Open Source](https://img.shields.io/badge/Open%20Source-💙-blue.svg)
![Python](https://img.shields.io/badge/Python-💛-yellow.svg)

### ⭐ If you found this project helpful, please give it a star!

[![🚀 Return To TOP](https://img.shields.io/badge/🚀%20Return%20to-%20TOP-FF6B6B?style=for-the-badge&labelColor=4ECDC4)](#pagebinder)

</div>
