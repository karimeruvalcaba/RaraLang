---
iteracion: 3
tema: Aritmética básica
tiempo_estimado: 45 min
---
# Iteración 3 — Aritmética

## Meta

Tu compilador puede evaluar expresiones aritméticas y guardar o imprimir el resultado.
Esto debe funcionar:

```
x <-- 10
y <-- 3
print x + y
print x - y
print x × y
print x ÷ y
print (x + 2) × (y - 1)
```

## Lo que se añade a la gramática

- **Suma** con el operador `+`
- **Resta** con el operador `-`
- **Multiplicación** con el carácter `×` (no es `*`, es el símbolo tipográfico)
- **División entera** con el carácter `÷` (no es `/`)
- **Paréntesis** para agrupar expresiones y controlar el orden de evaluación

El orden en que aparecen los operadores en la gramática determina su precedencia.
La gramática puede hacer que `×` tenga más prioridad que `+`, o puede no hacerlo —
eso depende de cómo la escribas. Vale la pena que lo discutas con el modelo.

## Pruebas de aceptación

Genera tus propios programas y córrelos en QtSPIM. Calcula el resultado esperado a mano antes de correr.
Tu suite debe cubrir:

- Las cuatro operaciones con valores conocidos (verifica cada una por separado)
- Una expresión que mezcle suma y multiplicación: ¿tu compilador respeta la precedencia?
  Prueba `print 2 + 3 × 4` — el resultado correcto es 14, no 20
- Expresión con paréntesis que cambie el orden: `print (2 + 3) × 4` debe dar 20
- División donde el resultado no es exacto (ej. `10 ÷ 3`) — ¿qué pasa con el residuo?

**Trampa silenciosa** — pídele al LLM que genere un programa que divida entre cero literal.

## Prompt de ejemplo para el LLM

---

> Tengo un compilador RaraLang → MIPS. Ya funciona print con literales y variables.
> Ahora necesito operaciones aritméticas entre expresiones.
>
> En MIPS, para sumar o restar dos valores que están en registros, existe una instrucción
> directa. Para multiplicar, el resultado puede ser un número grande, así que se guarda
> en registros especiales — hay que moverlo a un registro normal después. Para dividir,
> ocurre algo similar: cociente y residuo quedan en lugares distintos, y hay que elegir
> cuál mover.
>
> El compilador usa una pila de registros temporales. Cuando evalúa `a + b`, primero
> evalúa `a` (deja un registro con el valor), luego evalúa `b` (deja otro), y cuando
> llega al `+` toma los dos del tope de la pila y produce un tercero con el resultado.
> El orden importa: el último en entrar a la pila es el operando derecho.
>
> Los operadores en RaraLang son `+`, `-`, `×` y `÷` (caracteres Unicode).
> La gramática debe expresar que `×` y `÷` tienen mayor precedencia que `+` y `-`.

---

## Reflexión (llenar después de terminar esta iteración)

**¿Qué resultado da `2 + 3 × 4` en tu compilador? ¿Es el que esperabas? ¿Cómo lo verificaste?**

Da 14, este es el correcto. La gramática mete la multiplicación más adentro en el árbol que la suma, entonces se evalúa primero. Lo revisé con 02_precedence.rara que también prueba (2 + 3) × 4 y da 20.

**En la división entera, ¿qué pasa con el residuo? ¿Dónde queda? ¿Se pierde?**

Si se pierde. MIPS guarda cociente y residuo en registros separados y el compilador solo toma el cociente, nunca el residuo. Para 10 ÷ 3, QtSPIM imprime 3 y el 1 que sobra simplemente se descarta sin decir nada.

**Explica con tus palabras por qué el orden en que se sacan los registros de la pila importa para la resta.**

La pila es LIFO, entonces el ultimo en entrar es el primero en salir. Para a - b, primero se empuja a y luego b, entonces al hacer pop sale b primero (ese es el operando derecho) y a sale despues (el izquierdo). Si se sacaran al reves se haria b - a en lugar de a - b. Para 10 - 3 daria -7 en vez de 7. Con suma y multiplicación no importa porque son conmutativas, pero con resta y división sí cambia el resultado.
