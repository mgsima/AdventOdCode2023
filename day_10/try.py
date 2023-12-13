# Definiendo las direcciones como cadenas
from collections import deque


# Primero, necesito leer el archivo de entrada para entender la estructura de los datos proporcionados.
file_path = './day_10/input.txt'

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    return [list(line) for line in lines]


north, east, south, west = "north", "east", "south", "west"

# Actualizando el diccionario de arreglos con las direcciones corregidas
arrangements = {
    "|": [north, south],
    "-": [east, west],
    "L": [north, east],
    "J": [north, west],
    "7": [south, west],
    "F": [south, east],
    ".": None,
    "S": [north, east, south, west]  # Asumimos que 'S' puede conectar en cualquier dirección
}

# Función para comprobar las conexiones válidas de un punto dado en la cuadrícula
def get_connections(input, position, arrangements):
    rows = len(input)
    cols = len(input[0]) if rows else 0
    connection = []

    # Comprobando arriba
    if position[0] > 0:
        up = input[position[0] - 1][position[1]]
        if arrangements[up] and south in arrangements[up]:
            connection.append((position[0] - 1, position[1]))

    # Comprobando abajo
    if position[0] < rows - 1:
        down = input[position[0] + 1][position[1]]
        if arrangements[down] and north in arrangements[down]:
            connection.append((position[0] + 1, position[1]))

    # Comprobando izquierda
    if position[1] > 0:
        left = input[position[0]][position[1] - 1]
        if arrangements[left] and east in arrangements[left]:
            connection.append((position[0], position[1] - 1))

    # Comprobando derecha
    if position[1] < cols - 1:
        right = input[position[0]][position[1] + 1]
        if arrangements[right] and west in arrangements[right]:
            connection.append((position[0], position[1] + 1))

    return connection

# Función para seguir el bucle de tuberías y encontrar el punto más alejado
def follow_the_loop(grid, start, arrangements):
    visited = set()  # Conjunto para mantener un registro de los puntos visitados
    queue = deque([(start, 0)])  # Cola para BFS, almacenando pares (posición, distancia)
    max_distance = 0  # Distancia máxima desde el punto de partida

    while queue:
        current_position, distance = queue.popleft()
        if current_position not in visited:
            visited.add(current_position)
            max_distance = max(max_distance, distance)

            # Obtener conexiones válidas y agregarlas a la cola
            for next_position in get_connections(grid, current_position, arrangements):
                if next_position not in visited:
                    queue.append((next_position, distance + 1))

    return max_distance

# Función para buscar el punto de partida 'S' en la cuadrícula
def look_for_start_point(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                return i, j



input_data = read_input_file(file_path)

starting_point = look_for_start_point(input_data)

# Calculamos la distancia máxima desde el punto de partida en el bucle
max_distance = follow_the_loop(input_data, starting_point, arrangements)

print(max_distance)