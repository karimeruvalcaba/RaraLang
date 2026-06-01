.text
.globl main
main:
li $t0, 4
li $t1, 5
sll $t2, $t0, 1
add $t2, $t2, $t1
move $a0, $t2
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $t0, 2
li $t1, 10
sll $t2, $t0, 1
add $t2, $t2, $t1
move $a0, $t2
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $v0, 10
syscall