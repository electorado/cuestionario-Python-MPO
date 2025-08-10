import random
from colorama import Fore, Style

# Importar las preguntas del módulo que las contiene.
from preguntas import preguntas_trivial

# 1. Definir la función de puntuación
def calcular_puntuacion(aciertos, total_preguntas):
    """
    Calcula una puntuación final que combina el número de aciertos con el porcentaje,
    redondeando el resultado a un número entero.

    Args:
        aciertos (int): El número de respuestas correctas.
        total_preguntas (int): El número total de preguntas del cuestionario.

    Returns:
        int: La puntuación final calculada, redondeada al entero más cercano.
    """
    # Evita la división por cero si el trivial está vacío.
    if total_preguntas == 0:
        return 0

    # La puntuación se obtiene multiplicando el número de aciertos por el porcentaje de aciertos.
    # Esto premia a quién haya respondido más preguntas.
    porcentaje_aciertos = aciertos / total_preguntas
    puntuacion_flotante = aciertos * porcentaje_aciertos

    puntuacion_entera = round(puntuacion_flotante)

    return puntuacion_entera

# 2. Funciones para el juego del trivial
def mostrar_pregunta(pregunta, color):
    """
    Muestra el enunciado y las opciones de una pregunta con el color de la categoría.

    Args:
        pregunta (dict): El diccionario que contiene la pregunta.
        color (str): El código de color para la consola (por ejemplo, Fore.CYAN).
    """
    print(color + pregunta["pregunta"] + Style.RESET_ALL)
    for opcion in pregunta["opciones"]:
        print(f"  {opcion}")


def obtener_respuesta():
    """
    Pide al usuario que introduzca una respuesta y la valida.

    Returns:
        str: La respuesta válida del usuario (A, B, C, D o 0 para salir).
    """
    while True:
        respuesta = input("Tu respuesta (A, B, C, D o 0 para salir): ").upper()
        if respuesta in ["A", "B", "C", "D", "0"]:
            return respuesta
        else:
            print(Fore.RED + "Respuesta no válida. Por favor, elige A, B, C, D o 0." + Style.RESET_ALL)

def corregir_respuesta(respuesta_usuario, respuesta_correcta):
    """
    Comprueba si la respuesta del usuario es correcta.

    Args:
        respuesta_usuario (str): La respuesta del usuario.
        respuesta_correcta (str): La respuesta correcta almacenada en los datos.

    Returns:
        bool: True si la respuesta es correcta, False en caso contrario.
    """
    return respuesta_usuario == respuesta_correcta


def mostrar_resultados(aciertos, total):
    """
    Muestra un resumen final del cuestionario.

    Args:
        aciertos (int): El número de respuestas correctas.
        total (int): El número total de preguntas.
    """
    porcentaje = (aciertos / total) * 100 if total > 0 else 0
    print("\n--- Resultados ---")
    print(f"Total de preguntas: {total}")
    print(f"Aciertos: {aciertos}")
    print(f"Porcentaje de aciertos: {porcentaje:.2f}%")

    if porcentaje > 95:
        print(Fore.GREEN + "🤩 ¡WOW Qué Crack!" + Style.RESET_ALL)
    elif porcentaje >= 75:
        print(Fore.YELLOW + "😎 ¡Muy bien! ¡Eres un experto!" + Style.RESET_ALL)
    elif porcentaje >= 50:
        print(Fore.BLUE + "👍 Bueeeeeno. ¡Necesitas practicar un poco! " + Style.RESET_ALL)
    else:
        print(Fore.RED + "🙃 Necesitas leer más....pero ¡Tú puedes, campeón!" + Style.RESET_ALL)

def empezar_trivial():
    """
    Función principal para ejecutar el flujo del cuestionario.

    Returns:
        int or None: La puntuación final si se completa el juego, o None si se sale.
    """
    print(Fore.BLUE + "--- Empezando el cuestionario ---" + Style.RESET_ALL)
    print(Fore.BLUE + "Pulsa '0' en cualquier momento para salir." + Style.RESET_ALL)

    # Maper las categorías a los colores de la consola.
    colores_categorias = {
        "Ciencia": Fore.CYAN,
        "Historia": Fore.YELLOW,
        "Geografia": Fore.GREEN,
        "Cultura general": Fore.MAGENTA,
        "Cine": Fore.RED,
        "Música": Fore.BLUE
    }

    # Crear una lista de todas las preguntas con su categoría.
    preguntas_mezcladas = []
    for categoria, lista_preguntas in preguntas_trivial.items():
        for pregunta in lista_preguntas:
            preguntas_mezcladas.append({"pregunta_info": pregunta, "categoria": categoria})

    # Mezclar la lista de preguntas para obtener una lista aleatoria.
    random.shuffle(preguntas_mezcladas)

    aciertos = 0
    total_preguntas_respondidas = 0

    # Iterar sobre la lista aleatoria.
    for item in preguntas_mezcladas:
        pregunta = item["pregunta_info"]
        categoria = item["categoria"]
        color_categoria = colores_categorias.get(categoria, Fore.WHITE)

        print(f"\n{color_categoria}--- CATEGORÍA: {categoria} ---{Style.RESET_ALL}")
        mostrar_pregunta(pregunta, color_categoria)
        respuesta_usuario = obtener_respuesta()

        # Lógica para salir del trivial
        if respuesta_usuario == "0":
            print(Fore.YELLOW + "\nSaliendo del trivial. Guardando progreso..." + Style.RESET_ALL)
            # Mostramos los resultados parciales
            mostrar_resultados(aciertos, total_preguntas_respondidas)
            # Calculamos y mostramos la puntuación
            puntuacion_parcial = calcular_puntuacion(aciertos, total_preguntas_respondidas)
            print(f"Tu puntuación final es: {puntuacion_parcial}")
            return puntuacion_parcial

        if corregir_respuesta(respuesta_usuario, pregunta["respuesta_correcta"]):
            print(Fore.GREEN + "✅ ¡Respuesta correcta!" + Style.RESET_ALL)
            aciertos += 1
        else:
            print(Fore.RED + "❌ Respuesta incorrecta." + Style.RESET_ALL)
            print(f"La respuesta correcta era: {pregunta['respuesta_correcta']}")

        total_preguntas_respondidas += 1

    mostrar_resultados(aciertos, total_preguntas_respondidas)
    puntuacion_final = calcular_puntuacion(aciertos, total_preguntas_respondidas)
    print(f"\nTu puntuación final es: {puntuacion_final}")

    return puntuacion_final
