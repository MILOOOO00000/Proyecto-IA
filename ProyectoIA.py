import random

# Función para inicializar el tablero
def inicializar_tablero(filas, columnas):
    tablero = []
    for _ in range(filas):
        fila = ['-'] * columnas
        tablero.append(fila)
    return tablero

# Función para imprimir el tablero con los indicadores de filas y columnas
def imprimir_tablero(tablero):
    # Imprimir los números de las columnas
    print("  ", end="")
    for i in range(len(tablero[0])):
        print(f"{i+1}", end=" ")
    print()
    
    # Imprimir el tablero con los indicadores de fila y columna
    for i, fila in enumerate(tablero):
        print(f"{i+1} {' '.join(fila)}")

# Función para imprimir el tablero de disparos fallidos
def imprimir_tablero_disparos_fallidos(tablero):
    print("\nTablero de disparos fallidos:")
    # Imprimir los números de las columnas
    print("  ", end="")
    for i in range(len(tablero[0])):
        print(f"{i+1}", end=" ")
    print()
    
    # Imprimir el tablero de disparos fallidos
    for i, fila in enumerate(tablero):
        print(f"{i+1} {' '.join(fila)}")

# Función para que un jugador coloque sus barcos
def colocar_barcos_jugador(tablero, jugador):
    for tamano in [3, 3, 2]:
        print(f"Jugador {jugador}, coloca un barco de tamaño", tamano)
        while True:
            imprimir_tablero(tablero)
            fila_inicio = int(input("Ingresa el número de fila de inicio: ")) - 1
            columna_inicio = int(input("Ingresa el número de columna de inicio: ")) - 1
            direccion = input("Ingresa la dirección (h para horizontal, v para vertical): ")
            if direccion.lower() == 'h':
                fila_fin = fila_inicio
                columna_fin = columna_inicio + tamano - 1
            elif direccion.lower() == 'v':
                fila_fin = fila_inicio + tamano - 1
                columna_fin = columna_inicio
            else:
                print("Dirección no válida. Inténtalo de nuevo.")
                continue

            if (0 <= fila_inicio < len(tablero) and
                0 <= columna_inicio < len(tablero[0]) and
                0 <= fila_fin < len(tablero) and
                0 <= columna_fin < len(tablero[0])):
                barco_valido = True
                for i in range(tamano):
                    if direccion.lower() == 'h':
                        if tablero[fila_inicio][columna_inicio + i] == 'B':
                            barco_valido = False
                            break
                    elif direccion.lower() == 'v':
                        if tablero[fila_inicio + i][columna_inicio] == 'B':
                            barco_valido = False
                            break
                if barco_valido:
                    for i in range(tamano):
                        if direccion.lower() == 'h':
                            tablero[fila_inicio][columna_inicio + i] = 'B'
                        elif direccion.lower() == 'v':
                            tablero[fila_inicio + i][columna_inicio] = 'B'
                    break
                else:
                    print("¡Ya hay un barco en esa posición! Inténtalo de nuevo.")
            else:
                print("Coordenadas inválidas. Inténtalo de nuevo.")

# Función para que un jugador ingrese las coordenadas de su ataque
def ingresar_coordenadas():
    fila = int(input("Ingresa el número de fila: ")) - 1
    columna = int(input("Ingresa el número de columna: ")) - 1
    return fila, columna

# Función para verificar si las coordenadas son válidas
def coordenadas_validas(fila, columna, tablero):
    if 0 <= fila < len(tablero) and 0 <= columna < len(tablero[0]):
        return True
    else:
        return False

# Función para actualizar el tablero después de un disparo
def actualizar_tablero(tablero, fila, columna):
    if tablero[fila][columna] == 'B':
        print("¡Barco tocado!")
        tablero[fila][columna] = 'X'
        return True, (fila, columna)
    elif tablero[fila][columna] == 'X':
        print("¡Ya has disparado a esta posición!")
        return False, (fila, columna)
    else:
        print("¡Agua!")
        tablero[fila][columna] = 'O'  # 'O' para indicar un disparo fallido
        return False, (fila, columna)

# Función para verificar si todos los barcos han sido hundidos
def todos_barcos_hundidos(tablero):
    for fila in tablero:
        if 'B' in fila:
            return False
    return True

# Función principal del juego
def jugar_batalla_naval(filas, columnas, num_jugadores):
    print("¡Bienvenido al juego de Batalla Naval!")
    
    # Inicializar tableros para cada jugador
    tableros = [inicializar_tablero(filas, columnas) for _ in range(num_jugadores)]
    
    # Colocar barcos para cada jugador
    for i in range(num_jugadores):
        print(f"Jugador {i + 1}, prepara tus barcos:")
        colocar_barcos_jugador(tableros[i], i + 1)

    print("\n¡Comienza la batalla!")
    
    # Turnos de ataque en forma circular entre los jugadores
    turno = 0
    while True:
        jugador_actual = turno % num_jugadores
        jugador_siguiente = (turno + 1) % num_jugadores
        
        print(f"\nJugador {jugador_actual + 1}, es tu turno de atacar al jugador {jugador_siguiente + 1}:")
        print(f"Tablero del jugador {jugador_actual + 1}:")
        imprimir_tablero(tableros[jugador_actual])
        
        fila, columna = ingresar_coordenadas()
        if coordenadas_validas(fila, columna, tableros[jugador_siguiente]):
            tocado, ubicacion = actualizar_tablero(tableros[jugador_siguiente], fila, columna)
            if tocado:
                print("¡Has tocado un barco enemigo!")
                tableros[jugador_actual][fila][columna] = 'D'  # Marcar el disparo en el tablero del jugador actual
                if todos_barcos_hundidos(tableros[jugador_siguiente]):
                    print(f"¡Felicidades! ¡Has hundido todos los barcos del jugador {jugador_siguiente + 1}! ¡Jugador {jugador_actual + 1} gana!")
                    break
            else:
                print("¡No has tocado ningún barco enemigo!")
                tableros[jugador_actual][fila][columna] = 'O'  # Marcar el disparo fallido en el tablero del jugador actual

        turno += 1

# Parámetros del juego
filas = 10
columnas = 10
num_jugadores = 3

# Iniciar juego
jugar_batalla_naval(filas, columnas, num_jugadores)