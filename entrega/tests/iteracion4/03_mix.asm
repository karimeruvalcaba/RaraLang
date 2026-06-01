.text
.globl main
main:
li $t0, 10
li $t1, 3
div $t0, $t1
mfhi $t2
li $t3, 1
add $t4, $t2, $t3
move $a0, $t4
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $v0, 10
syscall