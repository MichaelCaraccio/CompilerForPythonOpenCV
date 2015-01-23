import AST as AST
from AST import addToClass
from functools import reduce


vars ={}

@addToClass(AST.ProgramNode)
def execute(self):
    for c in self.children:
        c.execute()
    
@addToClass(AST.TokenNode)
def execute(self):
    if isinstance(self.tok, str):
        try:
            return vars[self.tok]
        except KeyError:
            print ("*** Error: variable %s undefined!" % self.tok)
    return self.tok

@addToClass(AST.AssignNode)
def execute(self):
    vars[self.children[0].tok] = self.children[1].execute()

@addToClass(AST.PrintNode)
def execute(self):
    print (self.children[0].execute())
    
@addToClass(AST.WhileNode)
def execute(self):
    while self.children[0].execute():
        self.children[1].execute()

@addToClass(AST.LoadNode)
def execute(self):
   print("import cv2")
   print("import os")
   file = str(self.children[1]).replace('\n','')
   print("LOAD_SRC=\""+file+ "\"")

#@addToClass(AST.FileNode)
#def execute(self):
    #print(str(self.children[0])+"\"")

@addToClass(AST.SaveNode)
def execute(self):
    varFile = str(self.children[1]).replace('\n','')
    print("SAVE_SRC=\""+varFile+ "\"")

@addToClass(AST.ForNode)
def execute(self):
    print("for filename in os.listdir(LOAD_SRC):")

@addToClass(AST.IfNode)
def execute(self):
    varIf = str(self.children[0].children[1]).replace('\n','')
    print("\tif filename.endswith("+varIf+"):")

@addToClass(AST.MatrixNode3)
def execute(self):
    return

@addToClass(AST.MatrixNode5)
def execute(self):
    return


if __name__ == "__main__":
    from parser import parse
    import sys
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    
    ast.execute()