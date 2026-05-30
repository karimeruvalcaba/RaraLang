.data
var_b: .word 0
.text
.globl main
main:
lw $a0, var_b
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $v0, 10
syscall