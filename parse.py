from lex import lexer
import ply.yacc as yacc
from lex import tokens
from code_generator import generate_tac
precedence = (
    
    ('left', '+', '-'),
    ('left', '/', '*'),
    ('right', 'UMINUS'),
    ('nonassoc','(',')'),  # Nonassociative precedence for parentheses

)

# dictionary of names
names = {}


def p_statement_assign(p):
    '''statement :  NAME "=" expression
                  | NAME HOCCHE expression
                   '''
    
    p[0]=('EQUAL',p[1],p[3])
    names[p[1]] = p[3]


def p_statement_expr(p):
    'statement : expression'
    print(p[1])


def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''
    if p[2] == '+':
        p[0] = ('+', p[1], p[3])
    elif p[2] == '-':
        p[0] = ('-', p[1], p[3])
    elif p[2] == '*':
        p[0] = ('*', p[1],p[3])
    elif p[2] == '/':
        p[0] = ('/', p[1],p[3])

def p_expression_relop(t):
    '''expression : expression GT expression
                  | expression LT expression
                  | expression GTE expression
                  | expression LTE expression
                  | expression EQ expression
                  | expression NEQ expression
                  | expression '&' expression
                  | expression '|' expression'''
    if t[2] == '>': 
        t[0] = t[1] > t[3]
    elif t[2] == '<':
        t[0] = t[1] < t[3]
    elif t[2] == '>=':
        t[0] = t[1] >= t[3]
    elif t[2] == '<=':
        t[0] = t[1] <= t[3]
    elif t[2] == '==':
        t[0] = t[1] == t[3]
    elif t[2] == '!=':
        t[0] = t[1] != t[3]
    elif t[2] == '&':
        t[0] = t[1] and t[3]
    elif t[2] == '|':
        t[0] = t[1] or t[3]



def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]


def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]


def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]


def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

# Build the parser
parser=yacc.yacc(debug=True)
        