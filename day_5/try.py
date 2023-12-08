from pprint import pprint
import numpy as np

input = []
with open('./day_5/input.txt', 'r') as f:
    input = [line.strip() for line in f]

data_example = [
    "seeds: 79 14 55 13",
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4"
]


def categorize_data(data):
    print('importando datos')
    categories = {
        "seeds": (),
        "seed-to-soil map": (),
        "soil-to-fertilizer map": (),
        "fertilizer-to-water map": (),
        "water-to-light map": (),
        "light-to-temperature map": (),
        "temperature-to-humidity map": (),
        "humidity-to-location map": ()
    }

    current_category = None
    for line in data:
        if ':' in line:
            # Separar el nombre de la categoría y los datos iniciales
            parts = line.split(':')
            current_category = parts[0]

            # Si hay datos después del ':', añadirlos directamente
            if len(parts) > 1 and parts[1].strip():
                categories[current_category] += tuple(int(element) for element in parts[1].strip().split(' '))
        elif current_category:
            if line:
                data_line = tuple(int(element) for element in line.strip().split(' '))
                categories[current_category] += (data_line,)
    return categories


def find_location(seeds, categorized_data):

    for category, mappings in categorized_data.items():
        original_seeds = seeds.copy()  # Copiar las semillas originales
        already_mapped = np.zeros_like(seeds, dtype=bool)  # Inicializar una máscara para rastrear los mapeos
        if category != 'seeds':
            for destination_range_start, source_range_start, range_length in mappings:
                mask = ((source_range_start <= original_seeds) & 
                        (original_seeds <= source_range_start + range_length) &
                        ~already_mapped)  # Solo considerar semillas no mapeadas
                seeds[mask] = destination_range_start + (original_seeds[mask] - source_range_start)
                already_mapped[mask] = True  # Actualizar la máscara para las semillas mapeadas
    print(seeds)
    return seeds


def process_seed_range(start_range, range_length, categorized_data):
    seed_range = np.arange(start_range, start_range + range_length)
    locations = find_location(seed_range, categorized_data)
    return np.min(locations)

# Uso de la función
categorized_data = categorize_data(input)

min_location = float('inf')
is_range = False
for seed in categorized_data['seeds']:
    if not is_range:
        is_range = True
        start_range = seed
    else:
        is_range = False
        range_length = seed
        min_location = min(min_location, process_seed_range(start_range, range_length, categorized_data))

print(f'min: {min_location}')





    



