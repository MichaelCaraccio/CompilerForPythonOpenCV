# Projet
## EXEMPLE 1
Charger un dossier contenant des images et afficher les images du dossier
```
LOAD_SRC mondossier /Users/michaelcaraccio/Desktop/images/sources;
SAVE_DEST dossierDestination /Users/michaelcaraccio/Desktop/images/dest;

for file in mondossier
	DISPLAY file
```

Le compilateur va générer le code suivant :
```
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
```

Si l'on compile le fichier python et que l'on l'execute, nous obtenons ceci :
![image result 1](https://raw.githubusercontent.com/MichaelCaraccio/CompilerForPythonOpenCV/master/images/compilation_result_1.png)


## EXEMPLE 2
Charger un dossier contenant des images et appliquer une convolution (détection de contour) pour les fichiers avec comme extension jpg, puis afficher les images. Les images convoluées se trouveront dans le dossier destination
```
LOAD_SRC mondossier /Users/michaelcaraccio/Desktop/images/sources;
SAVE_DEST dossierDestination /Users/michaelcaraccio/Desktop/images/dest;

for file in mondossier;
    if EXTENSION file == jpg;
		matrix3 blup = [[-1, -1, -1],[-1, 8, -1],[-1, -1, -1]];
		TRANSFORM file matrice3x3;
		DISPLAY file
```

Le compilateur va générer le code suivant :
```
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
```

Si l'on compile le fichier python et que l'on l'execute, nous obtenons ceci :
![image result 2](https://raw.githubusercontent.com/MichaelCaraccio/CompilerForPythonOpenCV/master/images/compilation_result_2.png)


## EXEMPLE 3
Charger uniquement une image et lui appliquer une matrice de transformation quelconque
```
LOAD_SRC monimage image.png
SAVE_DEST madestination imageDest.png

MATRIX matrice3x3 = [[0,0,1],[0,0,-1],[0,0,-1]]
TRANSFORM monimage matrice3x3
```

