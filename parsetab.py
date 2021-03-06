
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x8ck\xec\xd9Om\xcf1\xa5\xe74\t\x8a\xe3\xf0\x17'
    
_lr_action_items = {'DASH':([9,10,24,],[18,19,-15,]),'LPARAN':([3,6,7,22,25,26,],[8,8,8,-11,-14,-16,]),'RPARAN':([16,17,23,25,26,],[22,-13,-12,-14,-16,]),'NUMBER':([4,18,19,21,28,],[12,24,26,28,29,]),'LBRACKET':([0,5,20,28,29,],[3,3,3,-4,-3,]),'LETTER':([0,3,6,7,8,17,22,25,26,],[4,9,9,9,9,9,-11,-14,-16,]),'RBRACKET':([6,7,11,14,15,22,25,26,],[-8,-10,20,-7,-9,-11,-14,-16,]),'POST':([12,],[21,]),'$end':([1,2,13,20,27,],[-2,0,-1,-6,-5,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'bars':([0,5,20,],[1,13,27,]),'compostion':([0,],[2,]),'notes':([8,17,],[16,23,]),'note':([3,6,7,8,17,],[6,6,6,17,17,]),'duration':([19,],[25,]),'chord':([3,6,7,],[7,7,7,]),'pitch':([3,6,7,8,17,],[10,10,10,10,10,]),'units':([3,6,7,],[11,14,15,]),'prelude':([0,],[5,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> compostion","S'",1,None,None,None),
  ('compostion -> prelude bars','compostion',2,'p_compostion','parser.py',19),
  ('compostion -> bars','compostion',1,'p_compostion','parser.py',20),
  ('prelude -> LETTER NUMBER POST NUMBER NUMBER','prelude',5,'p_prelude','parser.py',30),
  ('prelude -> LETTER NUMBER POST NUMBER','prelude',4,'p_prelude','parser.py',31),
  ('bars -> LBRACKET units RBRACKET bars','bars',4,'p_bars_notes','parser.py',42),
  ('bars -> LBRACKET units RBRACKET','bars',3,'p_bars_notes','parser.py',43),
  ('units -> note units','units',2,'p_units_note_chords','parser.py',55),
  ('units -> note','units',1,'p_units_note_chords','parser.py',56),
  ('units -> chord units','units',2,'p_units_note_chords','parser.py',57),
  ('units -> chord','units',1,'p_units_note_chords','parser.py',58),
  ('chord -> LPARAN notes RPARAN','chord',3,'p_chord_notes','parser.py',65),
  ('notes -> note notes','notes',2,'p_notes','parser.py',71),
  ('notes -> note','notes',1,'p_notes','parser.py',72),
  ('note -> pitch DASH duration','note',3,'p_note_pitch_duration','parser.py',80),
  ('pitch -> LETTER DASH NUMBER','pitch',3,'p_pitch_terminals','parser.py',84),
  ('duration -> NUMBER','duration',1,'p_duration_terminals','parser.py',88),
]
