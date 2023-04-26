# ----------------------------------------- 87 points ---------------------------------------
size = int(input())
bombs = int(input())
directions = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, 1], [1, -1]]

matrix = []
for row in range(size):
    new_row = []
    for col in range(size):
        new_row.append(".")
    matrix.append(new_row)

for _ in range(bombs):
    coordinate = input()
    if len(coordinate) == 6:
        row = int(coordinate[1])
        col = int(coordinate[4])
        matrix[row][col] = "*"

for row in range(size):
    for col in range(size):
        counter = 0
        if matrix[row][col] == ".":
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if 0 <= new_row < size and 0 <= new_col < size:
                    if matrix[new_row][new_col] == "*":
                        counter += 1
            matrix[row][col] = counter
for path in matrix:
    print(*path)


