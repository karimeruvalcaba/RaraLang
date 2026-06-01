.data
var_x: .word 0
.text
.globl main
main:
li $t0, 5
move $a0, $t0
jal func_doble
move $t1, $v0
move $a0, $t1
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $t0, 3
move $a0, $t0
jal func_doble
move $t1, $v0
move $a0, $t1
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $v0, 10
syscall
func_doble:
sw $a0, var_x
lw $t0, var_x
lw $t1, var_x
add $t2, $t0, $t1
move $v0, $t2
jr $ra
jr $ra