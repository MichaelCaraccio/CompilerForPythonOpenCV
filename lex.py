import ply.lex as lex
import re

reserved_words = (
    'while',
    'print',
    'for',
    'if',
    'in',
    'load_src',
    'save_dest',
    'display',
    'extension',
    'transform'
)

tokens = (
         'NUMBER',
         'IDENTIFIER',
         'MATRIX3',
         'MATRIX4',
         'FILE'
         ) + tuple(map(lambda s: s.upper(), reserved_words))

literals = '();={}'

def t_MATRIX3(t):
    r'\[(\{(\-?\d+\.?\d*),(\-?\d+\.?\d*),(\-?\d+\.?\d*)\}\,?){3}\]'
    return t

def t_MATRIX4(t):
    r'\[(\{(\-?\d+\.?\d*),(\-?\d+\.?\d*),(\-?\d+\.?\d*),(\-?\d+\.?\d*)\}\,?){4}\]'
    return t

def t_FILE(t):
    r'[A-Za-z_]\w*\.[A-Za-z]{3,4}'
    print("FILE")
    return t

# Traitement des fichiers à faire

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Line %d: Problem while parsing %s!" % (t.lineno, t.value))
        t.value = 0
    return t


def t_IDENTIFIER(t):
    r'[A-Za-z_.]\w*'
    if t.value.lower() in reserved_words:
        t.type = t.value.upper()
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % repr(t.value[0]))
    t.lexer.skip(1)


lex.lex()

if __name__ == "__main__":
    import sys

    prog = open(sys.argv[1]).read()

    lex.input(prog)

    while 1:
        tok = lex.token()
        if not tok: break
        print("line %d: %s(%s)" % (tok.lineno, tok.type, tok.value))
