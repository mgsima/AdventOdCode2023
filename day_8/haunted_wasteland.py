from pprint import pprint
input = []
real = './day_8/input.txt'
example = './day_8/example1.txt'

end = 'ZZZ'


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


turns, nodes = extract_data(real)
node = 'AAA'



i=0
top = len(turns)
jumps = 0

while node != end:
    print(node)
    if turns[i]=='L':
        node = nodes[node][0]
        jumps += 1
    elif turns[i]=='R':
        node = nodes[node][1]
        jumps += 1
    
    i+=1
    if i == top:
        i=0

print(jumps)