;{1: 't1 = a EQUAL 10', 2: 't2 = b EQUAL 20', 3: 't3 = 10 + 20', 4: 't4 = c EQUAL t3', 5: 't5 = 10 + 20', 6: 't6 = t5 * 3', 7: 't7 = d EQUAL t6', 8: 't8 = 10 + 20', 9: 't9 = t8 * 3', 10: 't10 = t9 / 3', 11: 't11 = e EQUAL t10'}
t1: DW 0
t2: DW 0
t3: DW 0
t4: DW 0
t5: DW 0
t6: DW 0
t7: DW 0
t8: DW 0
t9: DW 0
t10: DW 0
t11: DW 0
start:
MOV AX,10
ADD AX,20
MOV word t3,AX
MOV AX,10
ADD AX,20
MOV word t5,AX
MOV AX,word t5
MOV BX,3
MUL BL
MOV word t6,AX
MOV AX,10
ADD AX,20
MOV word t8,AX
MOV AX,word t8
MOV BX,3
MUL BL
MOV word t9,AX
MOV AX,word t9
MOV BX,3
DIV BL
MOV word t10,AX
