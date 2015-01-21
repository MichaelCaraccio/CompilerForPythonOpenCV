import CompilerForPythonOpenCV.AST as AST
from CompilerForPythonOpenCV.AST import addToClass

fileName = ''
isDisplayed = False
tabulation = ""
compteur = 0
matrix = ""


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
    global fileName
    pythonCode = ""
    pythonCode += "import cv2\n"
    pythonCode += "import os\n"
    pythonCode += "from matplotlib import pyplot as plt\n"
    file = str(self.children[1]).replace('\n','')
    pythonCode += "LOAD_SRC=\""+file+ "\"\n"
    fileName = pythonCode
    return pythonCode

@addToClass(AST.SaveNode)
def compile(self):
    pythonCode = ""
    file = str(self.children[1]).replace('\n','')
    pythonCode += "SAVE_SRC=\""+file+ "\"\n"
    return pythonCode

@addToClass(AST.ForNode)
def compile(self):
    global fileName
    global tabulation
    fileName = 'filename'
    pythonCode = ""
    pythonCode += tabulation.join("for filename in os.listdir(LOAD_SRC):\n")
    tabulation = tabulation+'\t'
    return pythonCode

@addToClass(AST.IfNode)
def compile(self):
    pythonCode = ""
    global tabulation
    extension = str(self.children[0].children[1]).replace('\n','')
    pythonCode += str(tabulation)+"if filename.endswith(""):\n"
    tabulation= tabulation+'\t'
    return pythonCode

@addToClass(AST.MatrixNode3)
def compile(self):
    global matrix
    matrix = self.children[0].children[1]
    return ""

@addToClass(AST.MatrixNode4)
def compile(self):
    global matrix
    matrix = self.children[0].children[1]
    return ""

@addToClass(AST.TransformNode)
def compile(self):
    global matrix
    img = "img = cv2.imread('"+fileName+"')"
    kernel = "kernel = np.matrix("+str(matrix).replace('\n','')+ ")"
    dest = "cv2.filter2D(img,-1,kernel)"
    pythonCode = img + "\n" + kernel + "\n" + dest + "\n"
    return pythonCode

@addToClass(AST.DisplayNode)
def compile(self):
    global isDisplayed
    global fileName
    isDisplayed = True
    compteur = 1
    pythonCode = ""
    pythonCode += str(tabulation)+"plt.subplot(2,3,"+str(compteur)+"),plt.imshow("+str(fileName)+"),plt.title("+str(compteur)+")\n"
    pythonCode += str(tabulation)+"plt.xticks([]),plt.yticks([])\n"
    return pythonCode


if __name__ == "__main__":
    from CompilerForPythonOpenCV.parser import parse
    import sys
    import os
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    compiled = ast.compile()
    name = os.path.splitext(sys.argv[1])[0]+'.py'
    outfile = open(name, 'w')
    outfile.write(compiled)
    outfile.close()
    print ("Wrote output to", name)