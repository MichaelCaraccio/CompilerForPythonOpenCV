import cv2
import os
from matplotlib import pyplot as plt

LOAD_SRC = "/Users/michaelcaraccio/Desktop/images/sources"
SAVE_SRC = "/Users/michaelcaraccio/Desktop/images/dest"

compteur = 1

for filename in os.listdir(LOAD_SRC):
	img = cv2.imread("/Users/michaelcaraccio/Desktop/images/sources/" + filename)
	b, g, r = cv2.split(img)     # get b, g, r
	img = cv2.merge([r, g, b])     # switch it to rgb
	plt.subplot(2, 3, compteur)
	plt.imshow(img)
	plt.title(filename)
	plt.xticks([])
	plt.yticks([])
	compteur += 1
plt.show()