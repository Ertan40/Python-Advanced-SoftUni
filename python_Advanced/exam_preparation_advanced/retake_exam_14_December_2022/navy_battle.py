size = int(input())
matrix = [[i for i in input()] for _ in range(size)]
start_pos = []
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "S":
            start_pos.append([row, col])
            matrix[row][col] = "-"
row, col = int(start_pos[0][0]), int(start_pos[0][1])

destroyed_cruisers = 0
total_hit_by_mine = 0
last_position = []
last_position_destroyed = []
while True:
    command = input()
    if command == "right":
        col += 1
    elif command == "left":
        col += -1
    elif command == "down":
        row += 1
    elif command == "up":
        row += -1
    if matrix[row][col] == "C":
        matrix[row][col] = "-"
        destroyed_cruisers += 1
        last_position_destroyed.append([row, col])
    elif matrix[row][col] == "*":
        matrix[row][col] = "-"
        total_hit_by_mine += 1
        last_position.append([row, col])
    elif matrix[row][col] == "-":
        continue
    if total_hit_by_mine == 3:
        matrix[last_position[-1][0]][last_position[-1][1]] = "S"
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{last_position[-1][0]}, {last_position[-1][1]}]!")
        break
    if destroyed_cruisers == 3:
        matrix[last_position_destroyed[-1][0]][last_position_destroyed[-1][1]] = "S"
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break
for m in matrix:  # [print(''.join(matrix[row])) for row in range(size)]
    print(''.join(m))
