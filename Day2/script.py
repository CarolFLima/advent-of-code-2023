import re

file_path = 'input.txt'

result = 0

with open(file_path, 'r') as file:
    for i, line in enumerate(file):
        is_valid = True
        for round in line.split(';'):

            blue_amount = 0
            red_amount = 0
            green_amount = 0

            blue_match = re.search(r'(\d+)\s+blue', round)
            red_match = re.search(r'(\d+)\s+red', round)
            green_match = re.search(r'(\d+)\s+green', round)

            if blue_match:
                blue_amount = int(blue_match.group(1))
            if red_match:
                red_amount = int(red_match.group(1))
            if green_match:
                green_amount = int(green_match.group(1))

            if blue_amount > 14 or red_amount > 12 or green_amount > 13:     
                is_valid = False
                break
       
        if is_valid:
            result = result + (i+1)    
print("The result is {}".format(result))

