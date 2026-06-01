.data
var_x: .word 0
var_y: .word 0
.text
.globl main
main:
li $t0, 5
sw $t0, var_x
li $t0, 10
sw $t0, var_y
lw $t0, var_x
lw $t1, var_y
seq $t2, $t0, $t1
move $a0, $t2
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
lw $t0, var_x
lw $t1, var_y
sne $t2, $t0, $t1
move $a0, $t2
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
lw $t0, var_x
lw $t1, var_y
slt $t2, $t0, $t1
move $a0, $t2
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
lw $t0, var_x
lw $t1, var_y
sgt $t2, $t0, $t1
move $a0, $t2
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $v0, 10
syscall