from lexer import *
import ply.yacc as yacc
from mingus.midi import fluidsynth
from mingus.containers import *

#TODO
#1. Basic chords
#2. Variable duration chords
#3. Variables
#4. In-line Python
#5. The composition block

key = 'C'
meter = (4,4)
bpm = 120

def p_compostion(p):
    '''compostion : prelude bars
                  | bars'''
    if len(p) == 3:
        barsIndex = 2
    else:
        barsIndex = 1
    p[0] = Track()
    for bar in reversed(p[barsIndex]):
        p[0].add_bar(bar)

def p_prelude(p):
    '''prelude : LETTER NUMBER POST NUMBER LPARAN NUMBER RPARAN
               | LETTER NUMBER POST NUMBER'''
    global key
    global meter
    global bpm

    key = p[1]
    meter = (int(p[2]),int(p[4]))
    if len(p) == 8:
        bpm = int(p[6])

def p_bars_notes(p):
    '''bars : LBRACKET units RBRACKET bars
            | LBRACKET units RBRACKET'''
    if len(p) == 4: # base case
        p[0] = [Bar(key,meter)]
        for note in reversed(p[2]):
            p[0][0].place_notes(note[0],note[1])
    else:
        p[0] = p[4]
        p[0].append(Bar(key,meter))
        for note in reversed(p[2]):
            p[0][len(p[0])-1].place_notes(note[0],note[1])

def p_units_notes_chords(p):
    '''units : notes
             | chords'''
    p[0] = p[1]

def p_chords_notes(p):
    '''chords : LPARAN notes RPARAN chords
              | LPARAN notes RPARAN'''
    if len(p) == 4: # base case
        p[0] = [[NoteContainer(),p[2][0][1]]]
        for note in reversed(p[2]):
            p[0][0][0].add_note(note[0])
    else:
        p[0] = p[4]
        p[0].append([NoteContainer(),p[2][0][1]])
        for note in reversed(p[2]):
            p[0][len(p[0])-1][0].add_note(note[0])

def p_notes_pitch_duration(p):
    '''notes : pitch DASH duration notes
             | pitch DASH duration'''
    if len(p) == 4: # base case
        p[0] = [[p[1],p[3]]]
    else:
        p[0] = p[4]
        p[0].append([p[1],p[3]])

def p_pitch_terminals(p):
    'pitch : LETTER DASH NUMBER'
    p[0] = Note(''.join(p[1:4]))

def p_duration_terminals(p):
    'duration : NUMBER'
    p[0] = int(p[1])

def p_error(p):
    print("parser: syntax error")

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
