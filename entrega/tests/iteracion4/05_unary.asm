.text
.globl main
main:
li $t0, 8
sub $t1, $zero, $t0
move $a0, $t1
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $t0, 5
sub $t1, $zero, $t0
sub $t2, $zero, $t1
move $a0, $t2
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $t0, 0
sub $t1, $zero, $t0
move $a0, $t1
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $v0, 10
syscall