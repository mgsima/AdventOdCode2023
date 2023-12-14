from functools import cache
from time import time
input = []
real = './day_14/input.txt'
example = './day_14/example.txt'
# Optimización: Utilizando listas y operaciones de lista eficientes
def if_empty_move(line):
    result = list(line)
    free_spaces = []

    for pos, char in enumerate(line):
        if char == '.':
            free_spaces.append(pos)
        elif char == 'O' and free_spaces:
            result[free_spaces.pop(0)] = 'O'
            result[pos] = '.'
            free_spaces.append(pos)
        elif char == '#':
            free_spaces.clear()

    return ''.join(result)

def move_all_stones(matrix):
    return [''.join(if_empty_move(''.join(row))) for row in matrix]

def rotate_matrix(matrix, direction):
    if direction == 'left':
        return [''.join(row) for row in zip(*matrix[::-1])]
    elif direction == 'right':
        return [''.join(row) for row in zip(*matrix)][::-1]
    elif direction == 'down':
        return [row[::-1] for row in matrix[::-1]]

@cache  # Memoización para mejorar la eficiencia
def one_cycle(matrix):
    matrix = move_all_stones(rotate_matrix(matrix, 'left'))
    matrix = move_all_stones(rotate_matrix(matrix, 'right'))
    matrix = move_all_stones(rotate_matrix(matrix, 'right'))
    matrix = move_all_stones(rotate_matrix(matrix, 'right'))
    return rotate_matrix(matrix, 'down')

def extract_data(document_input):
    with open(document_input, 'r') as f:
        return [line.strip() for line in f.readlines()]

def summatory_stones(input):
    return sum(line.count('O') * (len(input) - i) for i, line in enumerate(input))

# Ejecución del código
input_data = extract_data(example)
matrix = input_data

t1 = time()
for _ in range(1000000000):  # Ejemplo con 100 iteraciones
    matrix = one_cycle(tuple(matrix))  # Usar tuplas para garantizar inmutabilidad
t2 = time()
print(t2 - t1)

suma = summatory_stones(matrix)
print(suma)
