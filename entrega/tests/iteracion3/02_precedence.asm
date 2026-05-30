.text
.globl main
main:
li $t0, 2
li $t1, 3
li $t2, 4
mult $t1, $t2
mflo $t3
add $t4, $t0, $t3
move $a0, $t4
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $t0, 2
li $t1, 3
add $t2, $t0, $t1
li $t3, 4
mult $t2, $t3
mflo $t4
move $a0, $t4
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $v0, 10
syscall