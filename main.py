def imprimir_menu(menu):
    """
    Imprime el menu proporcionado.
    """
    print(menu)

def recibir_opcion(min, max):
    """
    Recibe la opción del usuario un número y la valida
    para que esté dentro del rango especificado.

    Args:
        min (int): El valor mínimo aceptado.
        max (int): El valor máximo aceptado.

    Returns:
        int: El número válido introducido por el usuario.
    """
    opcion = 0
    valida = False
    while not valida:
        try:
            opcion = int(input(f"Selecciona una opción: "))
            if opcion < min or opcion > max:
                print("Opción fuera de rango. Intenta de nuevo.")
            else:
                valida = True
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")
    return opcion


def main():
    """
    Función para ejecutar el menú principal.
    """
    menu_principal = """
***MENÚ PRINCIPAL***
1. Regístrate
2. Comenzar el trivial
3. Ver ranking
4. Salir
"""
    opcion = 0
    print("¡Bienvenida/o al trivial!\n")

    # El bucle 'while' mantiene el programa en ejecución hasta que el usuario elija "Salir".
    while opcion != 4:
        imprimir_menu(menu_principal)
        opcion = recibir_opcion(1, 4)

        if opcion == 1:
            # Aquí irá la lógica para registrar al usuario
            pass
        elif opcion == 2:
            # Aquí irá la lógica del cuestionario
            pass
        elif opcion == 3:
            # Aquí irá la lógica para ver el ranking
            pass
        elif opcion == 4:
            print("--- Saliendo de la aplicación. ¡Hasta pronto! ---")

