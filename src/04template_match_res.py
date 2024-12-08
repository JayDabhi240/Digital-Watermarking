import os
import cv2
import numpy as np

template = cv2.imread('images\\watermark.jpg', 0)

path = "images/regenerated_watermarks"
fileList=os.listdir(path)
numberOfImages=len(fileList)

for k in range(0, numberOfImages):
    img_gray = cv2.imread('images\\regenerated_watermarks\\watermark_img_'+str(k)+'.jpg', 0)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    print(res)
