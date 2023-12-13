from pprint import pprint
from itertools import product
from functools import lru_cache
from time import time
import re

input = []
real = './day_12/input.txt'
example = './day_12/example.txt'

def extract_data(document_input):
    with open(document_input, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    return [(springs, [int(item) for item in check.split(',')]) 
            for springs, check in (line.split(' ') for line in lines)]


def check_if_valid(chain, validation):
    '''
    Pasamos los grupos de combinaciones y lista de comprobaciones. Si coincide, es una forma válida.
    '''
    return all(len(c) == v for c, v in zip(chain, validation))
    

def creating_posibilities(cadena_original, validation):
    # Caracteres para reemplazar '?'
    caracteres = ['#', '.']
    posibilities = 0
    sum_val = sum(validation)
    sum_chain = cadena_original.count('#')

    # Contar cuántos '?' hay en la cadena
    num_interrogantes = cadena_original.count('?')
    
    combinaciones = product(caracteres, repeat=num_interrogantes)

    # Generar todas las combinaciones posibles para los '?'
    for combinacion in combinaciones:
        if combinacion.count('#')+sum_chain == sum_val:
            nueva_cadena = cadena_original
            for c in combinacion:
                nueva_cadena = nueva_cadena.replace('?', c, 1)
            groups_springs = [i for i in nueva_cadena.split('.') if i]
            if len(groups_springs) == len(validation) and check_if_valid(groups_springs, validation):
                posibilities+=1
    return posibilities 


def recursive_springs(springs, damaged):
    if len(springs)==0:
        return 1 if len(damaged) == 0 else 0
        
    if springs[0]== '.':
        return recursive_springs(springs.strip("."), damaged)

    if springs[0] == '?':
        return (recursive_springs(springs.replace("?", "#", 1), damaged) + 
                recursive_springs(springs.replace("?", ".", 1), damaged))


    if springs[0]== '#':
            # Is damaged empty -> 0
            # Are there fewer springs than in the damaged group -> 0
            # Will a "." prevent the placement of the next damaged group -> 0
        if len(damaged) == 0 or len(springs) < damaged[0] or any(s == "." for s in springs[0:damaged[0]]):
            return 0
                        

        if len(damaged)>1:
                # Si el tamaño de springs es más pequeño que el número de grupos->0
                # Tiene que haber un . después de cada grupo
            if len(springs)<damaged[0]+1 or springs[damaged[0]]== '#':
                return 0
            return recursive_springs(springs[damaged[0]+1:], damaged[1:])
        else:
            return recursive_springs(springs[damaged[0]:], damaged[1:])
        


def part1(data):
    pos = 0
    for d in data:
        chain = d[0]
        validation = tuple(d[1])
        pos += recursive_springs(chain, validation)
    return pos


def part2(data):
    unfolded_pos = 0    
    for d in data:
        chain = d[0]
        validation = tuple(d[1])
        unfolded_chain = '?'.join([chain, chain, chain, chain, chain])
        unfolded_validation = validation * 5
        unfolded_pos += recursive_springs(unfolded_chain, unfolded_validation)
    return unfolded_pos


data = extract_data(example)

print(recursive_springs('#???..???', (1, 1, 2)))

t1 = time()
pos = part1(data)
t2 = time()

print(pos)
print(t2-t1)