import cv2
import os
from matplotlib import pyplot as plt
LOAD_SRC="C:/csa2"
SAVE_SRC="C:/csa"
for filename in os.listdir(LOAD_SRC):
	if filename.endswith():
		plt.subplot(2,3,1),plt.imshow(filename),plt.title(1)
		plt.xticks([]),plt.yticks([])
img = cv2.imread('filename')
kernel = np.matrix('[{0,0,1},{0,0,-1},{0,2,3}]')
cv2.filter2D(img,-1,kernel)
plt.show()