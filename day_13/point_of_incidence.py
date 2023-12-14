from pprint import pprint
from itertools import pairwise


input = []
real = './day_13/input.txt'
example = './day_13/example.txt'

def extract_data(document_input):
    with open(document_input, 'r') as f:
        lines = f.readlines()
    
    patterns = []
    pattern = []
    for line in lines:
        if line == '\n':
            patterns.append(pattern)
            pattern = []
            continue        
        elif line == lines[-1]:
            pattern.append(line.strip())
            patterns.append(pattern)
            pattern = []
            continue
        pattern.append(line.strip())
    
    return patterns

def transpose_pattern(pattern):
    return [''.join(row) for row in zip(*pattern)]


def find_reflection(pattern, smudges=0):

    # vamos línea por línea para ver si coinciden las listas anteriores
    # con las líneas posteriores
    for i in range(len(pattern)):

        # si llegamos al final devolvemos 0
        if i+1 == len(pattern):
            return 0
        
        # creamos pares de cada línea
        pairs = []

        # ejemplo i=2 pattern ['A', 'B', 'C', 'C', 'B', 'A']
            # creamos dos listas: ['C', 'B', 'A'] <-> ['C', 'B', 'A']
        for line_a, line_b in zip(pattern[i::-1], pattern[i+1:]):

                # emparejamos cada elemento en parejas [('C', 'C'), ('B', 'B'), ('A', 'A')].
                # las que no tienen pareja, no aparecen aquí.
            for a, b in zip(line_a, line_b):
                pairs.append((a, b))

        # ahora comprobamos si cada pareja contiene el mismo elemento.
        matching_pairs = 0
        for a, b in pairs:
            if a == b:
                matching_pairs += 1

        # si todos las parejas tienen matches devolvemos en qué indice estamos.
        # En caso de que esté permitido los smudges, permitimos que una pareja no
        # se igual.
        if len(pairs) - smudges == matching_pairs:
            return i + 1





patterns = extract_data(example)

partl = 0
part2 = 0
for i in patterns:
    partl += find_reflection(i)*100 + find_reflection(transpose_pattern(i))
    part2 += find_reflection(i, 1)*100 + find_reflection(transpose_pattern(i),1)

print(partl)
print(part2)



