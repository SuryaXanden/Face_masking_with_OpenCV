import cv2
from PIL import Image
import numpy as np
maskPath = "bean_ani.png"
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
mask = Image.open(maskPath) 
def thug_mask(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray, 3)
	background = Image.fromarray(image)
	for (x,y,w,h) in faces:
		resized_mask = mask.resize( (w + 100 , h + 100) , Image.ANTIALIAS )
		offset = (x - 50, y + 82 )
		background.paste(resized_mask, offset, mask=resized_mask)
	return np.asarray(background)
cap = cv2.VideoCapture(cv2.CAP_ANY)
while True:
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Live', cv2.flip( thug_mask( frame ) , 1) )
        if cv2.waitKey(1) == 27:
            break
cap.release()
cv2.destroyAllWindows()