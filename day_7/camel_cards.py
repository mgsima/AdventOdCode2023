from pprint import pprint
from collections import defaultdict
from functools import cmp_to_key

input = []
real = './day_7/input.txt'
example = './day_7/example.txt'
cards_rank= "AKQT98765432J"



def extract_data(input):
    with open(input, 'r') as f:
        input = [line.strip() for line in f]

    games = ()
    for i in input:
        parts = i.split(' ')
        games += ((parts[0], int(parts[1])),)
    return games


def get_type(hand):
     # creamos un diccionario que cree la key si no existe
    hand_set = defaultdict(int)

    if 'J' in hand:
        j=0
        for i in hand:
            if i != 'J':
                hand_set[i]+=1
            else:
                j+=1
        
        if j == 5:
            type_hand = [5]

        else:
            type_hand = sorted(hand_set.values())
            for k in range(j):
                type_hand[-1]+=1
        
    else:
        for i in hand:
            hand_set[i]+=1
            type_hand = sorted(hand_set.values())

    if type_hand==[5]:
        return 7
    
    if type_hand==[1, 4]:
        return 6

    if type_hand==[2, 3]:
        return 5
    
    if type_hand==[1, 1, 3]:
        return 4
    
    if type_hand==[1, 2, 2]:
        return 3
    
    if type_hand==[1, 1, 1, 2]:
        return 2
    
    return 1


def compare_hands(hand_A, hand_B):
    rankA = get_type(hand_A)
    rankB = get_type(hand_B)

    if rankA==rankB:
        if hand_A==hand_B:
            return 0
        
        for i, j in zip(hand_A, hand_B):
            if cards_rank.index(i)<cards_rank.index(j):
                return 1
    
            if cards_rank.index(i)>cards_rank.index(j):
                return -1
        
        return -1

    if rankA > rankB:
        return 1
    return -1


games = extract_data(real)   # (hand, bid)

for game in games:
    hand = get_type(game[0])

games_sorted = sorted(games, key=cmp_to_key(lambda x, y: compare_hands(x[0], y[0])))

result = 0
rank = 1
for i in games_sorted:
    result += i[1]* rank
    rank+=1

print(result)

