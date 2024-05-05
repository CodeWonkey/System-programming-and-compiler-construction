import ply.lex as lex
import ply.yacc as yacc

# Define the lexer tokens
tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'
]

# Define the token regular expressions
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule to handle whitespace and newlines
t_ignore = ' \t\n'

# Define a rule to handle errors
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Define the grammar rules
def p_expression(p):
    '''expression : term
                  | expression PLUS term
                  | expression MINUS term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        else:
            p[0] = p[1] - p[3]

def p_term(p):
    '''term : factor
            | term TIMES factor
            | term DIVIDE factor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        else:
            p[0] = p[1] / p[3]

def p_factor(p):
    '''factor : NUMBER
              | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

# Define a rule to handle syntax errors
def p_error(p):
    print("Syntax error")

# Build the parser
parser = yacc.yacc()

# Example usage
expression = "3 + 4 * 5 - 6 / 2"
result = parser.parse(expression, lexer=lexer)
print(f"Result: {result}")