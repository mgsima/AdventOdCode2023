from itertools import pairwise, accumulate, takewhile
input = []
real = './day_9/input.txt'
example = './day_9/example.txt'


def extract_data(document_input):
    with open(document_input, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    return [list(map(int, i.split(' '))) for i in lines]


def array_diference(reading):
    return [b - a for a, b in pairwise(reading)]


def check_zeros(array):
    return all(x == 0 for x in array)


def next_value(array):
    for i in range(len(array)-2, -1, -1):
        array[i-1].append(array[i][-1]+array[i-1][-1])
    return array[0][-1]


def get_sum_part1(document):

    readings = extract_data(document)
    result = 0

    for reading in readings:
        lista = array_diference(reading)
        extrapolations = [reading, lista]
        while not check_zeros(lista):
            lista = array_diference(lista)
            extrapolations.append(lista)
        result += next_value(extrapolations)

    return result


def previous_value(array):
    for i in range(len(array)-2, -1, -1):
        array[i].insert(0, array[i][0]-array[i+1][0])
    return array[0][0]


def get_sum_part2(document):
    readings = extract_data(document)
    result = 0

    for reading in readings:
        lista = array_diference(reading)
        extrapolations = [reading, lista]
        while not check_zeros(lista):
            lista = array_diference(lista)
            extrapolations.append(lista)
        result += previous_value(extrapolations)

    return result



result = get_sum_part1(example)
print(result)