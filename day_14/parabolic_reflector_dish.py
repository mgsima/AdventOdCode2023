from pprint import pprint
from time import time
from functools import cache


input = []
real = './day_14/input.txt'
example = './day_14/example.txt'

def extract_data(document_input):
    with open(document_input, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


@cache
def if_empty_move(line):
    line = list(line)
    empty_spaces = []  # Usamos una lista para rastrear los espacios vacíos

    for pos_l in range(len(line)):
        if line[pos_l] == '.':
            empty_spaces.append(pos_l)
        elif line[pos_l] == 'O':
            if empty_spaces:
                # Mover la 'O' al primer espacio vacío
                first_free_space = empty_spaces.pop(0)
                line[first_free_space], line[pos_l] = line[pos_l], line[first_free_space]
                empty_spaces.append(pos_l)
        elif line[pos_l] == '#':
            empty_spaces = []  # Reiniciar la lista de espacios vacíos
    return line


def summatory_stones(input):
    return sum(line.count('O') * (len(input) - i) for i, line in enumerate(input))


def move_all_stones(matrix):
    return tuple(if_empty_move(tuple(line)) for line in matrix)


def rotate_matrix(matrix, direction):
    if direction == 'left':
        return tuple(tuple(matrix[j][i] for j in range(len(matrix))) 
                     for i in range(len(matrix[0]) - 1, -1, -1))
    elif direction == 'right':
        return tuple(tuple(matrix[j][i] for j in range(len(matrix) - 1, -1, -1)) 
                     for i in range(len(matrix[0])))
    elif direction == 'down':
        return tuple(tuple(reversed(row)) for row in reversed(matrix))


@cache
def one_cycle(matrix):
    matrix = move_all_stones(rotate_matrix(matrix, 'left'))
    matrix = move_all_stones(rotate_matrix(matrix, 'right'))
    matrix = move_all_stones(rotate_matrix(matrix, 'right'))
    matrix = move_all_stones(rotate_matrix(matrix, 'right'))
    return rotate_matrix(matrix, 'down')


def part1(matrix):
    result = rotate_matrix(move_all_stones
                           (rotate_matrix(matrix, 'left')), 'right')
    print(summatory_stones(result))
    return 



def part2(matrix):
    tuple_matrix = tuple(tuple(row) for row in matrix)
    seen_states = {tuple_matrix: 0}  # Almacenar el estado con el ciclo en el que se vio
    pattern_length = None
    pattern_start = None

    for i in range(1, 1000000000):
        tuple_matrix = one_cycle(tuple_matrix)

        if tuple_matrix in seen_states:
            pattern_start = seen_states[tuple_matrix]
            pattern_length = i - pattern_start
            break
        else:
            seen_states[tuple_matrix] = i

    # Si se ha encontrado un patrón
    if pattern_length is not None:
        remaining_cycles = (1000000000 - pattern_start) % pattern_length
        for _ in range(remaining_cycles):
            tuple_matrix = one_cycle(tuple_matrix)

    # Convertir de nuevo a lista de listas para calcular la suma
    matrix = [list(row) for row in tuple_matrix]
    print(summatory_stones(matrix))



input = extract_data(real)

matrix = []
for line in input:
    matrix.append(list(line))

t1 = time()
part1(matrix)
t2 = time()

print(t2-t1)


