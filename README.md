# Projet
## EXEMPLE 1
Charger un dossier contenant des images et afficher les images du dossier
```
LOAD_SRC mondossier ./dossier1
SAVE_DEST dossierDestination ./save

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
Charger un dossier contenant des images et transformer en noire et blanc les images qui ont pour extension « png »
```
LOAD_SRC mondossier ./dossier1
SAVE_DEST dossierDestination ./save

for file in mondossier
	if file EXTENSION == "png"
		MATRIX matrice3x3 = [[0,0,1],[0,0,-1],[0,0,-1]]
		TRANSFORM file matrice3x3
```

## EXEMPLE 3
Charger uniquement une image et lui appliquer une matrice de transformation quelconque
```
LOAD_SRC monimage image.png
SAVE_DEST madestination imageDest.png

MATRIX matrice3x3 = [[0,0,1],[0,0,-1],[0,0,-1]]
TRANSFORM monimage matrice3x3
```

