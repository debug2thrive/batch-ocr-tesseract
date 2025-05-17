import os
import platform
from PIL import Image
import pytesseract

# ====== Configuration ======

# Folder where input images are stored (only root-level files will be processed)
INPUT_FOLDER = "images"

# Folder where OCR output .txt files will be saved
OUTPUT_FOLDER = "ocr_output"

# ====== Set Tesseract executable path (only needed for Windows) ======
# If you're on Windows, make sure this path matches your Tesseract installation directory
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Set of allowed image file extensions
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".webp"}

# ====== Check if input folder exists ======
if not os.path.exists(INPUT_FOLDER):
    raise FileNotFoundError(f"Input folder '{INPUT_FOLDER}' does not exist.")

# ====== Create output folder if it doesn't exist ======
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ====== Initialize counters ======
total, success, failed = 0, 0, 0

# ====== Loop through each file in the input folder ======
for filename in os.listdir(INPUT_FOLDER):
    name, ext = os.path.splitext(filename)

    # Only process supported image files
    if ext.lower() in IMAGE_EXTENSIONS:
        total += 1

        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, f"{name}.txt")

        try:
            # Load the image using PIL
            image = Image.open(input_path)

            # Run OCR on the image
            text = pytesseract.image_to_string(image, lang='eng')

            # Write the extracted text to a .txt file with the same name
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)

            # Report success
            print(f"✅ Processed: {filename} → {output_path}")
            success += 1

        except Exception as e:
            # Handle and report any errors per file
            print(f"❌ Failed: {filename} - Error: {e}")
            failed += 1

# ====== Final summary ======
print(f"\nSummary: {success}/{total} files processed successfully, {failed} failed.")
