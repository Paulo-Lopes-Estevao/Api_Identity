#import PIL
import cv2
import easyocr
#import numpy as np
#from PIL import Image, ImageDraw

""" IMAGE_PATH = 'img/BI_Dercio.JPG'
img = PIL.Image.open(IMAGE_PATH) """

img = cv2.imread('img/BI_Dercio.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction
edged = cv2.Canny(bfilter, 30, 200) #Edge detection
myImg = cv2.cvtColor(bfilter, cv2.COLOR_BGR2RGB)

reader = easyocr.Reader(['pt', 'en'], gpu=False)
result = reader.readtext(myImg)
print(result)
# print(img.shape)


# print(f'Data: {data["value"][0]} -- Prob: {data["prob"][0]:.2f}')

# while True:
#   cv2.imshow("Image", myImg)
#   if cv2.waitKey(1) & 0xFF==27:
#     break
# cv2.destroyAllWindows()
