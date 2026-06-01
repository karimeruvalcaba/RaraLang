.data
var_n: .word 0
.text
.globl main
main:
li $t0, 3
move $a0, $t0
jal func_cuadrado
move $t1, $v0
li $t2, 1
add $t3, $t1, $t2
move $a0, $t3
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $t0, 4
move $a0, $t0
jal func_cuadrado
move $t1, $v0
li $t2, 2
mult $t1, $t2
mflo $t3
move $a0, $t3
li $v0, 1
syscall
li $a0, 10
li $v0, 11
syscall
li $v0, 10
syscall
func_cuadrado:
sw $a0, var_n
lw $t0, var_n
lw $t1, var_n
mult $t0, $t1
mflo $t2
move $v0, $t2
jr $ra
jr $ra