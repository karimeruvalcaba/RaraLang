.data
var_x: .word 0
var_n: .word 0
.text
.globl main
main:
li $t0, 3
sw $t0, var_x
lw $t0, var_x
li $t1, 0
sgt $t2, $t0, $t1
beq $t2, $zero, if_end_1
li $t3, 1
sw $t3, var_n
while_start_2:
lw $t0, var_n
li $t1, 4
slt $t2, $t0, $t1
beq $t2, $zero, while_end_2
lw $t3, var_n
move $a0, $t3
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
lw $t0, var_n
li $t1, 1
add $t2, $t0, $t1
sw $t2, var_n
b while_start_2
while_end_2:
if_end_1:
li $v0, 10
syscall