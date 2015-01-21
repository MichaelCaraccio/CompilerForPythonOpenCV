# Projet
## EXEMPLE 1
Charger un dossier contenant des images et afficher les images du dossier
```
LOAD_SRC mondossier ./dossier1
SAVE_DEST dossierDestination ./save

for file in mondossier
	DISPLAY file
```

## EXEMPLE 2
Charger un dossier contenant des images et transformer en noire et blanc les images qui ont pour extension « png »
```
LOAD_SRC mondossier ./dossier1
SAVE_DEST dossierDestination ./save

for file in mondossier
	if file EXTENSION == « png »
		TRANSFORM file BLACKANDWHITE
```

## EXEMPLE 3
Charger uniquement une image et lui appliquer une matrice de transformation quelconque
```
LOAD_SRC monimage image.png
SAVE_DEST madestination imageDest.png

MATRIX matrice3x3 = [[0,0,1],[0,0,-1],[0,0,-1]]
TRANSFORM monimage matrice3x3
```

