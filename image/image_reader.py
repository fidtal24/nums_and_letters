import cv2
import pytesseract
from gocr import gocr

def load_gray_image():
	image = cv2.imread('/home/tal/Documents/Friday/nums/image/1.jpg')

	if image is None:
		print('Error: Unsupported image format')

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	return gray

def read_from_image_tesseract(image):
	text = pytesseract.image_to_string(image, lang="heb")
	return text

def read_from_image_gocr(image):
	text = gocr(image)
	return text

if __name__ == "__main__":
	image = load_gray_image()
	text = read_from_image_gocr(image)
	print(text)