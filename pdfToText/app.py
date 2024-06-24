import pytesseract
from PIL import Image

def image_to_text(image_path):
    try:
        # Extract text from image using Tesseract OCR
        print(pytesseract.image_to_string(image_path))
        text = pytesseract.image_to_string(Image.open(image_path))
        return text
    except Exception as e:
        print("An error occurred during text extraction:", e)
        return None

# Specify the path to your image
image_path = "cow.jpg"

# Extract text from the image
text_from_image = image_to_text(image_path)

if text_from_image is not None:
    print("\nText extracted from image:")
    print(text_from_image)
else:
    print("\nText extraction failed.")
