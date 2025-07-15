import os
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"

image = Image.open("screenshots/chapter1_full_clean.png")

text = pytesseract.image_to_string(image)

output_dir = os.path.join("text")
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "chapter1_ocr_extracted.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"✅ OCR text saved to: {output_path}")
