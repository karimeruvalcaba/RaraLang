from antlr.RaraLangListener import RaraLangListener
from antlr.RaraLangParser import RaraLangParser

class MIPSListener(RaraLangListener):
    def __init__(self):
        self.data = []
        self.text = []
        self.string_count = 0
        self.last_value = None
        self.last_type = None

    def enterProg(self, ctx):
        self.text.append(".text")
        self.text.append(".globl main")
        self.text.append("main:")


    def exitProg(self, ctx):
        self.text.append("li $v0, 10")
        self.text.append("syscall")
    
    def exitInt(self, ctx):
        self.last_value = int(ctx.INT().getText())
        self.last_type = "int"

    def exitBased(self, ctx):
        raw = ctx.BASED_NUMBER().getText()
        content = raw[1:-1]
        digits, base = content.split(":")
        self.last_value = int(digits, int(base))
        self.last_type = "int"

    def exitString(self, ctx):
        raw = ctx.STRING().getText()
        value = raw[1:-1]
        label = f"str{self.string_count}"
        self.string_count += 1

        self.data.append(f'{label}: .asciiz "{value}"')
        self.last_value = label
        self.last_type = "string"

    def exitPrintStmt(self, ctx):
        if self.last_type == "int":
            self.text.append(f"li $a0, {self.last_value}")
            self.text.append("li $v0, 1")
            self.text.append("syscall")
            self.text.append("li $a0, 10")
            self.text.append("li $v0, 11")
            self.text.append("syscall")

        elif self.last_type == "string":
            self.text.append(f"la $a0, {self.last_value}")
            self.text.append("li $v0, 4")
            self.text.append("syscall")
            self.text.append("li $a0, 10")
            self.text.append("li $v0, 11")
            self.text.append("syscall")

    def output(self) -> str:

        result = []
        if self.data:
            result.append(".data")
            result.extend(self.data)
        
        result.extend(self.text)
        return "\n".join(result)

