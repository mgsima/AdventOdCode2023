input = []

with open('./day_4/input.txt', 'r') as f:
    input = [line.strip() for line in f]

example_input = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]


# Convertir cada línea en un formato legible
def format_line(card):
    card_id, numbers = card.split(":")
    winner_numbers, own_numbers = numbers.split("|")
    
    winner_numbers = [int(n) for n in winner_numbers.strip().split()]
    numbers_to_check = [int(n) for n in own_numbers.strip().split()]

    return {
        "card_id": card_id.strip(),
        "winner_numbers": winner_numbers,
        "numbers_to_check": numbers_to_check
    }

# Sacar a cuantos puntos equivalen
def count_points(winners):
    if winners !=0:
        points = 1
        for win in range(winners-1):
            points = points*2
        return points
    else:
        return 0

# Buscar los números ganadores
def sum_winner_points(cards):
    suma = 0
    for card in formatted_cards:
        winner_numbers = card['winner_numbers']
        numbers_to_check = card['numbers_to_check']

        i=0
        for num in winner_numbers:
            if num in numbers_to_check:
                i+=1
        
        points = count_points(i)
        suma = suma + points
    return suma


formatted_cards = [format_line(card) for card in input]

suma = sum_winner_points(formatted_cards)
print(suma)


