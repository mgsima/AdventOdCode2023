'''
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

Your puzzle answer was 509115.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
'''

import re

input_file = 'day_3_input.txt'
input = []

special_characters = ['*', '-', '#', '/', '=', '%', '$', '&', '@', '+']
patron = re.compile(r'\d+')


with open(input_file, 'r') as f:
    input = [line.strip() for line in f]

def determine_target_list_bounds(line_number, position, length):
    line = input[line_number]
    line_length = len(line)

    # Asegurarse de que los índices no se salgan de los límites
    prev_index = max(position - 1, 0)
    post_index = min(position + length, line_length - 1)

    # Obtener los caracteres previos y posteriores
    prev = line[prev_index]
    post = line[post_index]

    # Determinar los límites de target_list basado en los caracteres adyacentes
    if prev in special_characters or prev.isdigit():
        start = prev_index
    else:
        start = position

    if post in special_characters or post.isdigit():
        end = post_index + 1
    else:
        end = position + length

    return start, end


def check_gear_same_line(line_number, position, length):
    line = input[line_number]
    line_length = len(line)

    # Ajustar los índices para asegurarse de no salir de los límites de la línea
    start = max(position - 4, 0)
    end = min(position + length + 4, line_length)

    target_list_longer = input[line_number][start:end]  


    relative_star_position = target_list_longer.find('*')

    if target_list_longer[relative_star_position-1].isdigit() and target_list_longer[relative_star_position+1].isdigit():
        coinc = patron.finditer(target_list_longer)
        gears = []
        for c in coinc:
            gears.append(int(c.group()))
        return gears[0]*gears[1]
    else:
        return 0




def check_gear(line_number, position, length, number):
    line = input[line_number]
    line_length = len(line)

    # Asegurarse de que los índices no se salgan de los límites
    start, end = determine_target_list_bounds(line_number, position, length)

    # tenemos un número y su posición
    target_list = input[line_number][start:end]

        

    # comprobamos si hay una estrella en la misma línea del target
    if '*' in target_list:
        try:
            gear_ratio = check_gear_same_line(line_number, position, length)
            if gear_ratio:
                return gear_ratio
        except:
            pass


    # Comprobamos que hay una estrella debajo del número
    if line_number+1 < len(input):
        under_target_line = input[line_number+1]

        prev_index = max(position - 1, 0)
        post_index = min(position + length + 1, line_length - 1)
        under_target_list = under_target_line[prev_index:post_index]
    else:
        return 0


    if '*' in under_target_list:
        relative_star_position = under_target_list.find('*') 
        star_position = relative_star_position + prev_index 

        prev_star_index = max(star_position-1, 0)
        post_star_index = min(star_position+1, line_length-1)

        # Buscamos dos números en dos líneas consecutivas 
        numbers_next_to_star = under_target_line[prev_star_index:post_star_index]
        for char in numbers_next_to_star:
            if char.isdigit():                        
                under_target_list_longer = under_target_line[position-4:position+length+5]
                coinc = patron.finditer(under_target_list_longer)
                for c in coinc:
                    start_s, end_s = c.span()
                    if start_s<=relative_star_position+2<end_s:
                        target_number =  int(patron.findall(target_list)[0])
                        second_gear_number = int(c.group())
                        return second_gear_number*target_number


        # Buscamos los números que esten en dos líneas separadas conectados por una estrella en medio

        if line_number+2 < len(input):
            under_star_line = input[line_number+2]
        else:
            return 0

        line_under_star_list = under_star_line[position-3:position+length+3]
        number_under_star_list = under_star_line[star_position-1:star_position+2]
        
        for char in number_under_star_list:
            if char.isdigit():
                coinc = patron.finditer(line_under_star_list)
                for c in coinc:
                    start_s, end_s = c.span()
                    if start_s<=relative_star_position+2<end_s:
                        target_number =  int(patron.findall(target_list)[0])
                        second_gear_number = int(c.group())
                        return second_gear_number*target_number
  

     
suma = 0

for line_number in range(len(input)):
        for coincidence in patron.finditer(input[line_number]):
            number = coincidence.group()
            position = coincidence.start()  
            gear_ratio = check_gear(line_number, position, len(number), number)
            if gear_ratio:
                suma = suma + gear_ratio

print(suma)








'''
    for j in i:
        if j == '.' or j.isdigit() or j in special_characters:
            pass
        else:
            special_characters.append(j)
    print(special_characters)
    '''