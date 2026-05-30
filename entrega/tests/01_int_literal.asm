.text
.globl main
main:
li $a0, 42
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $a0, 0
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $a0, 100
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $v0, 10
syscall