# 🧠 Tesseract Batch OCR Tool

This project is a Python-based OCR (Optical Character Recognition) tool that processes all root-level images in a folder and extracts text using [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).  
The extracted text is saved as `.txt` files in a separate output directory, preserving the original filenames.

---

## 📌 Features

- ✅ Batch OCR processing of images in a folder  
- ✅ Outputs `.txt` files with the same name as the input image  
- ✅ Supports common image formats: `.png`, `.jpg`, `.jpeg`, `.bmp`, `.tiff`, `.webp`  
- ✅ Handles errors per image with summary report  
- ✅ Windows, macOS, and Linux compatible

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/batch-ocr-tesseract.git
cd batch-ocr-tesseract

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
# or manually 
pip install pytesseract Pillow 

# Install Tesseract OCR Engine

https://github.com/tesseract-ocr/tessdoc/tree/main#binaries

⚠️ On Windows, update the path in batch_ocr.py:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"





