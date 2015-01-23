import ply.yacc as yacc

import AST as AST

from lex import tokens

def p_programme_statement(p):
	''' programme : statement '''
	p[0] = AST.ProgramNode(p[1])

def p_programme_recursive(p):
	''' programme : statement ';' programme '''
	p[0] = AST.ProgramNode([p[1]]+p[3].children)

def p_statement(p):
    '''statement : for
        | load
        | save
        | matrix3
        | matrix5
        | transform
        | display
        | if'''
    p[0] = p[1]

def p_load(p):
    '''load : LOAD_SRC expression FILE'''
    p[0] = AST.LoadNode([p[2], AST.FileNode(p[3])])

def p_save(p):
    '''save : SAVE_DEST expression FILE'''
    p[0] = AST.SaveNode([p[2], AST.FileNode(p[3])])

def p_for(p):
    '''for : FOR expression IN expression'''
    p[0] = AST.ForNode([p[2], AST.LoadNode(p[4])])

def p_matrix3(p):
    '''matrix3 : matrix3_assign'''
    p[0] = AST.MatrixNode3(p[1])

def p_matrix3_assign(p):
    '''matrix3_assign : MATRIX3 IDENTIFIER EGAL MATRIX3FORM '''
    p[0] = AST.AssignNode([AST.TokenNode(p[2]), AST.TokenNode(p[4])])

def p_matrix5(p):
    '''matrix5 : matrix5_assign'''
    p[0] = AST.MatrixNode5(p[1])

def p_matrix5_assign(p):
    '''matrix5_assign : MATRIX5 IDENTIFIER EGAL MATRIX5FORM '''
    p[0] = AST.AssignNode([AST.TokenNode(p[2]), AST.TokenNode(p[4])])

def p_transform(p):
    '''transform : TRANSFORM expression expression'''
    p[0] = AST.TransformNode([p[2], AST.TokenNode(p[3])])

def p_display(p):
    '''display : DISPLAY FILE
        | DISPLAY expression'''
    p[0] = AST.DisplayNode(AST.FileNode(p[2]))

def p_if_assign(p):
    '''if_assign : IF EXTENSION expression COMPARE expression'''
    p[0] = AST.CompareNode([AST.TokenNode(p[3]), AST.TokenNode(p[5])])

def p_if(p):
    '''if : if_assign'''
    p[0] = AST.IfNode(p[1])

def p_expression_num(p):
    '''expression : IDENTIFIER'''
    p[0] = AST.TokenNode(p[1])

def p_error(p):
    print("Syntax error in line %d" % p.lineno)
    yacc.errok()

def parse(program):
    return yacc.parse(program)

yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    import sys
    import os
    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog)
    graph = result.makegraphicaltree()
    name = os.path.splitext(sys.argv[1])[0] + '-ast.pdf'
    graph.write_pdf(name)
    print("wrote ast to ", name)