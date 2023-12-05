# Uga-Buga Compiler

A simple compiler that converts mathematical expression like this:
```
a=10
b=30
c=a+b
x=10
y=(10*2)+(4/3)+5
z=40-y
p=y+z
```
Into 8086 assembly code like this:
```
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
MOV AX,10
MOV BX,2
MUL BL
MOV word t6,AX
MOV AX,4
MOV BX,3
DIV BL
MOV word t7,AX
MOV AX,word t6
ADD AX,word t7
MOV word t8,AX
MOV AX,word t8
ADD AX,5
MOV word t9,AX
MOV AX,10
MOV BX,2
MUL BL
MOV word t11,AX
MOV AX,4
MOV BX,3
DIV BL
MOV word t12,AX
MOV AX,word t11
ADD AX,word t12
MOV word t13,AX
MOV AX,word t13
ADD AX,5
MOV word t14,AX
MOV AX,40
SUB AX,word t14
MOV word t15,AX
MOV AX,10
MOV BX,2
MUL BL
MOV word t17,AX
MOV AX,4
MOV BX,3
DIV BL
MOV word t18,AX
MOV AX,word t17
ADD AX,word t18
MOV word t19,AX
MOV AX,word t19
ADD AX,5
MOV word t20,AX
MOV AX,10
MOV BX,2
MUL BL
MOV word t21,AX
MOV AX,4
MOV BX,3
DIV BL
MOV word t22,AX
MOV AX,word t21
ADD AX,word t22
MOV word t23,AX
MOV AX,word t23
ADD AX,5
MOV word t24,AX
MOV AX,40
SUB AX,word t24
MOV word t25,AX
MOV AX,word t20
ADD AX,word t25
MOV word t26,AX
```
It is my final project for compiler course and built for educational purpose only.It is buggy and incomplete.
