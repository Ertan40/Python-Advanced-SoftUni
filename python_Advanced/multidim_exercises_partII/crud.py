matrix = [input().split() for _ in range(6)]
position = input()
row, col = int(position[1]), int(position[4])
command = input()
while command != "Stop":
    curr_command = command.split(", ")
    action, direction = curr_command[0], curr_command[1]
    if direction == "up":
        row += -1
    if direction == "down":
        row += 1
    if direction == "left":
        col += -1
    if direction == "right":
        col += 1
    if action == "Create":
        value = curr_command[2]
        if matrix[row][col] == ".":
            matrix[row][col] = value
    if action == "Update":
        value = curr_command[2]
        if matrix[row][col] != ".":
            matrix[row][col] = value
    if action == "Delete":
        if matrix[row][col] != ".":
            matrix[row][col] = "."
    if action == "Read":
        if matrix[row][col] != ".":
            print(matrix[row][col])
    command = input()
for i in matrix:
    print(*i)