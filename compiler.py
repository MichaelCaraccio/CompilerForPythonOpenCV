import CompilerForPythonOpenCV.AST as AST
from CompilerForPythonOpenCV.AST import addToClass
from matplotlib import pyplot as plt


fileName = ''
isDisplayed = False


# noeud de programme
# retourne la suite d'opcodes de tous les enfants
@addToClass(AST.ProgramNode)
def compile(self):
	pythonCode = ""
	for c in self.children:
		pythonCode += str(c.compile())
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

# noeud d'assignation de variable
# exécute le noeud à droite du signe =
# dépile un élément et le met dans ID
@addToClass(AST.AssignNode)
def compile(self):
	pythonCode = ""
	pythonCode += self.children[1].compile()
	pythonCode += self.children[0].tok
	return pythonCode

@addToClass(AST.PrintNode)
def execute(self):
    print (self.children[0].compile())
    
@addToClass(AST.WhileNode)
def compile(self):
    while self.children[0].execute():
        self.children[1].compile()

@addToClass(AST.LoadNode)
def compile(self):
   print("import cv2")
   print("import os")
   pythonCode = str(self.children[1]).replace('\n','')
   print("LOAD_SRC=\""+pythonCode+ "\"")
   fileName = pythonCode

#@addToClass(AST.FileNode)
#def execute(self):
    #print(str(self.children[0])+"\"")

@addToClass(AST.SaveNode)
def compile(self):
    pythonCode = str(self.children[1]).replace('\n','')
    print("SAVE_SRC=\""+pythonCode+ "\"")

tabulation = ''
compteur = 0

@addToClass(AST.ForNode)
def compile(self):
    global fileName
    fileName = 'filename'
    print(tabulation,"for filename in os.listdir(LOAD_SRC):")
    global tabulation
    tabulation = tabulation.join('\t')

@addToClass(AST.IfNode)
def compile(self):

    pythonCode = str(self.children[0].children[1]).replace('\n','')
    print(tabulation,"if filename.endswith("+pythonCode+"):")
    global tabulation
    tabulation = tabulation.join('\t')

@addToClass(AST.MatrixNode3)
def compile(self):
    return

@addToClass(AST.MatrixNode4)
def compile(self):
    return

@addToClass(AST.TransformNode)
def compile(self):
    return

@addToClass(AST.DisplayNode)
def compile(self):
    global isDisplayed
    isDisplayed = True
    global fileName
    compteur = 1
    plt.subplot(2,3,compteur),plt.imshow(fileName),plt.title(compteur)
    plt.xticks([]),plt.yticks([])
    plt.show()


if __name__ == "__main__":
    from CompilerForPythonOpenCV.parser import parse
    import sys
    import os
    global isDisplayed
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    compiled = ast.compile()
    if isDisplayed:
        compile += 'plt.show()'
    name = os.path.splitext(sys.argv[1])[0]+'.py'
    outfile = open(name, 'w')
    outfile.write(compiled)
    outfile.close()
    print ("Wrote output to", name)