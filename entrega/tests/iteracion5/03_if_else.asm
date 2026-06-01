.data
var_x: .word 0
var_y: .word 0
.text
.globl main
main:
li $t0, 7
sw $t0, var_x
lw $t0, var_x
li $t1, 5
sgt $t2, $t0, $t1
beq $t2, $zero, if_else_1
li $t3, 1
move $a0, $t3
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
b if_end_1
if_else_1:
li $t0, 0
move $a0, $t0
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
if_end_1:
li $t0, 2
sw $t0, var_y
lw $t0, var_y
li $t1, 5
sgt $t2, $t0, $t1
beq $t2, $zero, if_else_2
li $t3, 1
move $a0, $t3
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
b if_end_2
if_else_2:
li $t0, 0
move $a0, $t0
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
if_end_2:
li $v0, 10
syscall