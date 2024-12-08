import os
import cv2
import random
import numpy as np

KEY = 1001
THRESH = 75

def mean_neighbour(img, x, y):
    val = 0  # Initialize as an integer
    num = 0
    img_height,img_width=img.shape[:2]
    
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1), (0, 0), (0, 1),
                   (1, -1), (1, 0), (1, 1)]:
        i, j = x + dx, y + dy
        if 0 <= i < img_height and 0 <= j < img_width:
            val += int(img[i, j])  # Explicitly cast to int to prevent overflow
            num += 1
    
    return val / float(num)  # Return mean as float


watermark_img = cv2.imread('images\\watermark.jpg', 0)
watermark_height,watermark_width=watermark_img.shape[:2]
watermark_size = watermark_height * watermark_width



path = "images/stolen_images"
fileList=os.listdir(path)
numberOfImages=len(fileList)

for cnt in range(0, numberOfImages):
    stolen_img = cv2.imread('images\\stolen_images\\stolen_image_'+str(cnt)+'.jpg',0)

    img_height,img_width=stolen_img.shape[:2]
    img_size = img_height * img_width

    master_img = np.zeros((watermark_width, watermark_height, 1), np.uint8)

    random.seed(a=KEY)
    random_points = random.sample(range(img_size), watermark_size)

    i = 0
    j = 0

    for k in random_points:
        x = int(k / img_width)
        y = int(k % img_width)
        if mean_neighbour(stolen_img, x, y) > THRESH:
            master_img[i,j] = 255
        j += 1
        if j == watermark_width:
            j = 0
            i += 1

    cv2.imwrite('images\\master_images\\master_img_'+str(cnt)+'.jpg', master_img)
    print(cnt)

print("Done")