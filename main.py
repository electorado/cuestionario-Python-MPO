# Importamos las funciones del módulo de ranking.
# Esto le permite a main.py usar el código que está en ranking.py.
from ranking import mostrar_ranking, registrar_usuario, guardar_ranking


def imprimir_menu(menu):
    """
    Imprime el menu proporcionado.
    """
    print(menu)

def recibir_opcion(min, max):
    """
    Pide al usuario un número y valida que esté dentro del rango especificado.

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
            opcion = int(input(f"Selecciona una opción ({min}-{max}): "))
            if opcion < min or opcion > max:
                print("Opción fuera de rango. Intenta de nuevo.")
            else:
                valida = True
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")
    return opcion

def main():
    """
    Función principal que ejecuta el menú de la aplicación.
    """
    # El menú principal se define como un string multilínea para mayor claridad.
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
            print("--- Seleccionaste 'Registrarte' ---")
            # Llamamos a la función del módulo ranking para obtener el nombre del usuario.
            nombre_usuario = registrar_usuario()
            # Asumimos una puntuación inicial de 0. Esta se actualizará al jugar.
            guardar_ranking(nombre_usuario, 0)
        elif opcion == 2:
            print("--- Seleccionaste 'Comenzar el trivial' ---")
            # Aquí irá la lógica del cuestionario.
            pass
        elif opcion == 3:
            print("--- Seleccionaste 'Ver ranking' ---")
            # Llamamos a la función del módulo ranking para mostrar la lista.
            mostrar_ranking()
        elif opcion == 4:
            print("--- Saliendo de la aplicación. ¡Hasta pronto! ---")

# Este bloque se asegura de que el código solo se ejecute si el archivo es el principal.
if __name__ == '__main__':
    main()
