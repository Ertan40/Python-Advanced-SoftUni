n = int(input())
matrix = []
bunny_pos = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}
for row in range(n):
    matrix.append(input().split())
    if "B" in matrix[row]:
        bunny_pos = [row, matrix[row].index("B")]

max_sum = 0
best_direction = ""
best_path = []
for direction, positions in directions.items():
    row, col = [bunny_pos[0] + positions[0], bunny_pos[1] + positions[1]]
    current_path = []
    current_sum = 0
    while 0 <= row < n and 0 <= col < n and matrix[row][col] != "X":
        current_sum += int(matrix[row][col])
        current_path.append([row, col])
        row += positions[0]
        col += positions[1]

    if current_sum >= max_sum:
        max_sum = current_sum
        best_path = current_path
        best_direction = direction

print(best_direction)
print(*best_path, sep="\n")
print(max_sum)




# size = int(input())
# matrix = []
# bunny_row, bunny_col = 0, 0
# for row in range(size):
#     row_elements = input().split()
#     for col in range(size):
#         if row_elements[col] == "B":
#             bunny_col = col
#             bunny_row = row
#     matrix.append(row_elements)
#
# directions = {
#     "up": lambda r, c: (r - 1, c),
#     "down": lambda r, c: (r + 1, c),
#     "right": lambda r, c: (r, c + 1),
#     "left": lambda r, c: (r, c - 1),
# }
# max_sum = 0
# best_direction = ""
# best_coordinates = []
# for direction in directions:
#
#     current_sum = 0
#     row, col = directions[direction](bunny_row, bunny_col)
#     current_coordinates = []
#     while 0 <= row < size and 0 <= col < size and matrix[row][col] != "X":
#         current_sum += int(matrix[row][col])
#         current_coordinates.append([row, col])
#         row, col = directions[direction](row, col)
#     if current_sum > max_sum:
#         max_sum = current_sum
#         best_direction = direction
#         best_coordinates = current_coordinates
# print(best_direction)
# print(*best_coordinates, sep="\n")
# print(max_sum)