data = input().split()
rows = int(data[0])
cols = int(data[1])
matrix = [[x for x in input().split(" ")]for _ in range(rows)]

start_pos = []
for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == "B":
            start_pos.append([row, col])

row, col = int(start_pos[0][0]), int(start_pos[0][1])
moves = 0
touched_opponent = 0
touched_all = False
command = input()
while command != "Finish":
    if command == "up":
        row += -1
    elif command == "down":
        row += 1
    elif command == "right":
        col += 1
    elif command == "left":
        col += -1
    if not (0 <= row < rows and 0 <= col < cols):
        if command == "up":
            row += +1
        elif command == "down":
            row += -1
        elif command == "right":
            col += -1
        elif command == "left":
            col += +1
        moves -= 1
        position = [row, col]

    if matrix[row][col] == "O":
        if command == "up":
            row += +1
        elif command == "down":
            row += -1
        elif command == "right":
            col += -1
        elif command == "left":
            col += +1
        moves -= 1
        position = [row, col]
        row, col = position[0], position[1]

    elif matrix[row][col] == "P":
        touched_opponent += 1
        matrix[row][col] = "-"
    moves += 1
    if touched_opponent == 3:
        print("Game over!")
        print(f"Touched opponents: {touched_opponent} Moves made: {moves}")
        touched_all = True
        break
    command = input()

if not touched_all:
    print("Game over!")
    print(f"Touched opponents: {touched_opponent} Moves made: {moves}")
