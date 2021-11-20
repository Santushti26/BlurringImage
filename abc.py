import cv2
import numpy as np

img=cv2.imread("ironman.png")
img=cv2.resize(img,dsize=(480,480))

#converting to grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#blurring the image
blur=cv2.medianBlur(gray,5)


#detecting edges
edges=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
#adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst])
cv2.imshow("Edges", edges)


#smoothning original image

cv2.waitKey(0)
cv2.destroyAllWindows()
