
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'left*/left+-rightUMINUS()AND EQ GT GTE HOCCHE LT LTE NAME NEQ NUMBER ORstatement :  NAME "=" expression\n                  | NAME HOCCHE expression\n                   statement : expressionexpression : expression \'+\' expression\n                  | expression \'-\' expression\n                  | expression \'*\' expression\n                  | expression \'/\' expressionexpression : expression GT expression\n                  | expression LT expression\n                  | expression GTE expression\n                  | expression LTE expression\n                  | expression EQ expression\n                  | expression NEQ expression\n                  | expression \'&\' expression\n                  | expression \'|\' expressionexpression : \'-\' expression %prec UMINUSexpression : \'(\' expression \')\'expression : NUMBERexpression : NAME'
    
_lr_action_items = {'NAME':([0,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[2,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'-':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[4,-19,10,4,4,-18,4,4,4,4,4,4,4,4,4,4,4,4,4,4,-16,-19,10,10,10,-4,-5,10,10,10,10,10,10,10,10,10,10,-17,]),'(':([0,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'NUMBER':([0,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'$end':([1,2,3,6,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[0,-19,-3,-18,-16,-19,-1,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-17,]),'=':([2,],[7,]),'HOCCHE':([2,],[8,]),'+':([2,3,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-19,9,-18,-16,-19,9,9,9,-4,-5,9,9,9,9,9,9,9,9,9,9,-17,]),'*':([2,3,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-19,11,-18,-16,-19,11,11,11,-4,-5,-6,-7,11,11,11,11,11,11,11,11,-17,]),'/':([2,3,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-19,12,-18,-16,-19,12,12,12,-4,-5,-6,-7,12,12,12,12,12,12,12,12,-17,]),'GT':([2,3,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-19,13,-18,-16,-19,13,13,13,-4,-5,-6,-7,13,13,13,13,13,13,13,13,-17,]),'LT':([2,3,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-19,14,-18,-16,-19,14,14,14,-4,-5,-6,-7,14,14,14,14,14,14,14,14,-17,]),'GTE':([2,3,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-19,15,-18,-16,-19,15,15,15,-4,-5,-6,-7,15,15,15,15,15,15,15,15,-17,]),'LTE':([2,3,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-19,16,-18,-16,-19,16,16,16,-4,-5,-6,-7,16,16,16,16,16,16,16,16,-17,]),'EQ':([2,3,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-19,17,-18,-16,-19,17,17,17,-4,-5,-6,-7,17,17,17,17,17,17,17,17,-17,]),'NEQ':([2,3,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-19,18,-18,-16,-19,18,18,18,-4,-5,-6,-7,18,18,18,18,18,18,18,18,-17,]),'&':([2,3,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-19,19,-18,-16,-19,19,19,19,-4,-5,-6,-7,19,19,19,19,19,19,19,19,-17,]),'|':([2,3,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-19,20,-18,-16,-19,20,20,20,-4,-5,-6,-7,20,20,20,20,20,20,20,20,-17,]),')':([6,21,22,23,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-18,-16,-19,38,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[3,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME = expression','statement',3,'p_statement_assign','parse.py',18),
  ('statement -> NAME HOCCHE expression','statement',3,'p_statement_assign','parse.py',19),
  ('statement -> expression','statement',1,'p_statement_expr','parse.py',27),
  ('expression -> expression + expression','expression',3,'p_expression_binop','parse.py',32),
  ('expression -> expression - expression','expression',3,'p_expression_binop','parse.py',33),
  ('expression -> expression * expression','expression',3,'p_expression_binop','parse.py',34),
  ('expression -> expression / expression','expression',3,'p_expression_binop','parse.py',35),
  ('expression -> expression GT expression','expression',3,'p_expression_relop','parse.py',46),
  ('expression -> expression LT expression','expression',3,'p_expression_relop','parse.py',47),
  ('expression -> expression GTE expression','expression',3,'p_expression_relop','parse.py',48),
  ('expression -> expression LTE expression','expression',3,'p_expression_relop','parse.py',49),
  ('expression -> expression EQ expression','expression',3,'p_expression_relop','parse.py',50),
  ('expression -> expression NEQ expression','expression',3,'p_expression_relop','parse.py',51),
  ('expression -> expression & expression','expression',3,'p_expression_relop','parse.py',52),
  ('expression -> expression | expression','expression',3,'p_expression_relop','parse.py',53),
  ('expression -> - expression','expression',2,'p_expression_uminus','parse.py',74),
  ('expression -> ( expression )','expression',3,'p_expression_group','parse.py',79),
  ('expression -> NUMBER','expression',1,'p_expression_number','parse.py',84),
  ('expression -> NAME','expression',1,'p_expression_name','parse.py',89),
]
