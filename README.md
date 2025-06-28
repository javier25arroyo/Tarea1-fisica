# Calculadora de Suma de Vectores

Este proyecto es una calculadora simple en Python que suma múltiples vectores. El programa permite a los usuarios ingresar vectores de dos maneras:
1.  **Magnitud y dirección (en grados):** El programa calculará las componentes x e y.
2.  **Componentes x e y:** El usuario puede ingresar directamente las componentes del vector.

## Características

-   Suma un número arbitrario de vectores.
-   Entrada de vectores flexible (magnitud/dirección o componentes x/y).
-   Manejo de errores para entradas no válidas.
-   Muestra el vector resultante en sus componentes x e y.

## Cómo usar el programa

1.  **Ejecuta el script:**
    ```bash
    python Tarea1.py
    ```

2.  **Ingresa la cantidad de vectores:**
    El programa te pedirá que ingreses el número de vectores que deseas sumar.

3.  **Ingresa cada vector:**
    Para cada vector, elige el método de entrada:
    -   **Opción 1:** Ingresa la magnitud y la dirección en grados.
    -   **Opción 2:** Ingresa las componentes x e y del vector.

4.  **Ver el resultado:**
    Después de ingresar todos los vectores, el programa mostrará las componentes x e y del vector resultante, así como el vector resultante en formato de coordenadas.

## Ejemplo de uso

```
=== Calculadora de Suma de Vectores ===
Ingrese la cantidad de vectores a sumar: 2

--- Vector 1 ---
  ¿Cómo desea ingresar el vector? (1: Magnitud y dirección, 2: Componentes x, y): 1
    Ingrese la magnitud: 10
    Ingrese la dirección en grados: 45

--- Vector 2 ---
  ¿Cómo desea ingresar el vector? (1: Magnitud y dirección, 2: Componentes x, y): 2
    Ingrese la componente x: -5
    Ingrese la componente y: 3

--- Resultado ---
La suma de los vectores es:
  Componente x resultante: 2.07
  Componente y resultante: 10.07
  Vector resultante: (2.07, 10.07)
```
