from lexer import *
import ply.yacc as yacc
from mingus.midi import fluidsynth
from mingus.containers import *

fluidsynth.init('sounds/electricPiano.SF2','coreaudio')

def p_expression_bar(t):
    'expression : LBRACKET expression RBRACKET'
    t[0] = t[2]

def p_expression_notes(t):
    'expression : NAME DASH NUMBER DASH NAME expression'
    fluidsynth.play_Note(Note(''.join(t[1:4])))
    t[0] = 0

def p_expression_note(t):
    'expression : NAME DASH NUMBER DASH NAME'
    fluidsynth.play_Note(Note(''.join(t[1:4])))
    t[0] = 0

yacc.yacc()

if __name__ == '__main__':
    while 1:
        try:
            s = raw_input(">>> ")
            if s == 'q': break
        except EOFError:
            break
        yacc.parse(s)    
