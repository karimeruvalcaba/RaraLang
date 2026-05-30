.data
var_x: .word 0
var_y: .word 0
.text
.globl main
main:
li $t0, 10
sw $t0, var_x
li $t1, 3
sw $t1, var_y
lw $t2, var_x
lw $t3, var_y
add $t4, $t2, $t3
move $a0, $t4
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
lw $t0, var_x
lw $t1, var_y
sub $t2, $t0, $t1
move $a0, $t2
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
lw $t0, var_x
lw $t1, var_y
mult $t0, $t1
mflo $t2
move $a0, $t2
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
lw $t0, var_x
lw $t1, var_y
div $t0, $t1
mflo $t2
move $a0, $t2
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $v0, 10
syscall