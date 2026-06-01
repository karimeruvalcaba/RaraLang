.data
var_x: .word 0
var_y: .word 0
.text
.globl main
main:
li $t0, 10
sw $t0, var_x
li $t0, 5
sw $t0, var_y
lw $t0, var_x
li $t1, 0
sgt $t2, $t0, $t1
beq $t2, $zero, if_else_1
lw $t3, var_y
li $t4, 0
sgt $t5, $t3, $t4
beq $t5, $zero, if_else_2
li $t6, 1
move $a0, $t6
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
b if_end_2
if_else_2:
li $t0, 2
move $a0, $t0
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
if_end_2:
b if_end_1
if_else_1:
li $t0, 3
move $a0, $t0
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
if_end_1:
li $v0, 10
syscall