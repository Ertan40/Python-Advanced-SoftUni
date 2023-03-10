rows, cols = [int(i) for i in input().split()]
matrix = [input().split() for _ in range(rows)] # because it is string

equal_cells = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        symbol = matrix[row][col]
        if symbol == matrix[row][col+1] and symbol == matrix[row+1][col] and symbol == matrix[row+1][col+1]:
            equal_cells += 1

print(equal_cells)