import cv2
import os
import numpy as np

src_dir = 'C:/Users/sunhaokai/Desktop/3&c'
out_dir = 'test'
pic_paths = os.listdir(src_dir)
for i in pic_paths:
    img = cv2.imread(src_dir + '/' + str(i))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2 = np.zeros_like(img)
    img2[:, :, 0] = gray
    img2[:, :, 1] = gray
    img2[:, :, 2] = gray
    cv2.imwrite(out_dir+ '/' + i, img2)