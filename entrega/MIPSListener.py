from antlr.RaraLangListener import RaraLangListener


class MIPSListener(RaraLangListener):
    def __init__(self):
        self.data = []
        self.text = []
        self.string_count = 0
        self.variables = set()
        self.reg_stack = []
        self.temp_count = 0

    def enterProg(self, ctx):
        self.text.append(".text")
        self.text.append(".globl main")
        self.text.append("main:")

    def exitProg(self, ctx):
        self.text.append("li $v0, 10")
        self.text.append("syscall")

    def declare_variable(self, name: str):
        if name not in self.variables:
            self.variables.add(name)
            self.data.append(f"var_{name}: .word 0")

    def new_temp(self):
        reg = f"$t{self.temp_count}"
        self.temp_count += 1

        if self.temp_count > 9:
            raise Exception("Se acabaron los registros temporales $t0-$t9")

        return reg

    def push_reg(self, reg):
        self.reg_stack.append(reg)

    def pop_reg(self):
        if not self.reg_stack:
            raise Exception("Pila de registros vacía")
        return self.reg_stack.pop()

    def exitInt(self, ctx):
        reg = self.new_temp()
        value = int(ctx.INT().getText())
        self.text.append(f"li {reg}, {value}")
        self.push_reg(reg)

    def exitBased(self, ctx):
        raw = ctx.BASED_NUMBER().getText()
        content = raw[1:-1]
        digits, base = content.split(":")
        value = int(digits, int(base))

        reg = self.new_temp()
        self.text.append(f"li {reg}, {value}")
        self.push_reg(reg)

    def exitString(self, ctx):
        raw = ctx.STRING().getText()
        value = raw[1:-1]
        label = f"str{self.string_count}"
        self.string_count += 1

        self.data.append(f'{label}: .asciiz "{value}"')
        self.push_reg(label)

    def exitVar(self, ctx):
        name = ctx.ID().getText()
        self.declare_variable(name)

        reg = self.new_temp()
        self.text.append(f"lw {reg}, var_{name}")
        self.push_reg(reg)

    def exitParen(self, ctx):
        #No hace falta generar codigo aca, La expresión dentro del paréntesis ya deja su resultado en la pila.
        pass

#    def exitAddSub(self, ctx):
#        right = self.pop_reg()
#        left = self.pop_reg()
#        result = self.new_temp()
#
#        op = ctx.op.text
#
#        if op == "+":
#            self.text.append(f"add {result}, {left}, {right}")
#        elif op == "-":
#            self.text.append(f"sub {result}, {left}, {right}")
#
#        self.push_reg(result)

    def exitBinaryExpr(self, ctx):
        right = self.pop_reg()
        left = self.pop_reg()
        result = self.new_temp()

        op = ctx.op.text

        if op == "+":
            self.text.append(f"add {result}, {left}, {right}")

        elif op == "-":
            self.text.append(f"sub {result}, {left}, {right}")

        elif op == "⊞":
            self.text.append(f"div {left}, {right}")
            self.text.append(f"mfhi {result}")

        elif op == "⊠":
            self.text.append(f"sll {result}, {left}, 1")
            self.text.append(f"add {result}, {result}, {right}")

        self.push_reg(result)

    def exitMulDiv(self, ctx):
        right = self.pop_reg()
        left = self.pop_reg()
        result = self.new_temp()

        op = ctx.op.text

        if op == "×":
            self.text.append(f"mult {left}, {right}")
            self.text.append(f"mflo {result}")
        elif op == "÷":
            self.text.append(f"div {left}, {right}")
            self.text.append(f"mflo {result}")

        self.push_reg(result)

    def exitAssignStmt(self, ctx):
        name = ctx.ID().getText()
        self.declare_variable(name)

        value_reg = self.pop_reg()
        self.text.append(f"sw {value_reg}, var_{name}")

        self.reset_temporaries

    def exitPrintStmt(self, ctx):
        value = self.pop_reg()

        if isinstance(value, str) and value.startswith("str"):
            self.text.append(f"la $a0, {value}")
            self.text.append("li $v0, 4")
            self.text.append("syscall")
        else:
            self.text.append(f"move $a0, {value}")
            self.text.append("li $v0, 1")
            self.text.append("syscall")

        self.text.append("li $a0, 10")
        self.text.append("li $v0, 11")
        self.text.append("syscall")

        self.reset_temporaries()

    def output(self) -> str:
        result = []

        if self.data:
            result.append(".data")
            result.extend(self.data)

        result.extend(self.text)
        return "\n".join(result)
    
    def reset_temporaries(self):
        self.reg_stack = []
        self.temp_count = 0