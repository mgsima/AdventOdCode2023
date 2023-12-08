import re

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
def format_list(card):
    card_id, numbers = card.split(":")
    winner_numbers, own_numbers = numbers.split("|")
    
    winner_numbers = [int(n) for n in winner_numbers.strip().split()]
    numbers_to_check = [int(n) for n in own_numbers.strip().split()]

    return {
        "card_id": card_id.strip(),
        "winner_numbers": winner_numbers,
        "numbers_to_check": numbers_to_check
    }

# formatted_cards = [format_list(card) for card in example_input]

def format_dict(numbers):
    winner_numbers, own_numbers = numbers.split("|")
    
    winner_numbers = [int(n) for n in winner_numbers.strip().split()]
    numbers_to_check = [int(n) for n in own_numbers.strip().split()]

    return {
        "winner_numbers": winner_numbers,
        "numbers_to_check": numbers_to_check,
        "counter": 0
    }


cards_dict = {}
for card in input:
    card_n, numbers = card.split(":")
    match = re.search(r'Card\s+(\d+)', card_n)
    if match:
        card_name = int(match.group(1))
    else:
        print(f"Formato inesperado para la tarjeta: {card}")
    cards_dict[card_name] = format_dict(numbers)


cache = {}

def card_points(i):
    cards_dict[i]['counter']+=1
    if i in cache:
        wins = cache[i]
    else:    
        card = cards_dict[i]
        win_numbers = card['winner_numbers']
        try_numbers = card['numbers_to_check']
        wins = 1 + sum(1 for num in win_numbers if num in try_numbers)
        cache[i] = wins

    for k in range(1, wins):
        card_points(i+k)


for k in range(1, len(cards_dict)+1):
    card_points(k)

suma = sum(card['counter'] for card in cards_dict.values())


print(suma)
    



