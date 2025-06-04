# Analizador Léxico Personalizado
## 📌 Autómata
![image](https://github.com/user-attachments/assets/17a19e26-9117-4bda-b3fb-0594d17c7be6)

## 📌 Definición del Lenguaje

El lenguaje diseñado para este analizador léxico toma inspiración de diversos lenguajes conocidos. Su estructura es simple y precisa al indicar el inicio y el final de la sección de “código”. Permite la declaración de variables, operaciones aritméticas básicas y operaciones lógicas.

Tomando en cuenta el autómata definido, el alfabeto del lenguaje está compuesto por letras representadas con la **“L”** y dígitos representados con la **“n”**.

Este lenguaje reconoce las siguientes categorías léxicas:

- **Palabras reservadas**: definidas en la tabla más abajo.
- **Identificadores**: secuencia que comienza con una letra (L) seguida de letras o números (L|n).
- **Números enteros y decimales**: formados por dígitos (n), pueden incluir un punto decimal (`.`).
- **Cadenas de texto**: texto encerrado entre comillas dobles (`"texto"`).
- **Símbolos y operadores**, descritos a continuación.

---

## 🔤 Palabras Reservadas

| Palabra         | Descripción                                         |
|-----------------|-----------------------------------------------------|
| `main`          | Inicio del programa                                 |
| `fin`           | Fin del programa                                    |
| `imprimir>`     | Instrucción para mostrar información                |
| `for`           | Bucle de repetición con condición                   |
| `if`            | Condicional si                                      |
| `else`          | Condicional en caso contrario                       |
| `num#`          | Declaración de variable numérica entera             |
| `double#`       | Declaración de variable numérica con decimales      |
| `string#`       | Declaración de variable de tipo texto o cadena      |
| `boolean#`      | Declaración de variable booleana (`TRUE`, `FALSE`)  |
| `TRUE`          | Valor booleano verdadero                            |
| `FALSE`         | Valor booleano falso                                |

---

## 🧮 Operadores y Símbolos Especiales

| Símbolo / Operador | Tipo                   | Descripción                                          |
|--------------------|------------------------|------------------------------------------------------|
| `=`                | Asignación             | Asigna un valor a una variable                       |
| `+`, `-`, `*`, `/` | Aritmético             | Operaciones matemáticas básicas                      |
| `==`               | Relacional             | Igualdad                                             |
| `!=`               | Relacional             | Diferente                                            |
| `>`, `<`, `>=`, `<=` | Relacional          | Comparaciones entre valores                          |
| `&`, `|`           | Lógico                 | Operaciones booleanas (AND, OR)                      |
| `"`                | Delimitador de cadena  | Encierra textos tipo string                          |
| `(`, `)`           | Agrupadores            | Para expresiones o condiciones                       |
| `{`, `}`           | Delimitadores de bloque| Encierra bloques de instrucciones                    |
| `[`, `]`           | Agrupadores            | Usado para arreglos o índices                        |

---

## 📘 Sintaxis de Cada Instrucción
### 🟦 Declaración de Variables

```plaintext
<tipo_dato> <identificador>
```
### 🟨 Asignación de Variables

```plaintext
<identificador> = <valor>
```
### 🟩 Impresión de Datos
```plaintext
imprimir> <valor | identificador>
```
### 🟥 Estructura Principal del Programa
```plaintext
main {
    // instrucciones
} fin
```
### 🟪 Condicionales
```plaintext
if (<condición>) {
    // instrucciones
} else {
    // instrucciones
}
```
### 🔁 Ciclo for
```plaintext
for (<declaración>, <condición>, <incremento>) {
    // instrucciones
}
```

## 🧪 Textos de Prueba
### ✅ Prueba Correcta (Prueba2.txt)
```plaintext
main {
    num# x = 2
    num# y = 10
    num# z = 4

    boolean# comparar = y >= z

    if (comparar) == TRUE {
        num# resultado = y * x
        imprimir> resultado
    } else { 
        imprimir> "El valor de y es "+ comparar +", y no es >= x"
    }
} fin

```
### ❌ Prueba con Errores (PruebaError2.txt)
```plaintext
inicio {
    2num ¿ 23
    cadena# = 'holaaaaaaa2'
    boolean# = true;
    _imprimir> "Buenas a todos"
    double# = 29.5

    int# vector = [1,2,3,4,5]
    // Comentario
    for (i = 0, i < 10, i + 1) {
        imprimir> i
    }

} fin
```
