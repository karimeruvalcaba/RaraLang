# RaraLang - Qué falta y cómo seguir

## Importante

Estamos trabajando sobre:

```txt
C:\Users\user\RaraLang\entrega
```

NO sobre:

```txt
C:\Users\user\RaraLang\actividad3
```

La carpeta `actividad3` se dejó intacta porque es el material original.

Toda modificación va en `entrega`.

---

## Reporte

La parte individual de la actividad es el reporte.

En:

```txt
actividad3\doc\tunombre
```

hay un template:

```txt
template-reporte-tunombre.md
```

Y cada iteración tiene preguntas de reflexión al final., tambien esas las respondes , junto con el archivo de arriba

Por ejemplo:

```txt
it2-variables.md
it3-aritmetica.md
it4-unicode.md
it5-control-flujo.md
...
```

Cada iteración tiene una sección tipo:

```txt
Reflexión (llenar después de terminar esta iteración)
```

Hay que contestar esas preguntas después de implementar y probar cada iteración.

Aunque el código sea compartido, el reporte es individual.

---

## Estado actual

### Iteración 1

Terminada.

Funciona:

```rara
print 42
print [FF:16]
print "hola"
```

Pruebas:

```txt
tests/iteracion1
```

---

### Iteración 2

Terminada.

Funciona:

```rara
x <-- 10
print x
```

Variables almacenadas como:

```asm
var_x: .word 0
```

Pruebas:

```txt
tests/iteracion2
```

---

### Iteración 3

Terminada.

Funciona:

```rara
+
-
×
÷
()
```

Pruebas:

```txt
tests/iteracion3
```

Casos importantes:

```rara
print 2 + 3 × 4
```

Debe dar:

```txt
14
```

Y:

```rara
print (2 + 3) × 4
```

Debe dar:

```txt
20
```

---

### Iteración 4

Está dividida.

#### Ya hecho

Operador:

```txt
⊞
⊠
```

Implementados y probados.

Pruebas:

```txt
tests/iteracion4
```

Casos:

```rara
print 10 ⊞ 3
```

Resultado:

```txt
1
```

```rara
print 4 ⊠ 5
```

Resultado:

```txt
13
```

---

#### Falta

Implementar:

```txt
≈
±
```

Hay que modificar:

```txt
antlr/RaraLang.g4
MIPSListener.py
```

y crear pruebas nuevas.

Leer:

```txt
actividad3\doc\it4-unicode.md
```

y contestar las preguntas de reflexión.

---

## Lo que sigue

### Iteración 5

Archivo:

```txt
actividad3\doc\it5-control-flujo.md
```

Implementar:

```txt
if
else
comparaciones
```

Crear:

```txt
tests/iteracion5
```

Generar pruebas.

Contestar preguntas del final del documento.

---

### Iteración 6

Leer:

```txt
actividad3\doc\it6-while.md
```

Implementar:

```txt
while
bloques
```

Crear:

```txt
tests/iteracion6
```

Generar pruebas.

Contestar preguntas de reflexión.

---

### Iteración 7

Leer:

```txt
actividad3\doc\it7-funciones.md
```

Implementar:

```txt
funciones
parámetros
return
```

Crear:

```txt
tests/iteracion7
```

Generar pruebas.

Contestar preguntas de reflexión.

---

## Cada vez que se modifique la gramática

Borrar generados:

```powershell
Remove-Item .\antlr\RaraLang*.py
Remove-Item .\antlr\RaraLang*.tokens
Remove-Item .\antlr\RaraLang*.interp
```

Regenerar:

```powershell
java -jar .\antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -listener -o . .\antlr\RaraLang.g4
```

Después correr los tests. Cada que corras los tests crea una carpeta tipo tests/iteracionN/ y ahi adentro pones los .rara que se pide en doc itN-TEXTO-.md

---

## Entrega final

Por iteración debe existir:

```txt
tests/iteracionN/
```

con:

```txt
mínimo 3 archivos .rara
mínimo 1 archivo .asm generado
```

Y además:

```txt
MIPSListener.py
```

actualizado y funcionando.

No olvides llenar las preguntas de reflexión de cada archivo dentro de:

```txt
actividad3\doc
```

porque eso sí es parte de la evaluación individual.
