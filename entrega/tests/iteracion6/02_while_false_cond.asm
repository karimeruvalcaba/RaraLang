.data
var_x: .word 0
.text
.globl main
main:
li $t0, 10
sw $t0, var_x
while_start_1:
lw $t0, var_x
li $t1, 5
slt $t2, $t0, $t1
beq $t2, $zero, while_end_1
lw $t3, var_x
move $a0, $t3
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
lw $t0, var_x
li $t1, 1
add $t2, $t0, $t1
sw $t2, var_x
b while_start_1
while_end_1:
li $t0, 99
move $a0, $t0
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $v0, 10
syscall