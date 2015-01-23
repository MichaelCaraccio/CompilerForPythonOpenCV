import ply.lex as lex
import re

reserved_words = (
    'for',
    'if',
    'in',
    'load_src',
    'save_dest',
    'display',
    'extension',
    'transform',
    'matrix3',
    'matrix5'
)

tokens = (
         'IDENTIFIER',
         'MATRIX3FORM',
         'MATRIX5FORM',
         'FILE',
         'COMPARE',
         'EGAL'
         ) + tuple(map(lambda s: s.upper(), reserved_words))

literals = '();{}:.//'

def t_COMPARE(t):
    r'=='
    return t

def t_EGAL(t):
    r'='
    return t

def t_MATRIX3FORM(t):
    r'\[(\[([ ]?\-?[ ]?\d+\.?[ ]?\d*),([ ]?\-?[ ]?\d+\.?[ ]?\d*),([ ]?\-?[ ]?\d+\.?[ ]?\d*)\]\,?){3}\]'
    return t

def t_MATRIX5FORM(t):
    r'\[(\[([ ]?\-?[ ]?\d+\.?[ ]?\d*)[ ]?,[ ]?([ ]?\-?[ ]?\d+\.?[ ]?\d*),[ ]?([ ]?\-?[ ]?\d+\.?[ ]?\d*),[ ]?([ ]?\-?[ ]?\d+\.?[ ]?\d*),([ ]?\-?[ ]?\d+\.?[ ]?\d*)\]\,?){5}\]'
    return t

def t_FILE(t):
    #r'\w[:][\\/].([A-Za-z0-9/\\]+)'
    r'[\\/].([A-Za-z0-9/\\_. ]+)'
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
