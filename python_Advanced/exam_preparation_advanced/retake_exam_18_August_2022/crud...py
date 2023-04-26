size = 6
matrix = [input().split() for _ in range(size)]

start_pos = input()
row, col = int(start_pos[1]), int(start_pos[4])

command = input().split(", ")
while command[0] != "Stop":
    action = command[0]
    direction = command[1]
    if direction == "up":
        row += -1
    if direction == "down":
        row += 1
    if direction == "left":
        col += -1
    if direction == "right":
        col += 1
    if action == "Create":
        value = command[2]
        if matrix[row][col] == ".":
            matrix[row][col] = value

    if action == "Read":
        if matrix[row][col] != ".":
            print(matrix[row][col])

    if action == "Update":
        value = command[2]
        if matrix[row][col] != ".":
            matrix[row][col] = value

    if action == "Delete":
        if matrix[row][col] != ".":
            matrix[row][col] = "."
    command = input().split(", ")

for m in matrix:
    print(*m)