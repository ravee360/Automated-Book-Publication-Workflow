import os
import pytesseract
from PIL import Image

# Set path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Set path to tessdata folder (should point to the tessdata directory)
os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"

# Load the image
image = Image.open("screenshots/chapter1_full_clean.png")

# Extract text using OCR
text = pytesseract.image_to_string(image)

# Save the output to Scraper/text folder
output_dir = os.path.join("text")
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "chapter1_ocr_extracted.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"✅ OCR text saved to: {output_path}")
