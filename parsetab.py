
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASSIGNleftNEleftLTGTleftPLUSMINUSleftTIMESDIVIDErightPARLleftPARRAND ARRAY_FLOAT ARRAY_INT ASSIGN BEGIN BOOL COLON COMMA COMMENT CUBE_FLOAT CUBE_INT DIVIDE DO DOT DWHILE ELSE END ENDDO ENDF ENDIF ENDP ENDW EQ FLOAT FOR GOSUB GT ID IF IN INPUT INT LT MATRIX_FLOAT MATRIX_INT MINUS NE NUMBER OR PARL PARR PLUS PRINT PROCEDURE PROGRAM SQBL SQBR STRING TIMES VAR WHILE newline program : PROGRAM COLON V MAIN P B END MAIN : empty V : V VAR VM COLON TIPO\n    | empty VM : ID VM2 VM : ID SQBL NUMBER SQBR VM2 VM : ID SQBL NUMBER COMMA NUMBER SQBR VM2 VM : ID SQBL NUMBER COMMA NUMBER COMMA NUMBER SQBR VM2 VM2 : COMMA ID VM2 VM2 : COMMA ID SQBL NUMBER  SQBR VM2 VM2 : COMMA ID SQBL NUMBER COMMA NUMBER SQBR VM2 VM2 : COMMA ID SQBL NUMBER COMMA NUMBER COMMA NUMBER SQBR VM2VM2 : empty TIPO : FLOAT\n    | INT\n    | ARRAY_INT\n    | ARRAY_FLOAT\n    | MATRIX_INT\n    | MATRIX_FLOAT\n    | CUBE_INT\n    | CUBE_FLOAT\n    | BOOL P : P  AUXPOSP PROCEDURE ID COLON B ENDP P : empty AUXPOSP : empty B : BEGIN COLON ST  ST : S ST\n    | empty S : FOR ID IN ID COLON ST ENDF\n    | DO COLON ST DWHILE COLON CONDITION ENDDO\n     S : GOSUB IDS : PRINT PARL SID PARRSID : SID PLUS SID_TSID : SID_TSID_T : STRING\n    | IDSID : emptyS : INPUT PARL ID PARRS : INPUT PARL ID SQBL IDNUM SQBR PARRS : INPUT PARL ID SQBL IDNUM COMMA IDNUM SQBR PARRS : INPUT PARL ID SQBL IDNUM COMMA IDNUM COMMA IDNUM SQBR PARRIDNUM : ID\n    | NUMBER S : VAMC ASSIGN UPDATEUPDATE : T UPDATE : UPDATE PLUS T\n    | UPDATE MINUS T\n    | UPDATE OR TT : FT : T TIMES F\n    | T DIVIDE F\n    | T AND F\n    F : IDF : ID SQBL IDNUM SQBRF : ID SQBL IDNUM COMMA IDNUM SQBRF : ID SQBL IDNUM COMMA IDNUM COMMA IDNUM SQBRF : NUMBERF : PARL CONDITION PARRVAMC : IDVAMC : ID SQBL IDNUM SQBRVAMC : ID SQBL IDNUM COMMA IDNUM SQBRVAMC : ID SQBL IDNUM COMMA IDNUM COMMA IDNUM SQBRS : IF CONDITION AUXCOLON ST ENDIFS : IF CONDITION AUXCOLON ST ELSE COLON AUXQ ST AUXENDIF ENDIFAUXQ : emptyAUXENDIF : empty S : WHILE AUXWHILE CONDITION AUXCOLON ST AUXENDWHILE ENDWAUXWHILE : emptyAUXENDWHILE : emptyCONDITION : UPDATECONDITION : UPDATE NE UPDATE\n    | UPDATE GT UPDATE\n    | UPDATE LT UPDATE\n    | UPDATE EQ UPDATEAUXCOLON : COLON empty :\t'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,22,],[0,-1,]),'COLON':([2,11,12,15,18,21,36,37,43,50,52,63,64,65,66,67,68,72,102,104,106,108,111,117,118,119,120,121,122,123,124,125,126,128,131,133,140,141,144,146,157,159,168,170,176,181,],[3,17,-76,24,-5,-13,-76,54,58,-76,-9,89,-70,-45,-49,-53,-57,-6,89,-76,-76,134,136,-71,-72,-73,-74,-46,-47,-48,-50,-51,-52,-58,-7,-10,153,-54,-76,-76,-8,-11,-55,-76,-12,-56,]),'VAR':([3,4,5,25,26,27,28,29,30,31,32,33,34,],[-76,7,-4,-3,-14,-15,-16,-17,-18,-19,-20,-21,-22,]),'BEGIN':([3,4,5,6,8,9,10,25,26,27,28,29,30,31,32,33,34,54,107,],[-76,-76,-4,-76,-2,15,-24,-3,-14,-15,-16,-17,-18,-19,-20,-21,-22,15,-23,]),'PROCEDURE':([3,4,5,6,8,9,10,14,16,25,26,27,28,29,30,31,32,33,34,107,],[-76,-76,-4,-76,-2,-76,-24,23,-25,-3,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,]),'ID':([7,20,23,24,39,41,44,48,49,57,58,59,60,61,62,65,66,67,68,69,70,71,76,87,88,89,90,91,92,93,94,95,96,97,98,99,100,110,112,113,114,115,121,122,123,124,125,126,128,129,134,136,139,141,142,148,152,153,160,162,163,165,166,167,168,169,172,178,181,183,184,],[12,36,37,42,42,56,59,67,-76,77,42,-31,85,86,67,-45,-49,-53,-57,67,67,-68,108,-44,42,-75,67,67,67,67,67,67,67,67,67,67,77,77,-32,85,-38,77,-46,-47,-48,-50,-51,-52,-58,42,42,67,-63,-54,77,77,77,-76,-29,-30,-39,42,-65,77,-55,-67,77,-40,-56,-64,-41,]),'SQBL':([12,36,42,67,86,],[19,53,57,100,115,]),'COMMA':([12,35,36,50,73,74,77,78,79,104,106,127,132,135,138,144,146,154,164,170,],[20,51,20,20,103,105,-42,110,-43,20,20,142,145,148,152,20,20,167,172,20,]),'END':([13,24,38,39,40,55,59,65,66,67,68,87,112,114,121,122,123,124,125,126,128,139,141,160,162,163,168,169,178,181,183,184,],[22,-76,-26,-76,-28,-27,-31,-45,-49,-53,-57,-44,-32,-38,-46,-47,-48,-50,-51,-52,-58,-63,-54,-29,-30,-39,-55,-67,-40,-56,-64,-41,]),'FLOAT':([17,],[26,]),'INT':([17,],[27,]),'ARRAY_INT':([17,],[28,]),'ARRAY_FLOAT':([17,],[29,]),'MATRIX_INT':([17,],[30,]),'MATRIX_FLOAT':([17,],[31,]),'CUBE_INT':([17,],[32,]),'CUBE_FLOAT':([17,],[33,]),'BOOL':([17,],[34,]),'NUMBER':([19,48,49,51,53,57,62,69,70,71,90,91,92,93,94,95,96,97,98,99,100,103,105,110,115,136,142,145,148,152,167,172,],[35,68,-76,73,74,79,68,68,68,-68,68,68,68,68,68,68,68,68,68,68,79,130,132,79,79,68,79,158,79,79,79,79,]),'FOR':([24,39,58,59,65,66,67,68,87,88,89,112,114,121,122,123,124,125,126,128,129,134,139,141,153,160,162,163,165,166,168,169,178,181,183,184,],[41,41,41,-31,-45,-49,-53,-57,-44,41,-75,-32,-38,-46,-47,-48,-50,-51,-52,-58,41,41,-63,-54,-76,-29,-30,-39,41,-65,-55,-67,-40,-56,-64,-41,]),'DO':([24,39,58,59,65,66,67,68,87,88,89,112,114,121,122,123,124,125,126,128,129,134,139,141,153,160,162,163,165,166,168,169,178,181,183,184,],[43,43,43,-31,-45,-49,-53,-57,-44,43,-75,-32,-38,-46,-47,-48,-50,-51,-52,-58,43,43,-63,-54,-76,-29,-30,-39,43,-65,-55,-67,-40,-56,-64,-41,]),'GOSUB':([24,39,58,59,65,66,67,68,87,88,89,112,114,121,122,123,124,125,126,128,129,134,139,141,153,160,162,163,165,166,168,169,178,181,183,184,],[44,44,44,-31,-45,-49,-53,-57,-44,44,-75,-32,-38,-46,-47,-48,-50,-51,-52,-58,44,44,-63,-54,-76,-29,-30,-39,44,-65,-55,-67,-40,-56,-64,-41,]),'PRINT':([24,39,58,59,65,66,67,68,87,88,89,112,114,121,122,123,124,125,126,128,129,134,139,141,153,160,162,163,165,166,168,169,178,181,183,184,],[45,45,45,-31,-45,-49,-53,-57,-44,45,-75,-32,-38,-46,-47,-48,-50,-51,-52,-58,45,45,-63,-54,-76,-29,-30,-39,45,-65,-55,-67,-40,-56,-64,-41,]),'INPUT':([24,39,58,59,65,66,67,68,87,88,89,112,114,121,122,123,124,125,126,128,129,134,139,141,153,160,162,163,165,166,168,169,178,181,183,184,],[46,46,46,-31,-45,-49,-53,-57,-44,46,-75,-32,-38,-46,-47,-48,-50,-51,-52,-58,46,46,-63,-54,-76,-29,-30,-39,46,-65,-55,-67,-40,-56,-64,-41,]),'IF':([24,39,58,59,65,66,67,68,87,88,89,112,114,121,122,123,124,125,126,128,129,134,139,141,153,160,162,163,165,166,168,169,178,181,183,184,],[48,48,48,-31,-45,-49,-53,-57,-44,48,-75,-32,-38,-46,-47,-48,-50,-51,-52,-58,48,48,-63,-54,-76,-29,-30,-39,48,-65,-55,-67,-40,-56,-64,-41,]),'WHILE':([24,39,58,59,65,66,67,68,87,88,89,112,114,121,122,123,124,125,126,128,129,134,139,141,153,160,162,163,165,166,168,169,178,181,183,184,],[49,49,49,-31,-45,-49,-53,-57,-44,49,-75,-32,-38,-46,-47,-48,-50,-51,-52,-58,49,49,-63,-54,-76,-29,-30,-39,49,-65,-55,-67,-40,-56,-64,-41,]),'ENDP':([24,38,39,40,55,59,65,66,67,68,75,87,112,114,121,122,123,124,125,126,128,139,141,160,162,163,168,169,178,181,183,184,],[-76,-26,-76,-28,-27,-31,-45,-49,-53,-57,107,-44,-32,-38,-46,-47,-48,-50,-51,-52,-58,-63,-54,-29,-30,-39,-55,-67,-40,-56,-64,-41,]),'SQBR':([35,73,74,77,78,79,127,130,132,135,138,154,158,161,164,175,177,],[50,104,106,-42,109,-43,141,144,146,149,151,168,170,171,173,181,182,]),'DWHILE':([39,40,55,58,59,65,66,67,68,80,87,112,114,121,122,123,124,125,126,128,139,141,160,162,163,168,169,178,181,183,184,],[-76,-28,-27,-76,-31,-45,-49,-53,-57,111,-44,-32,-38,-46,-47,-48,-50,-51,-52,-58,-63,-54,-29,-30,-39,-55,-67,-40,-56,-64,-41,]),'ENDIF':([39,40,55,59,65,66,67,68,87,88,89,112,114,116,121,122,123,124,125,126,128,139,141,153,160,162,163,165,166,168,169,174,178,179,180,181,183,184,],[-76,-28,-27,-31,-45,-49,-53,-57,-44,-76,-75,-32,-38,139,-46,-47,-48,-50,-51,-52,-58,-63,-54,-76,-29,-30,-39,-76,-65,-55,-67,-76,-40,183,-66,-56,-64,-41,]),'ELSE':([39,40,55,59,65,66,67,68,87,88,89,112,114,116,121,122,123,124,125,126,128,139,141,160,162,163,168,169,178,181,183,184,],[-76,-28,-27,-31,-45,-49,-53,-57,-44,-76,-75,-32,-38,140,-46,-47,-48,-50,-51,-52,-58,-63,-54,-29,-30,-39,-55,-67,-40,-56,-64,-41,]),'ENDW':([39,40,55,59,65,66,67,68,87,89,112,114,121,122,123,124,125,126,128,129,139,141,143,155,156,160,162,163,168,169,178,181,183,184,],[-76,-28,-27,-31,-45,-49,-53,-57,-44,-75,-32,-38,-46,-47,-48,-50,-51,-52,-58,-76,-63,-54,-76,169,-69,-29,-30,-39,-55,-67,-40,-56,-64,-41,]),'ENDF':([39,40,55,59,65,66,67,68,87,112,114,121,122,123,124,125,126,128,134,139,141,147,160,162,163,168,169,178,181,183,184,],[-76,-28,-27,-31,-45,-49,-53,-57,-44,-32,-38,-46,-47,-48,-50,-51,-52,-58,-76,-63,-54,160,-29,-30,-39,-55,-67,-40,-56,-64,-41,]),'ASSIGN':([42,47,109,149,171,],[-59,62,-60,-61,-62,]),'PARL':([45,46,48,49,62,69,70,71,90,91,92,93,94,95,96,97,98,99,136,],[60,61,69,-76,69,69,69,-68,69,69,69,69,69,69,69,69,69,69,69,]),'IN':([56,],[76,]),'STRING':([60,113,],[84,84,]),'PARR':([60,64,65,66,67,68,81,82,83,84,85,86,101,117,118,119,120,121,122,123,124,125,126,128,137,141,151,168,173,181,182,],[-76,-70,-45,-49,-53,-57,112,-34,-37,-35,-36,114,128,-71,-72,-73,-74,-46,-47,-48,-50,-51,-52,-58,-33,-54,163,-55,178,-56,184,]),'PLUS':([60,64,65,66,67,68,81,82,83,84,85,87,117,118,119,120,121,122,123,124,125,126,128,137,141,168,181,],[-76,94,-45,-49,-53,-57,113,-34,-37,-35,-36,94,94,94,94,94,-46,-47,-48,-50,-51,-52,-58,-33,-54,-55,-56,]),'ENDDO':([64,65,66,67,68,117,118,119,120,121,122,123,124,125,126,128,141,150,168,181,],[-70,-45,-49,-53,-57,-71,-72,-73,-74,-46,-47,-48,-50,-51,-52,-58,-54,162,-55,-56,]),'NE':([64,65,66,67,68,121,122,123,124,125,126,128,141,168,181,],[90,-45,-49,-53,-57,-46,-47,-48,-50,-51,-52,-58,-54,-55,-56,]),'GT':([64,65,66,67,68,121,122,123,124,125,126,128,141,168,181,],[91,-45,-49,-53,-57,-46,-47,-48,-50,-51,-52,-58,-54,-55,-56,]),'LT':([64,65,66,67,68,121,122,123,124,125,126,128,141,168,181,],[92,-45,-49,-53,-57,-46,-47,-48,-50,-51,-52,-58,-54,-55,-56,]),'EQ':([64,65,66,67,68,121,122,123,124,125,126,128,141,168,181,],[93,-45,-49,-53,-57,-46,-47,-48,-50,-51,-52,-58,-54,-55,-56,]),'MINUS':([64,65,66,67,68,87,117,118,119,120,121,122,123,124,125,126,128,141,168,181,],[95,-45,-49,-53,-57,95,95,95,95,95,-46,-47,-48,-50,-51,-52,-58,-54,-55,-56,]),'OR':([64,65,66,67,68,87,117,118,119,120,121,122,123,124,125,126,128,141,168,181,],[96,-45,-49,-53,-57,96,96,96,96,96,-46,-47,-48,-50,-51,-52,-58,-54,-55,-56,]),'TIMES':([65,66,67,68,121,122,123,124,125,126,128,141,168,181,],[97,-49,-53,-57,97,97,97,-50,-51,-52,-58,-54,-55,-56,]),'DIVIDE':([65,66,67,68,121,122,123,124,125,126,128,141,168,181,],[98,-49,-53,-57,98,98,98,-50,-51,-52,-58,-54,-55,-56,]),'AND':([65,66,67,68,121,122,123,124,125,126,128,141,168,181,],[99,-49,-53,-57,99,99,99,-50,-51,-52,-58,-54,-55,-56,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'V':([3,],[4,]),'empty':([3,4,6,9,12,24,36,39,49,50,58,60,88,104,106,129,134,143,144,146,153,165,170,174,],[5,8,10,16,21,40,21,40,71,21,40,83,40,21,21,40,40,156,21,21,166,40,21,180,]),'MAIN':([4,],[6,]),'P':([6,],[9,]),'VM':([7,],[11,]),'B':([9,54,],[13,75,]),'AUXPOSP':([9,],[14,]),'VM2':([12,36,50,104,106,144,146,170,],[18,52,72,131,133,157,159,176,]),'TIPO':([17,],[25,]),'ST':([24,39,58,88,129,134,165,],[38,55,80,116,143,147,174,]),'S':([24,39,58,88,129,134,165,],[39,39,39,39,39,39,39,]),'VAMC':([24,39,58,88,129,134,165,],[47,47,47,47,47,47,47,]),'CONDITION':([48,69,70,136,],[63,101,102,150,]),'UPDATE':([48,62,69,70,90,91,92,93,136,],[64,87,64,64,117,118,119,120,64,]),'T':([48,62,69,70,90,91,92,93,94,95,96,136,],[65,65,65,65,65,65,65,65,121,122,123,65,]),'F':([48,62,69,70,90,91,92,93,94,95,96,97,98,99,136,],[66,66,66,66,66,66,66,66,66,66,66,124,125,126,66,]),'AUXWHILE':([49,],[70,]),'IDNUM':([57,100,110,115,142,148,152,167,172,],[78,127,135,138,154,161,164,175,177,]),'SID':([60,],[81,]),'SID_T':([60,113,],[82,137,]),'AUXCOLON':([63,102,],[88,129,]),'AUXENDWHILE':([143,],[155,]),'AUXQ':([153,],[165,]),'AUXENDIF':([174,],[179,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM COLON V MAIN P B END','program',7,'p_program','MathPi.py',23),
  ('MAIN -> empty','MAIN',1,'p_MAIN','MathPi.py',27),
  ('V -> V VAR VM COLON TIPO','V',5,'p_V','MathPi.py',41),
  ('V -> empty','V',1,'p_V','MathPi.py',42),
  ('VM -> ID VM2','VM',2,'p_VM','MathPi.py',46),
  ('VM -> ID SQBL NUMBER SQBR VM2','VM',5,'p_VM_array','MathPi.py',51),
  ('VM -> ID SQBL NUMBER COMMA NUMBER SQBR VM2','VM',7,'p_VM_matrix','MathPi.py',56),
  ('VM -> ID SQBL NUMBER COMMA NUMBER COMMA NUMBER SQBR VM2','VM',9,'p_VM_cube','MathPi.py',61),
  ('VM2 -> COMMA ID VM2','VM2',3,'p_VM2','MathPi.py',66),
  ('VM2 -> COMMA ID SQBL NUMBER SQBR VM2','VM2',6,'p_VM2_array','MathPi.py',71),
  ('VM2 -> COMMA ID SQBL NUMBER COMMA NUMBER SQBR VM2','VM2',8,'p_VM2_matrix','MathPi.py',76),
  ('VM2 -> COMMA ID SQBL NUMBER COMMA NUMBER COMMA NUMBER SQBR VM2','VM2',10,'p_VM2_cube','MathPi.py',81),
  ('VM2 -> empty','VM2',1,'p_VM2_empty','MathPi.py',86),
  ('TIPO -> FLOAT','TIPO',1,'p_TIPO','MathPi.py',91),
  ('TIPO -> INT','TIPO',1,'p_TIPO','MathPi.py',92),
  ('TIPO -> ARRAY_INT','TIPO',1,'p_TIPO','MathPi.py',93),
  ('TIPO -> ARRAY_FLOAT','TIPO',1,'p_TIPO','MathPi.py',94),
  ('TIPO -> MATRIX_INT','TIPO',1,'p_TIPO','MathPi.py',95),
  ('TIPO -> MATRIX_FLOAT','TIPO',1,'p_TIPO','MathPi.py',96),
  ('TIPO -> CUBE_INT','TIPO',1,'p_TIPO','MathPi.py',97),
  ('TIPO -> CUBE_FLOAT','TIPO',1,'p_TIPO','MathPi.py',98),
  ('TIPO -> BOOL','TIPO',1,'p_TIPO','MathPi.py',99),
  ('P -> P AUXPOSP PROCEDURE ID COLON B ENDP','P',7,'p_P','MathPi.py',113),
  ('P -> empty','P',1,'p_P_empty','MathPi.py',122),
  ('AUXPOSP -> empty','AUXPOSP',1,'p_AUXPOSP','MathPi.py',127),
  ('B -> BEGIN COLON ST','B',3,'p_B','MathPi.py',136),
  ('ST -> S ST','ST',2,'p_ST','MathPi.py',140),
  ('ST -> empty','ST',1,'p_ST','MathPi.py',141),
  ('S -> FOR ID IN ID COLON ST ENDF','S',7,'p_S','MathPi.py',149),
  ('S -> DO COLON ST DWHILE COLON CONDITION ENDDO','S',7,'p_S','MathPi.py',150),
  ('S -> GOSUB ID','S',2,'p_S_GOSUB','MathPi.py',156),
  ('S -> PRINT PARL SID PARR','S',4,'p_S_PRINT','MathPi.py',168),
  ('SID -> SID PLUS SID_T','SID',3,'p_SID','MathPi.py',180),
  ('SID -> SID_T','SID',1,'p_SID2','MathPi.py',184),
  ('SID_T -> STRING','SID_T',1,'p_SID_T','MathPi.py',188),
  ('SID_T -> ID','SID_T',1,'p_SID_T','MathPi.py',189),
  ('SID -> empty','SID',1,'p_SID2_empty','MathPi.py',199),
  ('S -> INPUT PARL ID PARR','S',4,'p_S_input','MathPi.py',208),
  ('S -> INPUT PARL ID SQBL IDNUM SQBR PARR','S',7,'p_S_input_array_id','MathPi.py',215),
  ('S -> INPUT PARL ID SQBL IDNUM COMMA IDNUM SQBR PARR','S',9,'p_S_input_matrix_id','MathPi.py',223),
  ('S -> INPUT PARL ID SQBL IDNUM COMMA IDNUM COMMA IDNUM SQBR PARR','S',11,'p_S_input_cube_id','MathPi.py',231),
  ('IDNUM -> ID','IDNUM',1,'p_id_number','MathPi.py',239),
  ('IDNUM -> NUMBER','IDNUM',1,'p_id_number','MathPi.py',240),
  ('S -> VAMC ASSIGN UPDATE','S',3,'p_S_ASSIGN','MathPi.py',255),
  ('UPDATE -> T','UPDATE',1,'p_update','MathPi.py',260),
  ('UPDATE -> UPDATE PLUS T','UPDATE',3,'p_update2','MathPi.py',264),
  ('UPDATE -> UPDATE MINUS T','UPDATE',3,'p_update2','MathPi.py',265),
  ('UPDATE -> UPDATE OR T','UPDATE',3,'p_update2','MathPi.py',266),
  ('T -> F','T',1,'p_T','MathPi.py',271),
  ('T -> T TIMES F','T',3,'p_T2','MathPi.py',275),
  ('T -> T DIVIDE F','T',3,'p_T2','MathPi.py',276),
  ('T -> T AND F','T',3,'p_T2','MathPi.py',277),
  ('F -> ID','F',1,'p_F','MathPi.py',283),
  ('F -> ID SQBL IDNUM SQBR','F',4,'p_F_array','MathPi.py',292),
  ('F -> ID SQBL IDNUM COMMA IDNUM SQBR','F',6,'p_F_matrix','MathPi.py',302),
  ('F -> ID SQBL IDNUM COMMA IDNUM COMMA IDNUM SQBR','F',8,'p_F_cube','MathPi.py',311),
  ('F -> NUMBER','F',1,'p_F_NUMBER','MathPi.py',322),
  ('F -> PARL CONDITION PARR','F',3,'p_FtoE','MathPi.py',327),
  ('VAMC -> ID','VAMC',1,'p_vamc','MathPi.py',332),
  ('VAMC -> ID SQBL IDNUM SQBR','VAMC',4,'p_vamc_array','MathPi.py',337),
  ('VAMC -> ID SQBL IDNUM COMMA IDNUM SQBR','VAMC',6,'p_vamc_matrix','MathPi.py',343),
  ('VAMC -> ID SQBL IDNUM COMMA IDNUM COMMA IDNUM SQBR','VAMC',8,'p_vamc_cube','MathPi.py',349),
  ('S -> IF CONDITION AUXCOLON ST ENDIF','S',5,'p_S_IF','MathPi.py',356),
  ('S -> IF CONDITION AUXCOLON ST ELSE COLON AUXQ ST AUXENDIF ENDIF','S',10,'p_S_IF2','MathPi.py',367),
  ('AUXQ -> empty','AUXQ',1,'p_AUXQ','MathPi.py',372),
  ('AUXENDIF -> empty','AUXENDIF',1,'p_AUXENDIF','MathPi.py',384),
  ('S -> WHILE AUXWHILE CONDITION AUXCOLON ST AUXENDWHILE ENDW','S',7,'p_S_WHILE','MathPi.py',395),
  ('AUXWHILE -> empty','AUXWHILE',1,'p_AUXWHILE','MathPi.py',399),
  ('AUXENDWHILE -> empty','AUXENDWHILE',1,'p_AUXENDWHILE','MathPi.py',404),
  ('CONDITION -> UPDATE','CONDITION',1,'p_CONDITION','MathPi.py',468),
  ('CONDITION -> UPDATE NE UPDATE','CONDITION',3,'p_CONDITION2','MathPi.py',472),
  ('CONDITION -> UPDATE GT UPDATE','CONDITION',3,'p_CONDITION2','MathPi.py',473),
  ('CONDITION -> UPDATE LT UPDATE','CONDITION',3,'p_CONDITION2','MathPi.py',474),
  ('CONDITION -> UPDATE EQ UPDATE','CONDITION',3,'p_CONDITION2','MathPi.py',475),
  ('AUXCOLON -> COLON','AUXCOLON',1,'p_AUXCOLON','MathPi.py',481),
  ('empty -> <empty>','empty',0,'p_empty','MathPi.py',496),
]
