from pprint import pprint
from collections import deque
from linked_list import NewNode, SingleLinkedList
input = []
real = './day_10/input.txt'
example = './day_10/example.txt'

north = "north"
east = "east"
south = "south"
west = "west"

arrangements = {
    "|": [north, south],
    "-": [east, west],
    "L":  [north, east],
    "J":  [north, west],
    "7":  [south, west],
    "F":  [south, east],
    ".": None,
    "S": 'Start'
}

def extract_data(document_input):
    with open(document_input, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    return [list(i) for i in lines]


def checking_conections(position):
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



def checking_conections_old(position):

    up = input[position[0]-1][position[1]]
    down = input[position[0]+1][position[1]]
    left = input[position[0]][position[1]-1]
    right = input[position[0]][position[1]+1]
    connection = []


    
    if arrangements[up] and south in arrangements[up]:
        connection.append((position[0]-1, position[1]))

    
    if arrangements[right] and west in arrangements[right]:
        connection.append((position[0], position[1]+1))

    if arrangements[down] and north in arrangements[down]:
        connection.append((position[0]+1, position[1]))

    if arrangements[left] and east in arrangements[left]:
         connection.append((position[0], position[1]-1))

    return connection


def look_for_start_point(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if arrangements[input[i][j]] == 'Start':
                return (i, j)
        

def follow_the_loop(starting_point):
    visited = set()
    distance = 0
    max_distance = 0
    queue = deque([(starting_point, 0)])

    queue = deque([starting_point])

    while queue:
        current_point = queue.popleft()
        if current_point not in visited:
            visited.add(current_point)
            max_distance = max(max_distance, distance)


            connections = checking_conections(current_point)
            for conn in connections:
                if conn not in visited:
                    distance = distance+1
                    queue.append(conn)
    print(distance)
    return visited



input = extract_data(real)

starting_point = look_for_start_point(input)

loop_pipe = follow_the_loop(starting_point)


print(f"len: {(len(loop_pipe))/2}")


