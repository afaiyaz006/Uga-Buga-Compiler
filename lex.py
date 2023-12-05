import ply.lex as lex
tokens = (
    'NAME', 'NUMBER','GTE','LTE','EQ','NEQ','OR','AND','GT','LT','HOCCHE'
)

literals = ['=', '+', '-', '*', '/', '(', ')','&','|']

t_GT='>'
t_LT='<'
t_GTE='<='
t_LTE='>='
t_EQ='=='
t_NEQ='!='

# Tokens

t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_HOCCHE(t):
    r'HOCCHE'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer=lex.lex()
