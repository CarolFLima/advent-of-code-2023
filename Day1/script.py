file_path = 'input.txt'

result = 0

with open(file_path, 'r') as file:

    for line in file:
        last_number = None
        first_number = None 
        for char in line:
            if char.isdigit():
                last_number = int(char)
                if first_number is None:
                    first_number = int(char)

        result += int(str(first_number) + str(last_number))

print("The result is {}".format(result))

