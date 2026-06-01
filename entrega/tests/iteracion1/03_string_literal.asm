.data
str0: .asciiz "hola"
str1: .asciiz "rara"
.text
.globl main
main:
la $a0, str0
li $v0, 4
syscall
li $a0, 10
li $v0, 11
syscall
la $a0, str1
li $v0, 4
syscall
li $a0, 10
li $v0, 11
syscall
li $v0, 10
syscall