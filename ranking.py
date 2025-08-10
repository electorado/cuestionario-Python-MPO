from colorama import Fore, Style

def registrar_usuario():
    """
    Pide al usuario que se registre y devuelve su nombre.

    Returns:
        str: El nombre del usuario.
    """
    nombre = input("Introduce tu nombre de usuario para participar en el ranking: ")
    return nombre

# Diccionario para almacenar el ranking en memoria.
# Las claves serán los nombres de los usuarios y los valores sus puntuaciones.
ranking_trivial = {}

def guardar_ranking(nombre, puntuacion):
    """
    Guarda la puntuación de un usuario en el ranking.

    Args:
        nombre (str): El nombre del usuario.
        puntuacion (int): La puntuación obtenida.
    """
    ranking_trivial[nombre] = puntuacion
    print(f"Tu puntuación ha sido guardada en el ranking.")

def mostrar_ranking():
    """
    Muestra el ranking de jugadores en la consola.
    """
    print(Fore.YELLOW + "\n--- RANKING DE JUGADORES ---" + Style.RESET_ALL)
    if not ranking_trivial:
        print("El ranking está vacío. ¡Sé el primero en participar!")
    else:
        # 1. Obtenemos las claves (nombres de usuario) del diccionario.
        nombres = list(ranking_trivial.keys())

        # 2. Ordenamos la lista de nombres de forma descendente.
        #    La clave de ordenación es la puntuación de cada nombre.
        nombres_ordenados = sorted(nombres, key=ranking_trivial.get, reverse=True)

        # 3. Recorremos la lista ordenada y mostramos el ranking.
        for i, nombre in enumerate(nombres_ordenados, 1):
            puntuacion = ranking_trivial.get(nombre)
            print(f"{i}. {nombre} - {puntuacion} aciertos")




