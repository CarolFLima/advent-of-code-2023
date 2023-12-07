file_path = 'input.txt'

result = 0
matrix = []

def has_adjacent_symbol(i, j, matrix):
    prev_row = max(i-1, 0)
    next_row = min(i+1, 139)
    prev_col = max(j-1, 0)
    next_col = min(j+1, 139)

    #First row
    if not matrix[prev_row][prev_col].isalnum() or not matrix[prev_row][j].isalnum() or not matrix[prev_row][next_col].isalnum():
            return True
    #Second row
    if not matrix[i][prev_col].isalnum() or not matrix[i][next_col].isalnum():
            return True
    #Third row
    if not matrix[next_row][prev_col].isalnum() or not matrix[next_row][j].isalnum() or not matrix[next_row][next_col].isalnum():
            return True
    return False

with open(file_path, 'r') as file:
    for line in file:
        matrix.append(line.replace('.', 'M'))

    i = 0; is_adjacent = False

    while i < 140:
        j = 0; num = ''; is_adjacent = False
        while j < 140:
            char = matrix[i][j]
            if char.isdigit():
                num = num + char
                is_adjacent = has_adjacent_symbol(i, j, matrix) or is_adjacent
            else:
                if is_adjacent and num != "":
                    result += int(num)
                num = ''
                is_adjacent = False
            if j==139 and is_adjacent and num != "":
                 result += int(num)
            j += 1

        i += 1

print("The result is {}".format(result))
