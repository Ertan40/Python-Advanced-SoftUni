size = int(input())
matrix = [[i for i in input()]for _ in range(size)]
food_quantity, burrow_pos, snake_pos = 0, [], []

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "S":
            snake_pos.append([row, col])
            matrix[int(snake_pos[0][0])][int(snake_pos[0][1])] = "."
        if matrix[row][col] == "B":
            burrow_pos.append([row, col]) # [[1, 4], [4, 2]]
        else:
            continue

row, col = int(snake_pos[0][0]), int(snake_pos[0][1])
if burrow_pos:
    last_burrow_pos = burrow_pos[1]
while True:
    direction = input()
    matrix[row][col] = "."
    if direction == "down":
        row += 1
    elif direction == "up":
        row += -1
    elif direction == "right":
        col += 1
    elif direction == "left":
        col += -1
    if not (0 <= row < size and 0 <= col < size):
        print("Game over!")
        break

    if matrix[row][col] == "B":
        matrix[row][col] = "."
        position = [last_burrow_pos[0], last_burrow_pos[1]]
        row, col = [position[0], position[1]]
        matrix[row][col] = "."
    if matrix[row][col] == "*":
        food_quantity += 1
        matrix[row][col] = "."
    if food_quantity == 10:
        matrix[row][col] = "S"
        print("You won! You fed the snake.")
        break

print(f"Food eaten: {food_quantity}")
for m in matrix:
    print(''.join(m))