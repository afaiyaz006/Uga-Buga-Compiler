# Uga-Buga Compiler

A simple compiler that converts mathematical expression like this:
```
a=10
b=20
c=10+(20*3)+10-b
```
Into 8086 assembly code like this:
```
.MODEL SMALL
.STACK 100H
.DATA
t1 DB 10
t2 DB 20
t3 DB 0
t4 DB 0
t5 DB 0
t6 DB 0
t7 DB t6
.CODE
MAIN PROC
MOV AX,@DATA
MOV DS,AX
MOV AX,0
MOV AL,10
ADD AL,20
MOV t3,AL
MOV AL,10
SUB AL,20
MOV t4,AL
MOV AL,3
ADD AL,t4
MOV t5,AL
MOV AL,t3
MOV BL,t5
MUL BL
MOV t6,AL
MAIN ENDP
END MAIN
```
It is my final project for compiler course and built for educational purpose only.It is buggy and incomplete.
