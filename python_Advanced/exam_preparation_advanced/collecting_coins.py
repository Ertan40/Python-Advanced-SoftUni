import math

size = int(input())
position = []
field = []
total_coins = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}
current_position = []
for row in range(size):
    field.append(input().split())
    if "P" in field[row]:
        position = [row, field[row].index("P")]
        field[row][position[1]] = "."

row, col = int(position[0]), int(position[1])  # (3, 0)
current_position.append([row, col])

while total_coins < 100:
    direction = input()
    row = row + directions[direction][0]  # directions[direction][0] = row
    col = col + directions[direction][1]  # directions[direction][1] = col

    if direction not in directions:
        continue
    if not (0 <= row < size and 0 <= col < size):  # is_outside and reposition it
        if direction == "left":
            reposition = [row, size - 1]
            if field[reposition[0]][reposition[1]].isdigit():
                total_coins += int(field[reposition[0]][reposition[1]])
                field[reposition[0]][reposition[1]] = "."
            row = reposition[0]
            col = reposition[1]

        if direction == "right":
            reposition = [row, 0]
            if field[reposition[0]][reposition[1]].isdigit():
                total_coins += int(field[reposition[0]][reposition[1]])
                field[reposition[0]][reposition[1]] = "."
            row = reposition[0]
            col = reposition[1]

        if direction == "up":
            reposition = [size - 1, col]
            if field[reposition[0]][reposition[1]].isdigit():
                total_coins += int(field[reposition[0]][reposition[1]])
                field[reposition[0]][reposition[1]] = "."
            row = reposition[0]
            col = reposition[1]

        if direction == "down":
            reposition = [0, col]
            if field[reposition[0]][reposition[1]].isdigit():
                total_coins += int(field[reposition[0]][reposition[1]])
                field[reposition[0]][reposition[1]] = "."
            row = reposition[0]
            col = reposition[1]

    current_position.append([row, col])
    player_pos = [row, col]
    position = field[row][col]

    if field[row][col] == "X":
        total_coins = total_coins - (total_coins * 0.5)
        print(f"Game over! You've collected {math.floor(total_coins)} coins.")
        break
    if position.isdigit():
        total_coins += int(position)
    field[row][col] = "."

if total_coins >= 100:
    print(f"You won! You've collected {math.floor(total_coins)} coins.")
print('Your path:')

for pos in current_position:
    print(pos)


# ---------------------------- not my solution -----------------------------

# from math import floor
# n = int(input())
# field = [input().split() for _ in range(n)]
# player_pos = [0, 0]
# movement = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
# path = []
# coins = 0
#
#
# def game_over():
#     global coins
#     if coins > 0:
#         coins /= 2
#     print(f"Game over! You've collected {floor(coins)} coins.")
#     print("Your path:")
#     [print(p) for p in path]
#     raise SystemExit
#
#
# for row in range(n):
#     for col in range(n):
#         if field[row][col] == "P":
#             player_pos = [row, col]
# while True:
#     command = input()
#     row, col = player_pos
#     if command in movement:
#         row += movement[command][0]
#         col += movement[command][1]
#     else:
#         continue
#     if not (0 <= row < n and 0 <= col < n):
#         game_over()
#     current_pos = field[row][col]
#     if current_pos.isdigit():
#         coins += int(current_pos)
#     elif current_pos == "X":
#         game_over()
#     player_pos = [row, col]
#     path.append([row, col])
#     if coins >= 100:
#         print(f"You won! You've collected {coins} coins.")
#         print("Your path:")
#         [print(p) for p in path]
#         break



