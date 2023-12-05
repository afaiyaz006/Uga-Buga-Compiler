# Uga-Buga Compiler

A simple compiler that converts mathematical expression like this:
```
a=10
b=20
c=10+20*3+(10-b)
```
Into 8086 assembly code like this:
```
.MODEL SMALL
.STACK 100H
.DATA
t1 DB 1
t2 DB 0
t3 DB t2
t4 DB 0
t5 DB 0
t6 DB t5
t7 DB 10
t8 DB 0
t9 DB 0
t10 DB 0
t11 DB t10
.CODE
MAIN PROC
MOV AX,@DATA
MOV DS,AX
MOV AX,0
MOV AL,10
ADD AL,20
MOV t2,AL
MOV AL,10
ADD AL,20
MOV t4,AL
MOV AL,1
ADD AL,t4
MOV t5,AL
MOV AL,10
ADD AL,20
MOV t8,AL
MOV AL,1
ADD AL,t8
MOV t9,AL
MOV AL,t9
SUB AL,10
MOV t10,AL
MAIN ENDP
END MAIN
```
It is my final project for compiler course and built for educational purpose only.It is buggy and incomplete.