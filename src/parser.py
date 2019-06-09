from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Simple image to string
print(pytesseract.image_to_string(Image.open('3.png'), lang='eng'))
