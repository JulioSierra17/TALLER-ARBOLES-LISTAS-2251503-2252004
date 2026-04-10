# TALLER-ARBOLES-LISTAS

## NEYDER FABIÁN PEÑA GONZÁLEZ CODIGO: 2252004
## JULIO CESAR SIERRA JIMENEZ CODIGO: 2251503

En este repositorio podremos encontrar un programa en python el cual mediante la implementacion de estructuras basicas de las listas enlazadas, previamente vistas en clase, se realiza un programa en el que se crean estructuras de arboles en el cual podemos ingresar de manera manual cada nodo y ademas tenemos opciones para poder ver el peso, el orden y la altura de este mismo.

# ¿Qué son los Árboles de Huffman?

Los Árboles de Huffman son un método muy usado para **comprimir datos**. Es decir, sirven para que un archivo o un mensaje ocupe menos espacio en la memoria de la computadora sin perder nada de información.

## ¿Cómo funcionan?
En lugar de que cada letra o símbolo use siempre la misma cantidad de espacio (como 8 bits), el Árbol de Huffman hace lo siguiente:
1. Mira qué letras se repiten más.
2. A las letras que **más se usan**, les pone un código muy cortito (como un `0` o `1`).
3. A las letras que **casi no se usan**, les pone un código más largo.

## Características principales
* **Son árboles binarios:** Cada nodo solo puede tener máximo dos hijos.
* **Sin prefijos:** Ningún código es el inicio de otro, así la computadora no se confunde al leer los datos.
* **Eficiencia:** Es una de las formas más eficientes de ahorrar espacio en textos.

## ¿Dónde se usan hoy en día?
Aunque no los veamos, los usamos todo el tiempo en:
* Archivos comprimidos **.ZIP** o **.RAR**.
* Formatos de imágenes como **JPEG**.
* Archivos de música y video.