file_path = 'input.txt'

result = 0
winning_numbers = []
ticket_numbers = []

with open(file_path, 'r') as file:
    for line in file:
        numbers = line.split('|')
        winning_numbers.append(numbers[0].split(':')[1].strip().split(' '))
        ticket_numbers.append(numbers[1].strip().split(' '))   

    for i in range(len(winning_numbers)):
        subtotal = 0
        for num in winning_numbers[i]:
            if num != '' and num in ticket_numbers[i]:
                if subtotal == 0:
                    subtotal = 1
                else:
                    subtotal = subtotal * 2
        result += subtotal

print("The result is {}".format(result))
