import re

file_path = 'input.txt'

result = 0

with open(file_path, 'r') as file:
    for i, line in enumerate(file):
        max_red = 1
        max_blue = 1
        max_green = 1

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

            if red_amount > max_red:
                max_red = red_amount
            if green_amount > max_green:
                max_green = green_amount
            if blue_amount > max_blue:
                max_blue = blue_amount

        result = result + (max_red * max_green * max_blue)    

print("The result is {}".format(result))

