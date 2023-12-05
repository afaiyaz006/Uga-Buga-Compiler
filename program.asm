;{1: 't1 = a EQUAL 10', 2: 't2 = b EQUAL 30', 3: 't3 = 10 + 30', 4: 't4 = c EQUAL t3', 5: 't5 = x EQUAL 10', 6: 't6 = 2 + 4', 7: 't7 = 10 * t6', 8: 't8 = 3 + 5', 9: 't9 = t7 / t8', 10: 't10 = y EQUAL t9', 11: 't11 = 2 + 4', 12: 't12 = 10 * t11', 13: 't13 = 3 + 5', 14: 't14 = t12 / t13', 15: 't15 = 40 - t14', 16: 't16 = z EQUAL t15', 17: 't17 = 2 + 4', 18: 't18 = 10 * t17', 19: 't19 = 3 + 5', 20: 't20 = t18 / t19', 21: 't21 = 2 + 4', 22: 't22 = 10 * t21', 23: 't23 = 3 + 5', 24: 't24 = t22 / t23', 25: 't25 = 40 - t24', 26: 't26 = t20 + t25', 27: 't27 = p EQUAL t26'}
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
t12: DW 0
t13: DW 0
t14: DW 0
t15: DW 0
t16: DW 0
t17: DW 0
t18: DW 0
t19: DW 0
t20: DW 0
t21: DW 0
t22: DW 0
t23: DW 0
t24: DW 0
t25: DW 0
t26: DW 0
t27: DW 0
start:
MOV AX,10
ADD AX,30
MOV word t3,AX
MOV AX,2
ADD AX,4
MOV word t6,AX
MOV AX,word t6
MOV BX,10
MUL BL
MOV word t7,AX
MOV AX,3
ADD AX,5
MOV word t8,AX
MOV AX,word t7
MOV BX,word t8
DIV BL
MOV word t9,AX
MOV AX,2
ADD AX,4
MOV word t11,AX
MOV AX,word t11
MOV BX,10
MUL BL
MOV word t12,AX
MOV AX,3
ADD AX,5
MOV word t13,AX
MOV AX,word t12
MOV BX,word t13
DIV BL
MOV word t14,AX
MOV AX,40
SUB AX,word t14
MOV word t15,AX
MOV AX,2
ADD AX,4
MOV word t17,AX
MOV AX,word t17
MOV BX,10
MUL BL
MOV word t18,AX
MOV AX,3
ADD AX,5
MOV word t19,AX
MOV AX,word t18
MOV BX,word t19
DIV BL
MOV word t20,AX
MOV AX,2
ADD AX,4
MOV word t21,AX
MOV AX,word t21
MOV BX,10
MUL BL
MOV word t22,AX
MOV AX,3
ADD AX,5
MOV word t23,AX
MOV AX,word t22
MOV BX,word t23
DIV BL
MOV word t24,AX
MOV AX,40
SUB AX,word t24
MOV word t25,AX
MOV AX,word t20
ADD AX,word t25
MOV word t26,AX
