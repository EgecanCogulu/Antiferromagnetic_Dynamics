# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:45:25 2020

@author: Egecan
"""

import cv2
import os
import numpy as np

folder=r"gif2\\"
image_folder = r'C:\Users\Egecan\Desktop\YZ\\'
video_name =r'C:\Users\Egecan\Desktop\YZScan.mp4'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images = list(np.sort(images))
# images = list(np.sort(images*10))

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 30, (int(width),int(height)))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()


 