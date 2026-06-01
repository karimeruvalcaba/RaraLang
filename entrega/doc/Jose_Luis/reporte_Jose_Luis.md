# Template: reporte de iteración (para pedir al LLM)

Copia este prompt al final de cada iteración y pégalo en Open Code.
Sustituye los campos entre `[corchetes]` antes de enviarlo.

---

## Prompt para el LLM

> Acabamos de terminar la iteración [NÚMERO] del compilador RaraLang.
> El tema de esta iteración fue: [TEMA, ej: "aritmética básica con + - × ÷"].
>
> Por favor genera un reporte de lo que implementamos con este formato exacto:
>
> ---
>
> **Iteración [NÚMERO] — [TEMA]**
>
> **¿Qué hace el compilador ahora que no hacía antes?**
> {{Describir en 2–3 oraciones qué feature se agregó y qué tipo de programas RaraLang
> puede compilar ahora que antes no podía.}}
>
> **¿Qué se agregó a la gramática?**
> {{Describir en lenguaje natural los tokens o reglas nuevas. No escribir código ANTLR,
> solo explicar qué construcciones nuevas acepta el lenguaje ahora.}}
>
> **¿Qué métodos del Listener se implementaron?**
> {{Listar los métodos exit*/enter* que se escribieron en esta iteración y describir
> en una línea qué hace cada uno.}}
>
> **¿Qué decisión técnica tomaste que no estaba explícita en la especificación?**
> {{Describir al menos una decisión de implementación que tuviste que tomar porque
> la especificación era ambigua o incompleta. Explicar qué elegiste y por qué.}}
>
> **Pruebas que pasan:**
> {{Listar los archivos .rara de la iteración que corren correctamente en QtSPIM,
> con el valor que imprime cada uno.}}
>
> **Limitaciones conocidas:**
> {{Describir qué casos del lenguaje aún no maneja el compilador, o qué errores
> produce de forma silenciosa en lugar de reportarlos.}}
>
> ---

---

## Qué hacer con el reporte

Una vez que el LLM lo genere:

1. **Léelo completo** antes de copiarlo a tu entrega.
2. En la sección "¿Qué decisión técnica tomaste?", verifica que la decisión que
   describe sea real — que efectivamente esté en el código generado. Si inventó algo
   que no está, repórtalo.
3. En "Pruebas que pasan", abre cada archivo `.rara` y confirma que el valor que
   dice el reporte es el que QtSPIM muestra. Si hay diferencia, repórtalo.
4. En "Limitaciones conocidas", agrega cualquier cosa que tú hayas notado y el
   modelo no mencionó.
5. Firma el reporte con una línea al final:
   > *Revisado por [tu nombre]. Correcciones: [lo que cambiaste, o "ninguna"].*

---

# Reporte de iteraciones — Jose Luis

---

**Iteración 4 — Operadores Unicode enteros (≈ y ±)**

**¿Qué hace el compilador ahora que no hacía antes?**
El compilador ahora soporta los cuatro operadores Unicode de la iteración: módulo (`⊞`), doble-más (`⊠`), promedio entero (`≈`) y negación unaria (`±`). Los primeros dos los implementó mi pareja; yo agregué `≈` y `±`. Ahora se pueden escribir expresiones como `print 7 ≈ 3` o `print ±x` y generar MIPS válido.

**¿Qué se agregó a la gramática?**
Se añadieron dos tokens nuevos: `AVG` para el símbolo `≈` y `UNARY` para `±`. El `AVG` se agregó como operador binario en la regla de adición (mismo nivel que `+` y `-`). El `±` se puso como alternativa en la regla `factor`, de la forma `UNARY factor`, lo que le da la mayor precedencia posible.

**¿Qué métodos del Listener se implementaron?**
- `exitBinaryExpr` (caso `≈`): suma los dos operandos y aplica `sra` (shift aritmético derecho) para obtener el piso de la división entre 2.
- `exitUnaryExpr`: saca el operando de la pila y emite `sub result, $zero, operand` para negarlo.

**¿Qué decisión técnica tomaste que no estaba explícita en la especificación?**
Para `≈` usé `sra` (desplazamiento aritmético) en lugar de `div $t, 2` o `srl`. La especificación dice "piso" (redondear hacia menos infinito), y `sra` lo hace correctamente para números negativos porque preserva el signo. `srl` (lógico) daría resultados incorrectos con negativos, y `div` trunca hacia cero que tampoco es piso. Decidí usar `sra` por eso.

**Pruebas que pasan:**
- `04_avg.rara`: `7 ≈ 3` → 5, `4 ≈ 4` → 4, `(-3) ≈ (-1)` → -2
- `05_unary.rara`: `±8` → -8, `±±5` → 5, `±0` → 0
- `06_mixed_unicode.rara`: `(10 ⊞ 3) ≈ (4 ⊠ 5)` → 7, `±(3+2)` → -5

**Limitaciones conocidas:**
`≈` con resultado impar trunca hacia abajo (comportamiento correcto según la spec). No hay validación de tipos ni de overflow.

*Revisado por Jose Luis. Correcciones: ninguna.*

---

**Iteración 5 — Comparaciones e if/then/else**

**¿Qué hace el compilador ahora que no hacía antes?**
El compilador puede tomar decisiones. Soporta los cuatro comparadores (`==`, `!=`, `<`, `>`) que producen 0 o 1, y la sentencia `if expr then stmt else stmt` con el else opcional. Los bloques then/else pueden ser cualquier sentencia válida, incluyendo ifs anidados.

**¿Qué se agregó a la gramática?**
Se añadieron los tokens `EQ`, `NEQ`, `LT`, `GT`, las palabras clave `IF`, `THEN`, `ELSE`, y una nueva regla de expresión `expr` por encima de la expresión aritmética para que las comparaciones tengan menor precedencia que los operadores aritméticos. La sentencia `ifStmt` se agregó como alternativa de `stmt`.

**¿Qué métodos del Listener se implementaron?**
- `exitCompareExpr`: saca dos operandos de la pila y emite `seq`/`sne`/`slt`/`sgt` según el operador.
- `enterIfStmt`: crea un `_CtrlFrame` con buffers separados para condición, then y else, y lo apila.
- `exitIfStmt`: saca el frame, ensambla los tres buffers con `beq`, saltos y etiquetas únicas.
- `enterEveryRule` (extensión): detecta cuando el primer `stmt` hijo del `ifStmt` está por entrar y cambia el buffer activo de `cond` a `then`, o de `then` a `else`.

**¿Qué decisión técnica tomaste que no estaba explícita en la especificación?**
`enterEveryRule` dispara para todos los hijos del `ifStmt`, incluyendo la expresión condición. Al principio intentaba hacer `pop_reg()` cuando veía cualquier hijo del if, lo que fallaba porque la condición aún no se había evaluado. Agregué un filtro `isinstance(ctx, StmtContext)` para que la transición solo ocurra cuando el hijo es una sentencia y no una expresión. Eso no estaba en la descripción del prompt.

**Pruebas que pasan:**
- `01_comparators.rara`: `5==10` → 0, `5!=10` → 1, `5<10` → 1, `5>10` → 0
- `02_if_no_else.rara`: `if 7>5` ejecuta print, `if 3>5` no ejecuta nada, imprime 0 al final
- `03_if_else.rara`: rama then con x=7, rama else con y=2 → imprime 1, luego 0
- `04_nested_if.rara`: x=10, y=5, ambas condiciones verdaderas → imprime 1
- `05_compare_in_expr.rara`: `(x>0)+1` → 2, `(x==0)+10` → 10

**Limitaciones conocidas:**
No hay cortocircuito en condiciones compuestas (no existe `and`/`or`). Las comparaciones solo funcionan con enteros, no con strings.

*Revisado por Jose Luis. Correcciones: ninguna.*

---

**Iteración 6 — While y bloques de sentencias**

**¿Qué hace el compilador ahora que no hacía antes?**
El compilador puede repetir código con `while`. Se soportan bloques `{ ... }` que agrupan múltiples sentencias como una sola, lo cual es necesario para que el cuerpo del while contenga más de una instrucción. Los while pueden anidarse y combinarse con if.

**¿Qué se agregó a la gramática?**
Se añadieron las palabras clave `WHILE` y `DO`, los tokens `LBRACE` y `RBRACE` para llaves, y dos nuevas alternativas de sentencia: `whileStmt` (`while expr do stmt`) y `blockStmt` (`{ stmt* }`).

**¿Qué métodos del Listener se implementaron?**
- `enterWhileStmt`: crea un `_CtrlFrame` con buffers para condición y cuerpo, genera un `label_id` único.
- `exitWhileStmt`: ensambla `while_start_N:`, código de condición, `beq ... while_end_N`, cuerpo, `b while_start_N`, `while_end_N:`.
- `exitBlockStmt`: vacío, las sentencias internas ya emitieron su código al buffer correcto.
- `enterEveryRule` (extensión): detecta también la transición de `cond` a `body` para el while.

**¿Qué decisión técnica tomaste que no estaba explícita en la especificación?**
El contador de etiquetas (`label_count`) es global y compartido entre ifs y whiles. Esto significa que si hay un if y después un while, los números no empiezan en 1 para cada tipo sino que continúan la secuencia. No cause ningún problema ya que solo importa que sean únicos, pero podría haber usado contadores separados. Elegí uno global por simplicidad.

**Pruebas que pasan:**
- `01_while_basic.rara`: x de 1 a 5 → imprime 1, 2, 3, 4, 5
- `02_while_false_cond.rara`: x=10, condición `x<5` falsa desde el inicio → solo imprime 99
- `03_nested_while.rara`: i y j de 1 a 2, imprime i+j → 2, 3, 3, 4
- `04_while_in_if.rara`: while dentro de if verdadero → imprime 1, 2, 3

**Limitaciones conocidas:**
No hay `break` ni `continue`. Un while infinito no puede terminarse desde dentro del cuerpo. El bloque vacío `{}` funciona pero genera código vacío entre las instrucciones del ciclo.

*Revisado por Jose Luis. Correcciones: ninguna.*

---

**Iteración 7 — Declaración y llamada a funciones**

**¿Qué hace el compilador ahora que no hacía antes?**
El compilador soporta funciones con parámetros y valor de retorno. Se pueden declarar con `func nombre(params) { cuerpo }`, llamar como expresión en cualquier parte, y retornar valores con `return`. Incluyendo el caso de una función que llama a otra, con el manejo correcto de `$ra`.

**¿Qué se agregó a la gramática?**
Se añadieron las palabras clave `FUNC` y `RETURN`, el token `COMMA` para separar parámetros y argumentos, la regla `funcDecl` al nivel de `prog`, la regla `returnStmt` como alternativa de `stmt`, la alternativa `call` en `factor` para llamadas de función, y las reglas `paramList` y `argList`.

**¿Qué métodos del Listener se implementaron?**
- `enterFuncDecl`: marca que estamos en modo función, crea una lista separada para el código, emite la etiqueta y los `sw $ai, var_param` para cada parámetro.
- `exitFuncDecl`: emite `jr $ra` de cierre y desactiva el modo función.
- `exitReturnStmt`: saca el valor de la pila, emite `move $v0, reg` y `jr $ra`.
- `exitCall`: saca los argumentos de la pila en orden, los mueve a `$a0-$a3`, guarda `$ra` en la pila si estamos dentro de una función, emite `jal func_nombre`, restaura `$ra`, mueve `$v0` a un registro temporal y lo empuja a la pila.

**¿Qué decisión técnica tomaste que no estaba explícita en la especificación?**
El código de las funciones se acumula en una lista separada (`func_sections`) y se emite al final del output, después del código de main. Esto evita que la ejecución de main caiga dentro del código de una función. La especificación lo mencionaba como requisito pero no decía cómo implementarlo; decidí usar una lista por función que se concatena en `output()`.

**Pruebas que pasan:**
- `01_one_param.rara`: `doble(5)` → 10, `doble(3)` → 6
- `02_two_params.rara`: `suma(3,4)` → 7, `suma(10,20)` → 30
- `03_call_in_expr.rara`: `cuadrado(3)+1` → 10, `cuadrado(4)×2` → 32
- `04_func_calls_func.rara`: `cuadruple(3)` → 12, `cuadruple(5)` → 20

**Limitaciones conocidas:**
Las funciones no son recursivas (parámetros en memoria estática). Máximo 4 argumentos (limitación de `$a0-$a3`). No se valida el número de argumentos en la llamada. El `exitFuncDecl` siempre agrega un `jr $ra` extra al final que queda como código muerto cuando hay `return` explícito (no afecta el resultado pero genera código innecesario).

*Revisado por Jose Luis. Correcciones: ninguna.*
