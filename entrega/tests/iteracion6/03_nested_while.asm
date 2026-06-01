.data
var_i: .word 0
var_j: .word 0
.text
.globl main
main:
li $t0, 1
sw $t0, var_i
while_start_1:
lw $t0, var_i
li $t1, 3
slt $t2, $t0, $t1
beq $t2, $zero, while_end_1
li $t3, 1
sw $t3, var_j
while_start_2:
lw $t0, var_j
li $t1, 3
slt $t2, $t0, $t1
beq $t2, $zero, while_end_2
lw $t3, var_i
lw $t4, var_j
add $t5, $t3, $t4
move $a0, $t5
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
lw $t0, var_j
li $t1, 1
add $t2, $t0, $t1
sw $t2, var_j
b while_start_2
while_end_2:
lw $t0, var_i
li $t1, 1
add $t2, $t0, $t1
sw $t2, var_i
b while_start_1
while_end_1:
li $v0, 10
syscall