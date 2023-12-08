'''
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; 
however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes
 of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. 
If any color had even one fewer cube, the game would have been impossible.

Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.

The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. 
The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. 
Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
'''

list_games = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 
 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', 
 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

input_file = 'day_2_input.txt'
input = []

with open(input_file, 'r') as f:
    input = [line.strip() for line in f]
   


suma = 0

def min_power_games(game):

    max_red = 0
    max_green = 0
    max_blue = 0
    # Separar el identificador de las bolas
    game_number, games_set = game.split(':')
    _, game_id = game_number.split(' ')

    # Separar los diferentes sets
    game_set = games_set.split(';')
    for i in game_set:
    # Separar los números del color
        number_of_colors = i.split(',')
        for j in number_of_colors:
            _, number_balls, color = j.split(' ')
            number_balls = int(number_balls)

            if color == 'red':
                if number_balls > max_red:
                    max_red = number_balls
            elif color == 'blue':
                if number_balls > max_blue:
                    max_blue = number_balls
            elif color == 'green':
                if number_balls > max_green:
                    max_green = number_balls
    power = 1
    if max_green > 0:
        power *= max_green
    if max_blue > 0:
        power *= max_blue
    if max_red > 0:
        power *= max_red

    print(f'sum:{power}\nred:{max_red}, blue:{max_blue}, green:{max_green}')
    return power


for i in input:
    suma = suma + min_power_games(i)
print(suma)
