
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = '7arf3atf 7arfjar1 7arfjar2 7arfjar3 7arfjar4 7arfjazm INT a3oudou bassmala damir darfzaman fi3l2 fi3lamr fi3lmad ismajrour2 ismmawsoul ismmbm issm issmj1 issmj2 khabar mad modaf1 modaf2 modaf22 modaf3 moubtada2 moudafilayh moudari31 moudari32 rabi sifa sifa2ikhlas : bassmala issmj1 sifa sifa2 fi3lamr damir issmj2 issm INT issmj2 moubtada2 INT 7arfjazm moudari32 7arf3atf 7arfjazm mad INT 7arf3atf 7arfjazm moudari31 7arfjar4 khabar issm INTikhlas : bassmala issmj1 sifa sifa2 fi3lamr a3oudou 7arfjar1 rabi moudafilayh INT 7arfjar2 ismmbm ismmawsoul fi3lmad INT 7arf3atf 7arfjar2 ismmbm modaf1 darfzaman fi3l2 INT 7arf3atf 7arfjar2 ismmbm modaf22 7arfjar3 ismajrour2 INT 7arf3atf 7arfjar2 ismmbm modaf2 darfzaman modaf3 INT'
    
_lr_action_items = {'bassmala':([0,],[2,]),'$end':([1,45,57,],[0,-1,-2,]),'issmj1':([2,],[3,]),'sifa':([3,],[4,]),'sifa2':([4,],[5,]),'fi3lamr':([5,],[6,]),'damir':([6,],[7,]),'a3oudou':([6,],[8,]),'issmj2':([7,13,],[9,15,]),'7arfjar1':([8,],[10,]),'issm':([9,41,],[11,43,]),'rabi':([10,],[12,]),'INT':([11,14,17,24,29,38,43,49,56,],[13,16,19,26,31,40,45,50,57,]),'moudafilayh':([12,],[14,]),'moubtada2':([15,],[17,]),'7arfjar2':([16,28,42,51,],[18,30,44,52,]),'ismmbm':([18,30,44,52,],[20,32,46,53,]),'7arfjazm':([19,25,33,],[21,27,35,]),'ismmawsoul':([20,],[22,]),'moudari32':([21,],[23,]),'fi3lmad':([22,],[24,]),'7arf3atf':([23,26,31,40,50,],[25,28,33,42,51,]),'mad':([27,],[29,]),'modaf1':([32,],[34,]),'darfzaman':([34,54,],[36,55,]),'moudari31':([35,],[37,]),'fi3l2':([36,],[38,]),'7arfjar4':([37,],[39,]),'khabar':([39,],[41,]),'modaf22':([46,],[47,]),'7arfjar3':([47,],[48,]),'ismajrour2':([48,],[49,]),'modaf2':([53,],[54,]),'modaf3':([55,],[56,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ikhlas':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ikhlas","S'",1,None,None,None),
  ('ikhlas -> bassmala issmj1 sifa sifa2 fi3lamr damir issmj2 issm INT issmj2 moubtada2 INT 7arfjazm moudari32 7arf3atf 7arfjazm mad INT 7arf3atf 7arfjazm moudari31 7arfjar4 khabar issm INT','ikhlas',25,'p_ikhlas','yacc.py',29),
  ('ikhlas -> bassmala issmj1 sifa sifa2 fi3lamr a3oudou 7arfjar1 rabi moudafilayh INT 7arfjar2 ismmbm ismmawsoul fi3lmad INT 7arf3atf 7arfjar2 ismmbm modaf1 darfzaman fi3l2 INT 7arf3atf 7arfjar2 ismmbm modaf22 7arfjar3 ismajrour2 INT 7arf3atf 7arfjar2 ismmbm modaf2 darfzaman modaf3 INT','ikhlas',36,'p_fala9','yacc.py',37),
]
