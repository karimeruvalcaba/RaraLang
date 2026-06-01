.data
var_x: .word 0
.text
.globl main
main:
li $t0, 8
sw $t0, var_x
lw $t0, var_x
li $t1, 0
sgt $t2, $t0, $t1
li $t3, 1
add $t4, $t2, $t3
move $a0, $t4
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
lw $t0, var_x
li $t1, 0
seq $t2, $t0, $t1
li $t3, 10
add $t4, $t2, $t3
move $a0, $t4
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $v0, 10
syscall