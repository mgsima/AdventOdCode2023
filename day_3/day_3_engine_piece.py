import re

input_file = 'day_3_input.txt'
input = []

special_characters = ['*', '-', '#', '/', '=', '%', '$', '&', '@', '+']

with open(input_file, 'r') as f:
    input = [line.strip() for line in f]


def check_adjacent_number(line_number, position, len):
    for i in range(position-1, position+len+1):
        try: 
            if input[line_number-1][i] in special_characters:
                return True
        except:
            pass
    for i in range(position-1, position+len+1):
        try: 
            if input[line_number][i] in special_characters:
                return True
        except:
            pass
    for i in range(position-1, position+len+1):
        try: 
            if input[line_number+1][i] in special_characters:
                return True
        except:
            pass
    return False
    

     
suma = 0

for line_number in range(len(input)):
        patron = re.compile(r'\d+')
        for coincidence in patron.finditer(input[line_number]):
            number = coincidence.group()
            position = coincidence.start()
            adjacent = check_adjacent_number(line_number, position, len(number))
            if adjacent:
                suma = suma + int(number)

print(suma)








'''
    for j in i:
        if j == '.' or j.isdigit() or j in special_characters:
            pass
        else:
            special_characters.append(j)
    print(special_characters)
    '''