import ply.lex as lex

tokens = ('LBRACKET', 'RBRACKET', 'LPARAN', 'RPARAN', 
          'POST', 'DASH', 'LETTER', 'NUMBER')

t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPARAN = r'\('
t_RPARAN = r'\)'
t_POST = r'\|'
t_DASH = r'-'
t_LETTER = r'[A-G_](b|\#)*'
t_NUMBER = r'\d+'

t_ignore = ' '

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()

if __name__ == '__main__':
    import sys

    lexer.input(sys.stdin.read())
    while True:
        tok = lexer.token()
        if not tok: break
        print tok
