import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

LOAD_SRC = "/Users/michaelcaraccio/Desktop/images/sources"
SAVE_SRC = "/Users/michaelcaraccio/Desktop/images/dest"

compteur = 1

for filename in os.listdir(LOAD_SRC):
	if filename.endswith('jpg'):
		img = cv2.imread("/Users/michaelcaraccio/Desktop/images/sources/" + filename)
		kernel = np.matrix('[[-1, -1, -1],[-1, 8, -1],[-1, -1, -1]]')
		img = cv2.filter2D(img, -1, kernel)
		cv2.imwrite("/Users/michaelcaraccio/Desktop/images/dest/" + filename, img)

		img = cv2.imread("/Users/michaelcaraccio/Desktop/images/dest/" + filename)
		b, g, r = cv2.split(img)     # get b, g, r
		img = cv2.merge([r, g, b])     # switch it to rgb
		plt.subplot(2, 3, compteur)
		plt.imshow(img)
		plt.title(filename)
		plt.xticks([])
		plt.yticks([])
		compteur += 1
plt.show()