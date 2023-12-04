file_path = 'input.txt'

result = 0

with open(file_path, 'r') as file:

    for line in file:
        last_number = None
        first_number = None 
        i = 0
        numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

        while i < len(line):
            char = line[i]
            if char.isdigit():
                last_number = int(char)
                if first_number is None:
                    first_number = int(char)
            else:
                match_digit = 0
                for j, number in enumerate(numbers):
                    if char == number[0]:
                        if line[i:i+(len(number))] == number:
                            match_digit = j+1
                            break
                if match_digit > 0:
                    if first_number is None:
                        first_number = match_digit
                    last_number = match_digit
            i += 1
                    
        result += int(str(first_number) + str(last_number))

print("The result is {}".format(result))

