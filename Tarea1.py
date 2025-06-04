import math

def obtener_componentes_vector():
    while True:
        tipo_entrada = input(
            "  ¿Cómo desea ingresar el vector? (1: Magnitud y dirección, 2: Componentes x, y): "
        )
        if tipo_entrada == "1":
            try:
                magnitud = float(input("    Ingrese la magnitud: "))
                if magnitud < 0:
                    print("    La magnitud no puede ser negativa. Intente de nuevo.")
                    continue
                direccion_grados = float(input("    Ingrese la dirección en grados: "))
                direccion_radianes = math.radians(direccion_grados)
                vx = magnitud * math.cos(direccion_radianes)
                vy = magnitud * math.sin(direccion_radianes)
                return vx, vy
            except ValueError:
                print("    Entrada inválida. Por favor, ingrese números.")
        elif tipo_entrada == "2":
            try:
                vx = float(input("    Ingrese la componente x: "))
                vy = float(input("    Ingrese la componente y: "))
                return vx, vy
            except ValueError:
                print("    Entrada inválida. Por favor, ingrese números.")
        else:
            print("  Opción no válida. Seleccione 1 o 2.")


def main():
    print("=== Calculadora de Suma de Vectores ===")

    # Solicitar la cantidad de vectores
    while True:
        try:
            n_vectores = int(input("Ingrese la cantidad de vectores a sumar: "))
            if n_vectores <= 0:
                print(
                    "  La cantidad de vectores debe ser un número entero positivo. Intente de nuevo."
                )
                continue
            break
        except ValueError:
            print("  Entrada inválida. Por favor, ingrese un número entero.")

    suma_vx = 0.0
    suma_vy = 0.0

    # Ingresar cada vector y acumular sus componentes
    for i in range(1, n_vectores + 1):
        print(f"\n--- Vector {i} ---")
        vx, vy = obtener_componentes_vector()
        suma_vx += vx
        suma_vy += vy

    # Mostrar el resultado con mayor precisión
    print("\n--- Resultado ---")
    print("La suma de los vectores es:")
    print(f"  Componente x resultante: {suma_vx:.2f}")
    print(f"  Componente y resultante: {suma_vy:.2f}")
    print(f"  Vector resultante: ({suma_vx:.2f}, {suma_vy:.2f})")


if __name__ == "__main__":
    main()
