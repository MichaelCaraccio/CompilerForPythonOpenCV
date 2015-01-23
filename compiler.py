import AST as AST
from AST import addToClass

fileName = ''
pathLoad = ''
pathDest = ''
isDisplayed = False
tabulation = ""
matrix = ""
currentFolder = ''


# noeud de programme
# retourne la suite d'opcodes de tous les enfants
@addToClass(AST.ProgramNode)
def compile(self):
    pythonCode = ""
    global isDisplayed
    for c in self.children:
        pythonCode += str(c.compile())
    if isDisplayed:
        pythonCode += "plt.show()"
    return pythonCode

# noeud terminal
# si c'est une variable : empile la valeur de la variable
# si c'est une constante : empile la constante
@addToClass(AST.TokenNode)
def compile(self):
    pythonCode = ""
    if isinstance(self.tok, str):
        pythonCode += self.tok
    else:
        pythonCode += self.tok
    return pythonCode

@addToClass(AST.AssignNode)
def compile(self):
    pythonCode = ""
    pythonCode += self.children[1].compile()
    pythonCode += self.children[0].tok
    return pythonCode

@addToClass(AST.LoadNode)
def compile(self):

    global fileName, pathLoad

    pythonCode = ""
    pythonCode += "import cv2\n"
    pythonCode += "import os\n"
    pythonCode += "import numpy as np\n"
    pythonCode += "from matplotlib import pyplot as plt\n\n"

    file = str(self.children[1]).replace('\n', '')
    pythonCode += "LOAD_SRC = \"" + file + "\"\n"

    fileName = 'filename'
    pathLoad = file

    return pythonCode

@addToClass(AST.SaveNode)
def compile(self):

    global pathDest

    pythonCode = ""

    file = str(self.children[1]).replace('\n', '')
    pythonCode += "SAVE_SRC = \"" + file + "\"\n\n"

    pathDest = file
    return pythonCode

@addToClass(AST.ForNode)
def compile(self):
    global fileName
    global tabulation
    fileName = 'filename'
    pythonCode = ""
    pythonCode += "compteur = 1\n\n"
    pythonCode += tabulation.join("for filename in os.listdir(LOAD_SRC):\n")
    tabulation = tabulation + '\t'
    return pythonCode

@addToClass(AST.IfNode)
def compile(self):
    pythonCode = ""
    global tabulation
    extension = str(self.children[0].children[1]).replace('\n', '')
    pythonCode += str(tabulation) + "if filename.endswith(" + extension + "):\n"
    tabulation= tabulation + '\t'
    return pythonCode

@addToClass(AST.MatrixNode3)
def compile(self):
    global matrix
    matrix = self.children[0].children[1]
    return ''

@addToClass(AST.MatrixNode5)
def compile(self):
    global matrix
    matrix = self.children[0].children[1]
    return ''

@addToClass(AST.TransformNode)
def compile(self):
    global matrix, currentFolder
    img = "img = cv2.imread(\"" + pathLoad + "/" + "\" + " + fileName + ")\n"
    kernel = "kernel = np.matrix(" + str(matrix).replace('\n', '') + ")"
    dest = "img = cv2.filter2D(img, -1, kernel)"
    write = "cv2.imwrite(\"" + pathDest + "/" + "\" + " + fileName + ", img)\n"
    pythonCode = str(tabulation) + img + str(tabulation) + kernel + "\n" + str(tabulation) + dest + "\n" + str(tabulation) + write + "\n"
    currentFolder = pathDest
    return pythonCode

@addToClass(AST.DisplayNode)
def compile(self):
    global isDisplayed, fileName, pathLoad, currentFolder
    isDisplayed = True

    if(currentFolder == ''):
        currentFolder = pathLoad

    pythonCode = ""
    pythonCode += str(tabulation) + "img = cv2.imread(\"" + currentFolder + "/" + "\" + " + str(fileName) + ")\n"
    pythonCode += str(tabulation) + "b, g, r = cv2.split(img)     # get b, g, r\n"
    pythonCode += str(tabulation) + "img = cv2.merge([r, g, b])     # switch it to rgb\n"

    pythonCode += str(tabulation) + "plt.subplot(2, 3, compteur)\n"
    pythonCode += str(tabulation) + "plt.imshow(img)\n"
    pythonCode += str(tabulation) + "plt.title(filename)\n"

    pythonCode += str(tabulation) + "plt.xticks([])\n"
    pythonCode += str(tabulation) + "plt.yticks([])\n"

    pythonCode += str(tabulation) + "compteur += 1\n"

    return pythonCode


if __name__ == "__main__":
    from parser import parse
    import sys
    import os
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    compiled = ast.compile()
    name = os.path.splitext(sys.argv[1])[0] + '.py'
    outfile = open(name, 'w')
    outfile.write(compiled)
    outfile.close()
    print ("Wrote output to", name)