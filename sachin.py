import cv2
from PIL import Image
import numpy as np

maskPath = "images/sachin.png"
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
mask = Image.open(maskPath)

def thug_mask(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
	faces = faceCascade.detectMultiScale(gray, 2)	
	background = Image.fromarray(image)
	for (x,y,w,h) in faces:
		resized_mask = mask.resize( (w + 600 , h + 250) , Image.ANTIALIAS )
		offset = (x - 290, y - 50  )
		background.paste(resized_mask, offset, mask = resized_mask)
	return np.asarray(background)

cap = cv2.VideoCapture(cv2.CAP_ANY)

while True:
	ret, frame = cap.read()
	frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
	if ret == True:
		cv2.imshow('Live',  cv2.cvtColor( thug_mask(cv2.flip(frame, 1)), cv2.COLOR_RGB2BGR) )
		if cv2.waitKey(1) == 27:
			break
cap.release()
cv2.destroyAllWindows()