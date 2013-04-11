from lexer import *
import ply.yacc as yacc
from mingus.midi import fluidsynth
from mingus.containers import *

key = 'C'
meter = (4,4)
bpm = 120

def p_compostion(t):
    '''compostion : prelude bars
                  | bars'''
    if len(t) == 3:
        barsIndex = 2
    else:
        barsIndex = 1
    t[0] = Track()
    for bar in reversed(t[barsIndex]):
        t[0].add_bar(bar)

def p_prelude(t):
    '''prelude : LETTER NUMBER POST NUMBER LPARAN NUMBER RPARAN
               | LETTER NUMBER POST NUMBER'''
    global key
    global meter
    global bpm

    key = t[1]
    meter = (int(t[2]),int(t[4]))
    if len(t) == 8:
        bpm = int(t[6])

def p_bars_notes(t):
    '''bars : LBRACKET notes RBRACKET bars
            | LBRACKET notes RBRACKET'''
    if len(t) == 4: # base case
        t[0] = [Bar(key,meter)]
        for note in reversed(t[2]):
            t[0][0].place_notes(note[0],note[1])
    else:
        t[0] = t[4]
        t[0].append(Bar(key,meter))
        for note in reversed(t[2]):
            t[0][len(t[0])-1].place_notes(note[0],note[1])

def p_notes_pitch_duration(t):
    '''notes : pitch DASH duration notes
             | pitch DASH duration'''
    if len(t) == 4: # base case
        t[0] = [[t[1],t[3]]]
    else:
        t[0] = t[4]
        t[0].append([t[1],t[3]])

def p_pitch_terminals(t):
    'pitch : LETTER DASH NUMBER'
    t[0] = Note(''.join(t[1:4]))

def p_duration_terminals(t):
    'duration : NUMBER'
    t[0] = int(t[1])

def p_error(t):
    print("Syntax error")

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
        fluidsynth.play_Track(result,1,bpm)
