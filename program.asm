;{1: 't1 = 2 + 3', 2: 't2 = 3 * 2', 3: 't3 = 5 + t2', 4: 't4 = 4 * t3', 5: 't5 = t4 / 3', 6: 't6 = t1 + t5', 7: 't7 = 3 / 2', 8: 't8 = 5 + t7', 9: 't9 = t8 * 2', 10: 't10 = t6 + t9', 11: 't11 = t10', 12: 't12 = 2 + 3', 13: 't13 = 3 * 2', 14: 't14 = 5 + t13', 15: 't15 = 4 * t14', 16: 't16 = t15 / 3', 17: 't17 = t12 + t16', 18: 't18 = 3 / 2', 19: 't19 = 5 + t18', 20: 't20 = t19 * 2', 21: 't21 = t17 + t20', 22: 't22 = 3 * t21', 23: 't23 = 2 + t22', 24: 't24 = t23 + 20', 25: 't25 = t24'}
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
start:
MOV AX,2
ADD AX,3
MOV word t1,AX
MOV AX,3
MOV BX,2
MUL BL
MOV word t2,AX
MOV AX,5
ADD AX,word t2
MOV word t3,AX
MOV AX,word t3
MOV BX,4
MUL BL
MOV word t4,AX
MOV AX,word t4
MOV BX,3
DIV BL
MOV word t5,AX
MOV AX,word t1
ADD AX,word t5
MOV word t6,AX
MOV AX,3
MOV BX,2
DIV BL
MOV word t7,AX
MOV AX,5
ADD AX,word t7
MOV word t8,AX
MOV AX,word t8
MOV BX,2
MUL BL
MOV word t9,AX
MOV AX,word t6
ADD AX,word t9
MOV word t10,AX
MOV AX,2
ADD AX,3
MOV word t12,AX
MOV AX,3
MOV BX,2
MUL BL
MOV word t13,AX
MOV AX,5
ADD AX,word t13
MOV word t14,AX
MOV AX,word t14
MOV BX,4
MUL BL
MOV word t15,AX
MOV AX,word t15
MOV BX,3
DIV BL
MOV word t16,AX
MOV AX,word t12
ADD AX,word t16
MOV word t17,AX
MOV AX,3
MOV BX,2
DIV BL
MOV word t18,AX
MOV AX,5
ADD AX,word t18
MOV word t19,AX
MOV AX,word t19
MOV BX,2
MUL BL
MOV word t20,AX
MOV AX,word t17
ADD AX,word t20
MOV word t21,AX
MOV AX,word t21
MOV BX,3
MUL BL
MOV word t22,AX
MOV AX,2
ADD AX,word t22
MOV word t23,AX
MOV AX,word t23
ADD AX,20
MOV word t24,AX
