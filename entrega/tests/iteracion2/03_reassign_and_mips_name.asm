.data
var_add: .word 0
.text
.globl main
main:
li $t0, 5
sw $t0, var_add
lw $t0, var_add
move $a0, $t0
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $t0, 20
sw $t0, var_add
lw $t0, var_add
move $a0, $t0
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $v0, 10
syscall