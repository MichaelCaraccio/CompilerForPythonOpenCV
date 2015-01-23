import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

LOAD_SRC = "/Users/michaelcaraccio/Desktop/images/sources"
SAVE_SRC = "/Users/michaelcaraccio/Desktop/images/dest"

compteur = 1

for filename in os.listdir(LOAD_SRC):
	img = cv2.imread("/Users/michaelcaraccio/Desktop/images/sources/" + filename)
	kernel = np.matrix('[[0.4,0.3,0.2,0,0],[0.3,0.2,0.1,0,0],[0.2,0.1,1,-0.1,-0.2],[0,0,-0.1,-0.2,-0.3],[0,0,-0.2,-0.3,-0.4]]')
	img = cv2.filter2D(img, -1, kernel)
	cv2.imwrite("/Users/michaelcaraccio/Desktop/images/dest/" + filename, img)

