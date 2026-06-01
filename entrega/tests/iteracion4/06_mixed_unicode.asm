.text
.globl main
main:
li $t0, 10
li $t1, 3
div $t0, $t1
mfhi $t2
li $t3, 4
li $t4, 5
sll $t5, $t3, 1
add $t5, $t5, $t4
add $t6, $t2, $t5
sra $t6, $t6, 1
move $a0, $t6
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $t0, 3
li $t1, 2
add $t2, $t0, $t1
sub $t3, $zero, $t2
move $a0, $t3
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $v0, 10
syscall