from antlr.RaraLangListener import RaraLangListener
from antlr.RaraLangParser import RaraLangParser


class _CtrlFrame:
    """Buffer para generar código de if/while con saltos."""
    def __init__(self, kind, label_id):
        self.kind = kind        # 'if' o 'while'
        self.label_id = label_id
        self.phase = 'cond'    # fase actual: 'cond', 'then', 'else', 'body'
        self.has_else = False
        self.cond_reg = None   # registro con el resultado de la condición
        self.buffers = {'cond': [], 'then': [], 'else': [], 'body': []}


class MIPSListener(RaraLangListener):
    def __init__(self):
        self.data = []
        self.text = []
        self.func_sections = []   # una lista por función declarada
        self.current_func = None  # lista activa mientras se genera una función
        self.in_func = False
        self.string_count = 0
        self.variables = set()
        self.reg_stack = []
        self.temp_count = 0
        self.label_count = 0
        self.ctrl_stack = []      # pila de _CtrlFrame activos

    # ─── Routing de emisión ───────────────────────────────────────────────────

    def emit(self, line):
        """Redirige la línea al buffer correcto según el contexto actual."""
        if self.ctrl_stack:
            frame = self.ctrl_stack[-1]
            frame.buffers[frame.phase].append(line)
        elif self.in_func:
            self.current_func.append(line)
        else:
            self.text.append(line)

    def new_label_id(self):
        self.label_count += 1
        return self.label_count

    # ─── Programa ─────────────────────────────────────────────────────────────

    def enterProg(self, ctx):
        self.text.append(".text")
        self.text.append(".globl main")
        self.text.append("main:")

    def exitProg(self, ctx):
        self.text.append("li $v0, 10")
        self.text.append("syscall")

    # ─── Variables ────────────────────────────────────────────────────────────

    def declare_variable(self, name: str):
        if name not in self.variables:
            self.variables.add(name)
            self.data.append(f"var_{name}: .word 0")

    # ─── Registros temporales ─────────────────────────────────────────────────

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

    def reset_temporaries(self):
        self.reg_stack = []
        self.temp_count = 0

    # ─── Literales ────────────────────────────────────────────────────────────

    def exitInt(self, ctx):
        reg = self.new_temp()
        value = int(ctx.INT().getText())
        self.emit(f"li {reg}, {value}")
        self.push_reg(reg)

    def exitBased(self, ctx):
        raw = ctx.BASED_NUMBER().getText()
        content = raw[1:-1]
        digits, base = content.split(":")
        value = int(digits, int(base))
        reg = self.new_temp()
        self.emit(f"li {reg}, {value}")
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
        self.emit(f"lw {reg}, var_{name}")
        self.push_reg(reg)

    def exitParen(self, ctx):
        pass

    # ─── Aritmética ───────────────────────────────────────────────────────────

    def exitBinaryExpr(self, ctx):
        right = self.pop_reg()
        left = self.pop_reg()
        result = self.new_temp()
        op = ctx.op.text

        if op == "+":
            self.emit(f"add {result}, {left}, {right}")
        elif op == "-":
            self.emit(f"sub {result}, {left}, {right}")
        elif op == "⊞":   # módulo
            self.emit(f"div {left}, {right}")
            self.emit(f"mfhi {result}")
        elif op == "⊠":   # doble más: 2a + b
            self.emit(f"sll {result}, {left}, 1")
            self.emit(f"add {result}, {result}, {right}")
        elif op == "≈":   # promedio entero (piso)
            self.emit(f"add {result}, {left}, {right}")
            self.emit(f"sra {result}, {result}, 1")   # desplazamiento aritmético = piso

        self.push_reg(result)

    def exitMulDiv(self, ctx):
        right = self.pop_reg()
        left = self.pop_reg()
        result = self.new_temp()
        op = ctx.op.text

        if op == "×":
            self.emit(f"mult {left}, {right}")
            self.emit(f"mflo {result}")
        elif op == "÷":
            self.emit(f"div {left}, {right}")
            self.emit(f"mflo {result}")

        self.push_reg(result)

    def exitUnaryExpr(self, ctx):
        """± : negación unaria. ±x = 0 - x."""
        operand = self.pop_reg()
        result = self.new_temp()
        self.emit(f"sub {result}, $zero, {operand}")
        self.push_reg(result)

    # ─── Comparaciones ────────────────────────────────────────────────────────

    def exitCompareExpr(self, ctx):
        """Produce 1 si la comparación es verdadera, 0 si no."""
        right = self.pop_reg()
        left = self.pop_reg()
        result = self.new_temp()
        op = ctx.op.text

        if op == "==":
            self.emit(f"seq {result}, {left}, {right}")
        elif op == "!=":
            self.emit(f"sne {result}, {left}, {right}")
        elif op == "<":
            self.emit(f"slt {result}, {left}, {right}")
        elif op == ">":
            self.emit(f"sgt {result}, {left}, {right}")

        self.push_reg(result)

    # ─── Sentencias básicas ───────────────────────────────────────────────────

    def exitAssignStmt(self, ctx):
        name = ctx.ID().getText()
        self.declare_variable(name)
        value_reg = self.pop_reg()
        self.emit(f"sw {value_reg}, var_{name}")
        self.reset_temporaries()

    def exitPrintStmt(self, ctx):
        value = self.pop_reg()

        if isinstance(value, str) and value.startswith("str"):
            self.emit(f"la $a0, {value}")
            self.emit("li $v0, 4")
            self.emit("syscall")
        else:
            self.emit(f"move $a0, {value}")
            self.emit("li $v0, 1")
            self.emit("syscall")

        self.emit("li $a0, 10")
        self.emit("li $v0, 11")
        self.emit("syscall")

        self.reset_temporaries()

    def exitBlockStmt(self, ctx):
        pass

    # ─── Control de flujo: if ─────────────────────────────────────────────────

    def enterIfStmt(self, ctx):
        frame = _CtrlFrame('if', self.new_label_id())
        self.ctrl_stack.append(frame)

    def exitIfStmt(self, ctx):
        frame = self.ctrl_stack.pop()
        cond_reg = frame.cond_reg
        lid = frame.label_id

        assembled = list(frame.buffers['cond'])

        if frame.has_else:
            assembled.append(f"beq {cond_reg}, $zero, if_else_{lid}")
            assembled.extend(frame.buffers['then'])
            assembled.append(f"b if_end_{lid}")
            assembled.append(f"if_else_{lid}:")
            assembled.extend(frame.buffers['else'])
        else:
            assembled.append(f"beq {cond_reg}, $zero, if_end_{lid}")
            assembled.extend(frame.buffers['then'])

        assembled.append(f"if_end_{lid}:")

        for line in assembled:
            self.emit(line)

        self.reset_temporaries()

    # ─── Control de flujo: while ──────────────────────────────────────────────

    def enterWhileStmt(self, ctx):
        frame = _CtrlFrame('while', self.new_label_id())
        self.ctrl_stack.append(frame)

    def exitWhileStmt(self, ctx):
        frame = self.ctrl_stack.pop()
        cond_reg = frame.cond_reg
        lid = frame.label_id

        assembled = []
        assembled.append(f"while_start_{lid}:")
        assembled.extend(frame.buffers['cond'])
        assembled.append(f"beq {cond_reg}, $zero, while_end_{lid}")
        assembled.extend(frame.buffers['body'])
        assembled.append(f"b while_start_{lid}")
        assembled.append(f"while_end_{lid}:")

        for line in assembled:
            self.emit(line)

        self.reset_temporaries()

    # ─── Detección de transición de fase ──────────────────────────────────────

    def enterEveryRule(self, ctx):
        """Detecta cuándo termina la condición de un if/while y empieza el cuerpo.

        Solo actúa cuando el nodo que se entra es un *stmt* (no la expr condición),
        ya que enterEveryRule también dispara para los hijos expr del if/while.
        """
        if not self.ctrl_stack:
            return

        frame = self.ctrl_stack[-1]

        # El filtro isinstance(ctx, StmtContext) excluye la expr condición,
        # que también es hija directa del ifStmt/whileStmt pero no es sentencia.
        if not isinstance(ctx, RaraLangParser.StmtContext):
            return

        if frame.kind == 'if':
            if isinstance(ctx.parentCtx, RaraLangParser.IfStmtContext):
                if frame.phase == 'cond':
                    # Primer stmt hijo del if → terminó la condición
                    frame.cond_reg = self.pop_reg()
                    frame.phase = 'then'
                elif frame.phase == 'then':
                    # Segundo stmt hijo → es el else
                    frame.has_else = True
                    frame.phase = 'else'

        elif frame.kind == 'while':
            if isinstance(ctx.parentCtx, RaraLangParser.WhileStmtContext):
                if frame.phase == 'cond':
                    # Stmt hijo del while → terminó la condición
                    frame.cond_reg = self.pop_reg()
                    frame.phase = 'body'

    # ─── Funciones ────────────────────────────────────────────────────────────

    def enterFuncDecl(self, ctx):
        name = ctx.ID().getText()
        params = [p.getText() for p in ctx.paramList().ID()]

        self.in_func = True
        self.current_func = []
        self.func_sections.append(self.current_func)

        self.current_func.append(f"func_{name}:")
        # Guardar argumentos ($a0-$a3) en variables de memoria
        for i, param in enumerate(params):
            self.declare_variable(param)
            self.current_func.append(f"sw $a{i}, var_{param}")

    def exitFuncDecl(self, ctx):
        # jr $ra al final por si el cuerpo no tiene return explícito
        self.current_func.append("jr $ra")
        self.in_func = False
        self.current_func = None
        self.reset_temporaries()

    def exitReturnStmt(self, ctx):
        value_reg = self.pop_reg()
        self.emit(f"move $v0, {value_reg}")
        self.emit("jr $ra")
        self.reset_temporaries()

    def exitCall(self, ctx):
        name = ctx.ID().getText()
        n_args = len(ctx.argList().expr())

        # Los args están en la pila en orden LIFO → invertir para $a0, $a1, ...
        arg_regs = [self.pop_reg() for _ in range(n_args)]
        arg_regs.reverse()

        for i, reg in enumerate(arg_regs):
            self.emit(f"move $a{i}, {reg}")

        # Si llamamos desde dentro de una función, $ra ya tiene valor → guardar en pila
        if self.in_func:
            self.emit("addi $sp, $sp, -4")
            self.emit("sw $ra, 0($sp)")

        self.emit(f"jal func_{name}")

        if self.in_func:
            self.emit("lw $ra, 0($sp)")
            self.emit("addi $sp, $sp, 4")

        result_reg = self.new_temp()
        self.emit(f"move {result_reg}, $v0")
        self.push_reg(result_reg)

    # ─── Salida ───────────────────────────────────────────────────────────────

    def output(self) -> str:
        result = []

        if self.data:
            result.append(".data")
            result.extend(self.data)

        result.extend(self.text)

        for func_code in self.func_sections:
            result.extend(func_code)

        return "\n".join(result)
