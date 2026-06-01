---
iteracion: 2
tema: Variables enteras y asignación
tiempo_estimado: 30 min
---

# Iteración 2 — Variables

## Meta

Tu compilador puede ahora guardar valores en variables con nombre y recuperarlos.
Un programa como este debe funcionar:

```
x <-- 10
y <-- 3
print x
print y
```

## Lo que se añade a la gramática

- **Nombres de variable**: una secuencia de letras, números y guiones bajos que empieza
  con letra. Por ejemplo: `x`, `contador`, `valor_final`.
- **Sentencia de asignación**: la forma `nombre <-- expresión` guarda un valor en la variable.
  El operador es `<--` (dos guiones, no uno).
- **Variable como expresión**: escribir el nombre de una variable donde va una expresión
  significa "leer el valor de esa variable".

## Pruebas de aceptación

Genera tus propios programas de prueba y córrelos en QtSPIM.
Tu suite debe cubrir:

- Asignar un valor a una variable e imprimirla
- Asignar dos variables distintas, imprimir ambas en orden
- Reasignar una variable y verificar que `print` muestra el nuevo valor
- Una variable cuyo nombre sea una instrucción de MIPS (ej: `add`, `sub`, `div`) — este caso suele romper compiladores ingenuos; verifica que el tuyo lo maneja

**Trampa silenciosa** — pídele al LLM que genere un programa que lea una variable
sin haberla asignado. ¿Qué hace tu compilador? ¿Debería ser un error?

## Prompt de ejemplo para el LLM

---

> Mi compilador ya genera código para `print` con literales. Ahora necesito variables.
>
> En MIPS, las variables enteras se guardan en la sección `.data` como palabras de 32 bits.
> Cuando se asigna un valor a una variable, hay que almacenarlo en esa dirección de memoria.
> Cuando se lee una variable, hay que cargarla desde esa dirección a un registro.
>
> Necesito que el compilador haga esto automáticamente la primera vez que ve cada variable:
> reservar espacio en `.data` con un valor inicial de 0.

---

## Reflexión (llenar después de terminar esta iteración)

**¿Cómo decidió el modelo reservar espacio para la variable? ¿Dónde queda en el archivo `.asm`?**

> Usa `var_nombre: .word 0` en la sección `.data`. La primera vez que el compilador ve una variable (ya sea leyéndola o asignándola) la declara ahí. Queda al inicio del archivo, antes del `.text`.

**Prueba b <-- 5 ¿Qué se genera, qué hace QtSpim?**

> Genera `var_b: .word 0` en `.data`, luego `li $t0, 5` y `sw $t0, var_b` en el código. En QtSPIM simplemente guarda el 5 en memoria, no imprime nada porque no hay `print`. Si después haces `print b` sí aparece el 5.

**¿Qué pasa si asignas una variable dos veces?**

> Solo se declara una vez en `.data` (el compilador lleva un set de variables vistas). Cada asignación genera un `sw` que sobreescribe el valor anterior en la misma dirección. La segunda asignación gana, que es el comportamiento esperado.
