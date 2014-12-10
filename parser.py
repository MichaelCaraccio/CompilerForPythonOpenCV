import ply.yacc as yacc

import CompilerForPythonOpenCV.AST as AST

from CompilerForPythonOpenCV.lex import tokens

vars = {}

def p_programme_statement(p):
    ''' programme : load_src'''
    print("programme_statement")
    p[0] = AST.ProgramNode(p[1])


def p_load_src(p):
    '''load_src : expression FILE'''
    print("rentrer")
    p[0] = p[1]

def p_statement(p):
    ''' statement : LOAD_SRC
        | SAVE_DEST '''
    p[0] = p[1]


def p_statement_print(p):
    '''statement : PRINT expression '''
    p[0] = AST.PrintNode(p[2])

def p_structure(p):
    ''' structure : WHILE expression '{' programme '}' '''
    p[0] = AST.WhileNode([p[2], p[4]])

def p_expression_num(p):
    '''expression : IDENTIFIER '''
    p[0] = AST.TokenNode(p[1])

def p_expression_paren(p):
    '''expression : '(' expression ')' '''
    p[0] = p[2]

def p_assign(p):
    ''' assignation : IDENTIFIER '=' expression '''
    p[0] = AST.AssignNode([AST.TokenNode(p[1]), p[3]])

def p_error(p):
    print ("Syntax error in line %d" % p.lineno)
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
    name = os.path.splitext(sys.argv[1])[0]+'-ast.pdf'
    graph.write_pdf(name)
    print("wrote ast to ", name)