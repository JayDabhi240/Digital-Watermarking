import cv2
import random
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

og_img = cv2.imread('images\\original_image.jpg',0)
watermark_img = cv2.imread('images\\watermark.jpg', 0)
ret,watermark_img = cv2.threshold(watermark_img,127,255,cv2.THRESH_BINARY)


img_height,img_width=og_img.shape[:2]
watermark_height,watermark_width=watermark_img.shape[:2]
img_size = img_height * img_width
watermark_size = watermark_height * watermark_width



master_img = np.zeros((watermark_height, watermark_width, 1), np.uint8)
owner_img = np.zeros((watermark_height, watermark_width, 1), np.uint8)

random.seed(a=KEY)
random_points = random.sample(range(img_size), watermark_size)

i = 0
j = 0

for k in random_points:
    x = int(k / img_width)
    y = int(k % img_width)
    if mean_neighbour(og_img, x, y) > THRESH:
        master_img[i,j] = 255
    j += 1
    if j == watermark_width:
        j = 0
        i += 1

for i in range(0, watermark_height):
    for j in range(0, watermark_width):
        owner_img[i, j] = xor(master_img[i, j], watermark_img[i, j])



cv2.imshow('M', master_img)
cv2.imshow('O', owner_img)
cv2.imwrite('images\\master_img.jpg', master_img)
cv2.imwrite('images\\owner_img.jpg', owner_img)
cv2.waitKey(0)
cv2.destroyAllWindows()