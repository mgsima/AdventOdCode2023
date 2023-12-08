'''
The newly-improved calibration document consists of lines of text; each line originally contained a 
specific calibration value that the Elves now need to recover. On each line, the calibration value can be 
found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

PART II

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: 
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. 

For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. 
Adding these together produces 281.
'''

input_file = 'day_1_input.txt'

char_numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
    }

input = []

with open(input_file, 'r') as f:
    input= f.readlines()


example = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']   
example2 = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four','4nineeightseven2', 'zoneight234', '7pqrstsixteen']



def find_first(string):
    for char in range(len(string)):
        if string[char].isdigit():
            return string[char]
        # Verificar si a partir de aquí, algo coincide con las char_numbers keys. 
        else:
            for key in char_numbers.keys():
                if string[char:].startswith(key):
                    return char_numbers[key]
                
def find_last(string):
    for char in range(len(string)-1,-1,-1):
        if string[char].isdigit():
            return string[char]
        # Verificar si a partir de aquí, algo coincide con las char_numbers keys. 
        else:
            for key in char_numbers.keys():
                if string[char:].startswith(key):
                    return char_numbers[key]

def find_numbers(string):
    first = find_first(string)
    last = find_last(string)
    return int(str(first) + str(last))
    
def find_sum(input):
    sum = 0
    for i in input:
        sum = find_numbers(i) + sum
    return sum
            

print(find_sum(input))
