.text
.globl main
main:
li $t0, 10
li $t1, 3
div $t0, $t1
mflo $t2
move $a0, $t2
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $t0, 20
li $t1, 6
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