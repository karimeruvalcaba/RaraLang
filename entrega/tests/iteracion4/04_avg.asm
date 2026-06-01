.data
var_x: .word 0
var_y: .word 0
.text
.globl main
main:
li $t0, 7
li $t1, 3
add $t2, $t0, $t1
sra $t2, $t2, 1
move $a0, $t2
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $t0, 4
li $t1, 4
add $t2, $t0, $t1
sra $t2, $t2, 1
move $a0, $t2
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $t0, 3
sub $t1, $zero, $t0
sw $t1, var_x
li $t0, 1
sub $t1, $zero, $t0
sw $t1, var_y
lw $t0, var_x
lw $t1, var_y
add $t2, $t0, $t1
sra $t2, $t2, 1
move $a0, $t2
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $v0, 10
syscall