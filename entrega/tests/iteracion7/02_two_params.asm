.data
var_a: .word 0
var_b: .word 0
.text
.globl main
main:
li $t0, 3
li $t1, 4
move $a0, $t0
move $a1, $t1
jal func_suma
move $t2, $v0
move $a0, $t2
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $t0, 10
li $t1, 20
move $a0, $t0
move $a1, $t1
jal func_suma
move $t2, $v0
move $a0, $t2
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $v0, 10
syscall
func_suma:
sw $a0, var_a
sw $a1, var_b
lw $t0, var_a
lw $t1, var_b
add $t2, $t0, $t1
move $v0, $t2
jr $ra
jr $ra