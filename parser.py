from lexer import *
import ply.yacc as yacc
from mingus.midi import fluidsynth
from mingus.containers import *

key = 'C'
meter = (4,4)
bpm = 120

def p_compostion_bpm(t):
    'composition : LETTER NUMBER POST NUMBER LPARAN NUMBER RPARAN bar'
    global key
    global meter
    global bpm

    key = t[1]
    meter = (int(t[2]),int(t[4]))
    bpm = int(t[6])
    t[0] = Track()
    t[0].add_bar(t[8])

def p_compostion_nobpm(t):
    'composition : LETTER NUMBER POST NUMBER bar'
    global key
    global meter

    key = t[1]
    meter = (int(t[2]),int(t[4]))
    t[0] = Track()
    t[0].add_bar(t[5])

def p_compostion_defaults(t):
    'composition : bar'
    t[0] = Track()
    t[0].add_bar(t[1])

def p_bar_note(t):
    'bar : LBRACKET notes RBRACKET'
    t[0] = Bar(key,meter)
    for note in reversed(t[2]):
        t[0].place_notes(note[0],note[1])

def p_notes_pitch_duration(t):
    '''notes : pitch DASH duration notes
             | pitch DASH duration'''
    if len(t) == 4:
        t[0] = [[t[1],t[3]]]
    else:
        t[0] = t[4]
        t[0].append([t[1],t[3]])

def p_note_terminals(t):
    'pitch : LETTER DASH NUMBER'
    t[0] = Note(''.join(t[1:4]))

def p_duration_terminals(t):
    'duration : NUMBER'
    t[0] = int(t[1])

def p_error(t):
    print("Bad parse")

yacc.yacc()

if __name__ == '__main__':
    fluidsynth.init('sounds/electricPiano.SF2','coreaudio')
    while 1:
        try:
            s = raw_input(">>> ")
            if s == 'q': break
            if s == '': continue
        except EOFError:
            break
        result = yacc.parse(s)
        print result
        fluidsynth.play_Track(result,1,bpm)
