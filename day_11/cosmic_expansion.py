from itertools import combinations      # Make all the posible combinations
from pprint import pprint

input = []
real = './day_11/input.txt'
example = './day_11/example.txt'

def extract_data(document_input):
    with open(document_input, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    return [list(i) for i in lines]


def read_input_file(document_input):
    '''
    Function that gives all the coordinates of the galaxy
    '''
    return [(row, col) for row, line in enumerate(open(document_input))
            for col, ch in enumerate(line) if ch == '#']


input = extract_data(real)



def expand_dimension(dimension_indexes, expansion_size):
    expanded_list = []
    top_limit = max(dimension_indexes) + 1
    expansion_distance = 0

    for i in range(top_limit):
        if i not in dimension_indexes:
            expansion_distance+= expansion_size -1
        expanded_list.append(i+expansion_distance)
    return expanded_list

def sum_of_distances(galaxias, expansion_size):
    rows = set([row for row, _ in galaxias])
    cols = set([col for _, col in galaxias])


    rows_expanded = expand_dimension(rows, expansion_size)
    cols_expanded = expand_dimension(cols, expansion_size)


    print(F"ROWS: {len(rows)} -> {len(rows_expanded)}")
    print(F"COLS: {len(cols)} -> {len(cols_expanded)}")


    # Initialize an empty list to store the expanded positions
    expanded_positions = []

    # Loop through each tuple (row, col) in the 'galaxias' list
    for row, col in galaxias:
        # For each tuple, find the expanded row and column indices
        expanded_row = rows_expanded[row]
        expanded_col = cols_expanded[col]

        # Create a tuple of these expanded indices
        expanded_position = (expanded_row, expanded_col)

        # Add this tuple to the list of expanded positions
        expanded_positions.append(expanded_position)

 
    suma = 0
    for a, b in combinations(expanded_positions, 2):        
        suma += abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    return suma

    

if __name__ == '__main__':
    # Identificar las Galaxias
    coordinate_galaxy = read_input_file(example)
    pprint(coordinate_galaxy)


    print(sum_of_distances(coordinate_galaxy, 2))





