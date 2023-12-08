from pprint import pprint

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
    print('datos importados')
    return categories


def find_location(seed, categorized_data):
    prev_category = seed
    for category, mappings in categorized_data.items():
        if category != 'seeds':
            for destination_range_start, source_range_start, range_length in mappings:
                if source_range_start <= prev_category <= source_range_start + range_length:
                    prev_category = destination_range_start + (prev_category - source_range_start)
                    break  # Una vez que encontramos el mapeo, salimos del bucle interno

    return prev_category

def process_seed_range(start_range, range_length, categorized_data):
    seed_range = range(start_range, start_range + range_length)
    # Aplicar find_location a cada semilla en el rango y encontrar la mínima localización
    locations = map(lambda seed: find_location(seed, categorized_data), seed_range)
    return min(locations)


# Uso de la función
categorized_data = categorize_data(data_example)


min_location = float('inf')  # Asumimos que min_location está definido en alguna parte del código

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
    



