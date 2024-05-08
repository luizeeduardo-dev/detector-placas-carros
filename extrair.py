import cv2
import pytesseract

def extrairTextoDaPlaca(image):
    _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    binary_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return pytesseract.image_to_string(binary_image, lang='por')