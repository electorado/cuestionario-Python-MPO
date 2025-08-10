# Importar las funciones de los módulos de ranking y trivial.
from ranking import mostrar_ranking, registrar_usuario, guardar_ranking
from trivial import empezar_trivial
from colorama import Fore, Style


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

    menu_principal = """
***MENÚ PRINCIPAL***
1. Regístrate
2. Comenzar el trivial
3. Ver ranking
4. Salir
"""
    opcion = 0
    print("¡Bienvenida/o al trivial!\n")

    # Uso de un diccionario para almacenar la información del usuario registrado
    # en la sesión actual.
    usuario_registrado = {"nombre": None}

    # Bucle 'while' que mantiene el programa en ejecución hasta que el usuario elija "Salir".
    while opcion != 4:
        imprimir_menu(menu_principal)
        opcion = recibir_opcion(1, 4)

        if opcion == 1:
            print("--- Seleccionaste 'Registrarte' ---")
            nombre_usuario = registrar_usuario()
            usuario_registrado["nombre"] = nombre_usuario
            print(f"¡Hola, {nombre_usuario}! Estás registrad@ para esta sesión.")
        elif opcion == 2:
            print("--- Seleccionaste 'Comenzar el trivial' ---")

            # Verificar si el usuario está registrado y le damos la opción de hacerlo.
            if not usuario_registrado["nombre"]:
                print(
                    Fore.YELLOW + "No estás registrad@, por lo que tu puntuación no se guardará en el ranking." + Style.RESET_ALL)
                sub_opcion = input("Pulsa '1' para registrarte o cualquier otra tecla para continuar: ")
                if sub_opcion == "1":
                    nombre_usuario = registrar_usuario()
                    usuario_registrado["nombre"] = nombre_usuario
                    print(f"¡Hola, {nombre_usuario}! Estás registrad@ para esta sesión.")

            puntuacion_final = empezar_trivial()

            # Solo se guarda la puntuación si el usuario está registrado.
            if usuario_registrado["nombre"]:
                if puntuacion_final is not None:
                    guardar_ranking(usuario_registrado["nombre"], puntuacion_final)
            else:
                print(
                    Fore.YELLOW + "No estás registrad@, por lo que tu puntuación no se guardará en el ranking." + Style.RESET_ALL)
        elif opcion == 3:
            print("--- Seleccionaste 'Ver ranking' ---")
            mostrar_ranking()
        elif opcion == 4:
            print("--- Saliendo de la aplicación. ¡Hasta pronto! ---")


# Este bloque asegura que el código solo se ejecute si el archivo es el principal.
if __name__ == '__main__':
    main()

