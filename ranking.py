import json
import os
from colorama import Fore, Style

# Definir el nombre del archivo donde se guardará el ranking.
# Utilizar 'os.path.join' para asegurar que la ruta sea compatible con cualquier sistema operativo.
RANKING_FILE = os.path.join("data", "ranking.json")


def cargar_ranking():
    """
    Carga el ranking de usuarios desde un archivo JSON.
    Si el archivo no existe o está vacío, devuelve una lista vacía.

    Returns:
        list: Una lista de diccionarios con el ranking.
    """
    try:
        # Utilizar 'with open' para cerciorarse de que el archivo se cierre correctamente.
        with open(RANKING_FILE, "r", encoding="utf-8") as f:
            ranking = json.load(f)
            # Ordenar el ranking por puntuación de forma descendente.
            return sorted(ranking, key=lambda x: x["puntuacion"], reverse=True)
    except (FileNotFoundError, json.JSONDecodeError):
        # Capturar errores si el archivo no existe o su formato es incorrecto.
        return []


def guardar_ranking(nombre, puntuacion):
    """
    Guarda la puntuación de un usuario en el ranking.

    Args:
        nombre (str): El nombre del usuario.
        puntuacion (int): La puntuación obtenida.
    """
    ranking = cargar_ranking()
    # Si el nombre ya existe, se actualiza la puntuación.
    usuario_encontrado = False
    for usuario in ranking:
        if usuario["nombre"] == nombre:
            # Acualizar puntuación solamente si la nueva es mayor que la anterior.
            if puntuacion > usuario["puntuacion"]:
                usuario["puntuacion"] = puntuacion
            usuario_encontrado = True
            break

    # Añadir nombre si no hay registro.
    if not usuario_encontrado:
        ranking.append({"nombre": nombre, "puntuacion": puntuacion})

    # Ordenar nuevamente la lista después de añadir registro o actualizar una puntuación.
    ranking = sorted(ranking, key=lambda x: x["puntuacion"], reverse=True)

    try:
        # Asegurse que la carpeta 'data' exista antes de guardar.
        os.makedirs(os.path.dirname(RANKING_FILE), exist_ok=True)
        with open(RANKING_FILE, "w", encoding="utf-8") as f:
            json.dump(ranking, f, indent=4)
        print(f"Tu puntuación ha sido guardada en el ranking.")
    except IOError:
        print(f"Error: No se pudo guardar el ranking.")


def mostrar_ranking():
    """
    Muestra el ranking de jugadores en la consola.
    """
    print(Fore.YELLOW + "\n--- RANKING DE JUGADORES ---" + Style.RESET_ALL)
    ranking = cargar_ranking()
    if not ranking:
        print("El ranking está vacío. ¡Sé el primero en participar!")
    else:
        # Iterar sobre cada jugador del ranking, empezando por el 1, usando enumerate.
        for i, jugador in enumerate(ranking, 1):
            # Imprimir el número, el nombre y la puntuación de cada jugador.
            print(f"{i}. {jugador['nombre']} - {jugador['puntuacion']} puntos")


def registrar_usuario():
    """
    Pide al usuario que se registre y devuelve su nombre.
    Si el usuario ya existe, ofrece la opción de jugar con él o crear uno nuevo.

    Returns:
        str: El nombre del usuario registrado o None si no se registra.
    """
    ranking = cargar_ranking()

    while True:
        nombre = input("Introduce tu nombre de usuario para participar en el ranking: ")

        # Comprobar si el nombre ya existe en el ranking
        nombres_existentes = {jugador['nombre'] for jugador in ranking}
        if nombre in nombres_existentes:
            print(Fore.YELLOW + f"El usuario '{nombre}' ya existe." + Style.RESET_ALL)
            opcion = input("Pulsa '1' para jugar con este usuario o '2' para registrar uno nuevo: ")

            if opcion == '1':
                return nombre
            elif opcion == '2':
                # El bucle continuará pidiendo un nuevo nombre
                continue
        else:
            # El nombre no existe, se puede usar
            return nombre

