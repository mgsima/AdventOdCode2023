from pprint import pprint
from math import gcd

input = []
real = 'D:/Code/advent-of-code-2023/day_8/input.txt'
example = 'D:/Code/advent-of-code-2023/day_8/example1.txt'


def extract_data(document_input):
    with open(document_input, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    turns = []
    for i in lines[0]:
        turns.append(i)

    # Ignora la primera línea si no se usa en esta función
    nodes = {}
    for line in lines[1:]:
        id_node, conections = line.split('=')
        id_node = id_node.strip()
        left, right = conections.replace('(', '').replace(')', '').split(',')
        nodes[id_node] = (left.strip(), right.strip())

    return turns, nodes


def lcm(a, b):
    return a * b // gcd(a, b)

def part2(document_input):
    try:
        # Utilizar la función extract_data para obtener turns y nodes
        turns, nodes = extract_data(document_input)
        starts = [node for node in nodes if node.endswith('A')]

        ans = 1
        for starting_node in starts:
            ctr = 0
            curr = starting_node

            while not curr.endswith('Z'):
                for instruction in turns:
                    if instruction == 'R':
                        curr = nodes[curr][1]
                    else:
                        curr = nodes[curr][0]
                    ctr += 1
                    if curr.endswith('Z'):
                        break
            ans = lcm(ans, ctr)

        print('Part 2:', ans)
    except Exception as error:
        print(error)

part2(real)

