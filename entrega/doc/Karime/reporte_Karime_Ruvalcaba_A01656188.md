# Reporte de iteración — Karime Ruvalcaba (A01656188)

---

**Iteración 1 — Literales enteros, números en otras bases, strings y print**

**¿Qué hace el compilador ahora que no hacía antes?**
El compilador puede tomar un programa RaraLang con instrucciones `print` y generar
código MIPS que QtSPIM ejecuta e imprime correctamente. Antes de esta iteración no
existía nada; ahora soporta tres tipos de literales: enteros decimales (`42`),
números en base arbitraria (`[FF:16]`, `[1010:2]`) y cadenas de texto (`"hola"`).

**¿Qué se agregó a la gramática?**
Se añadieron tres tokens nuevos al lexer: `INT` para secuencias de dígitos decimales,
`BASED_NUMBER` para el formato `[dígitos:base]` donde los dígitos pueden incluir letras
A–F, y `STRING` para texto entre comillas dobles. En el parser, la regla `factor` acepta
cualquiera de esos tres literales como alternativas válidas dentro de una expresión.
También existe la sentencia `print expr` que activa la impresión.

**¿Qué métodos del Listener se implementaron?**

- `exitInt` — lee el texto del token `INT`, lo convierte a entero y emite `li $tN, valor`.
- `exitBased` — parsea el formato `[dígitos:base]`, llama `int(digits, base)` en Python
  para obtener el valor decimal y emite el mismo `li` que un entero normal.
- `exitString` — asigna una etiqueta única (`str0`, `str1`, …) en `.data` con `.asciiz`,
  y empuja ese nombre de etiqueta en la pila interna (no un registro).
- `exitPrintStmt` — saca el valor de la pila; si es una etiqueta de string usa
  `la $a0, strN` + syscall 4; si es un registro usa `move $a0, $tN` + syscall 1.
  En ambos casos emite syscall 11 con carácter 10 para imprimir el salto de línea.
- `enterProg` / `exitProg` — emiten el encabezado `.text .globl main main:` y el
  `li $v0, 10 / syscall` de salida al final del programa.

**¿Qué decisión técnica tomaste que no estaba explícita en la especificación?**
Para distinguir strings de enteros en `exitPrintStmt` sin un sistema de tipos, el modelo
decidió empujar el *nombre de la etiqueta* (un string de Python como `"str0"`) en lugar
de un registro `$tN`. La detección en runtime es `value.startswith("str")`. Es un truco
de convención de nombres, no un tipo real, pero funciona mientras las variables del
programa no empiecen con los caracteres `str`.

**Pruebas que pasan:**

| Archivo                    | Salida esperada en QtSPIM                 |
| -------------------------- | ----------------------------------------- |
| `01_int_literal.rara`    | 42, 0, 100 (cada uno en su propia línea) |
| `02_based_number.rara`   | 255, 10, 15                               |
| `03_string_literal.rara` | hola, rara                                |

**Limitaciones conocidas:**

- `[29:2]` (dígito inválido para la base indicada) es aceptado por el lexer pero causa un `ValueError` de Python sin mensaje de error útil para el usuario.
- Las cadenas no admiten secuencias de escape (`\n`, `\"`, etc.).
- Solo hay 10 registros temporales ($t0–$t9); expresiones muy anidadas o programas con muchos prints seguidos agotan los temporales y el compilador lanza una excepción. Las variables no existen aún, cualquier identificador como expresión causa error.

---
