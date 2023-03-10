matrix = []
position = []
shot_targets = 0
shot_targets_pos = []
total_targets = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}
for row in range(5):
    matrix.append(input().split())
    if "A" in matrix[row]:
        position = [row, matrix[row].index("A")]
        matrix[row][position[1]] = "."
    total_targets += matrix[row].count("x")
    # if "x" in matrix[row]:
    #     total_targets += matrix[row].count("x")
row, col = int(position[0]), int(position[1])
n = int(input())

for _ in range(n):
    command = input().split()
    action = command[0]
    direction = command[1]
    if action == "move":
        steps = int(command[2])
        curr_row = position[0] + (directions[direction][0] * steps)
        curr_col = position[1] + (directions[direction][1] * steps)

        if 0 <= curr_row < len(matrix) and 0 <= curr_col < len(matrix):
            if matrix[curr_row][curr_col] == ".":
                position = [curr_row, curr_col]  # new coordinates

    elif action == "shoot":
        r = position[0] + directions[direction][0]
        c = position[1] + directions[direction][1]
        while 0 <= r < len(matrix) and 0 <= c < len(matrix):
            if matrix[r][c] == "x":
                shot_targets += 1
                matrix[r][c] = "."
                shot_targets_pos.append([r, c])
                break
            r += directions[direction][0]
            c += directions[direction][1]
        if total_targets == shot_targets:
            break

if total_targets == shot_targets:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets - shot_targets} targets left.")
print(*shot_targets_pos, sep="\n")

# def move(direction, steps):
#
#     curr_row = position[0] + (directions[direction][0] * steps)
#     curr_col = position[1] + (directions[direction][1] * steps)
#     if not (0 <= curr_row < len(matrix) and 0 <= curr_col < len(matrix)):
#         return position
#     if matrix[curr_row][curr_col] == "x":
#         return position
#
#     return [row, col]
#
# def shoot(direction):
#     r = position[0] + directions[direction][0]
#     c = position[1] + directions[direction][1]
#     while 0 <= r < n and 0 <= c < n:
#         if matrix[r][c] == "x":
#             matrix[r][c] = "."
#             return [r, c]
#
#         r += directions[direction][0]
#         c += directions[direction][1]
#
#
# matrix = []
# position = []
# targets_hit = 0
# shot_targets_pos = []
# total_targets = 0
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "right": (0, 1),
#     "left": (0, -1),
# }
# for row in range(5):
#     matrix.append(input().split())
#     if "A" in matrix[row]:
#         position = [row, matrix[row].index("A")]
#         matrix[row][position[1]] = "."
#     total_targets += matrix[row].count("x")
#     # if "x" in matrix[row]:
#     #     total_targets += matrix[row].count("x")
#
# row, col = int(position[0]), int(position[1])
# n = int(input())
#
# for _ in range(n):
#     command = input().split()
#     action = command[0]
#     direction = command[1]
#     if action == "move":
#         steps = int(command[2])
#         position = move(direction, steps)
#     elif action == "shoot":
#         target_down_pos = shoot(direction)
#
#         if target_down_pos:
#             shot_targets_pos.append(target_down_pos)
#             targets_hit += 1
#         if total_targets == targets_hit:
#             print(f"Training completed! All {total_targets} targets hit.")
#             break
#
# else:
#     print(f"Training not completed! {total_targets - targets_hit} targets left.")
#
# print(*shot_targets_pos, sep="\n")