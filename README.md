# Uga-Buga Compiler

A simple compiler that converts mathematical expression like this:
```
a HOCCHE 10
b HOCCHE 20
c HOCCHE a+b
d HOCCHE c*3
e HOCCHE d/3
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
```
This code is completely executable in this [8086_Emulator](https://yjdoc2.github.io/8086-emulator-web/)
It is my final project for compiler course and built for educational purpose only.It is buggy and incomplete.
