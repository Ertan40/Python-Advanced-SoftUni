string = input()
size = int(input())
matrix = [[col for col in input()] for row in range(size)]
initial_pos = []

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "P":
            initial_pos.append([row, col])
            matrix[row][col] = "-"
row, col = int(initial_pos[0][0]), int(initial_pos[0][1])

number_of_commands = int(input())
for command in range(number_of_commands):
    curr_command = input()
    matrix[row][col] = "-"
    if curr_command == "down":
        row += 1
        if 0 <= row < size and 0 <= col < size:
            if matrix[row][col] != "-":
                string += matrix[row][col]
            matrix[row][col] = "P"
            position = [row, col]
        else:
            if string:
                string = string[:-1]
                matrix[position[0]][position[1]] = "P"

    if curr_command == "right":
        col += 1
        if 0 <= row < size and 0 <= col < size:
            if matrix[row][col] != "-":
                string += matrix[row][col]
            matrix[row][col] = "P"
            position = [row, col]
        else:
            if string:
                string = string[:-1]
                matrix[position[0]][position[1]] = "P"

    if curr_command == "up":
        row += -1
        if 0 <= row < size and 0 <= col < size:
            if matrix[row][col] != "-":
                string += matrix[row][col]
            matrix[row][col] = "P"
            position = [row, col]
        else:
            if string:
                string = string[:-1]
                matrix[position[0]][position[1]] = "P"

    if curr_command == "left":
        col += -1
        if 0 <= row < size and 0 <= col < size:
            if matrix[row][col] != "-":
                string += matrix[row][col]
            matrix[row][col] = "P"
            position = [row, col]
        else:
            if string:
                string = string[:-1]
                matrix[position[0]][position[1]] = "P"
print(string)
for m in matrix:
    print(*m)

# --------------------------------- second way -----------------------------
# start_string = input()
# size = int(input())
# field = []
# position = []
# for row in range(size):
#     new_row = [x for x in input()]
#     field.append(new_row)
#     if "P" in new_row:
#         position = [row, new_row.index("P")]
#
# directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
# number_of_commands = int(input())
# for command in range(number_of_commands):
#     direction = input()
#     field[position[0]][position[1]] = "-"
#     row = position[0] + directions[direction][0]
#     col = position[1] + directions[direction][1]
#     if row in range(0, len(field)) and col in range(0, len(field[0])):
#         if field[row][col] != "-":
#             start_string += field[row][col]
#         field[row][col] = "P"
#         position = [row, col]
#     else:
#         if start_string:
#             start_string = start_string[:-1:]
#             position = [position[0], position[1]]
#             field[position[0]][position[1]] = "P"
# print(start_string)
# for row in field:
#     print("".join(x for x in row ))





