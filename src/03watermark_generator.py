import os
import cv2
import numpy as np

KEY = 1001
THRESH = 75

def xor(x ,y):
    if x == 0 and y == 0:
        return 0
    elif x == 0 and y != 0:
        return 255
    elif x != 0 and y == 0:
        return 255
    elif x !=0 and y != 0:
        return 0


watermark_img = cv2.imread('images\\watermark.jpg', 0)
owner_img = cv2.imread('images\\owner_img.jpg', 0)

watermark_height,watermark_width=watermark_img.shape[:2]
watermark_size = watermark_height * watermark_width


path = "images/master_images"
fileList=os.listdir(path)
numberOfImages=len(fileList)

for k in range(0, numberOfImages):
    master_img = cv2.imread('images\\master_images\\master_img_'+str(k)+'.jpg', 0)
    watermark_img = np.zeros((watermark_width, watermark_height, 1), np.uint8)

    i = 0
    j = 0

    for i in range(0, watermark_height):
        for j in range(0, watermark_width):
            watermark_img[i, j] = xor(master_img[i, j], owner_img[i, j])

    watermark_img = (255-watermark_img)
    kernel = np.ones((4,4),np.uint8)
    watermark_img = cv2.medianBlur(watermark_img, 3)
    watermark_img = cv2.morphologyEx(watermark_img, cv2.MORPH_OPEN, kernel)
    watermark_img = cv2.morphologyEx(watermark_img, cv2.MORPH_CLOSE, kernel)
    watermark_img = (255-watermark_img)

    cv2.imwrite('images\\regenerated_watermarks\\watermark_img_'+str(k)+'.jpg', watermark_img)
    print(k)
print("Done")