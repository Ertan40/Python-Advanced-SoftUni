size = int(input())
commands = input().split(", ")
matrix = [[i for i in input()]for _ in range(size)]

squirrel_position = []
collected = 0
ended_by_trap = False
ended_by_collected = False
ended_by_out_of_field = False

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "s":
            squirrel_position.append([row, col])

row, col = int(squirrel_position[0][0]), int(squirrel_position[0][1])

while commands:
    curr_command = commands.pop(0)
    if curr_command == "down":
        row += 1
    elif curr_command == "up":
        row += -1
    elif curr_command == "right":
        col += 1
    elif curr_command == "left":
        col += -1
    if 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "t":
            print(f"Unfortunately, the squirrel stepped on a trap...")
            print(f"Hazelnuts collected: {collected}")
            ended_by_trap = True
            break
        elif matrix[row][col] == "h":
            collected += 1
            matrix[row][col] = "*"

    if collected == 3:
        print(f"Good job! You have collected all hazelnuts!")
        print(f"Hazelnuts collected: {collected}")
        ended_by_collected = True
        break

    if not (0 <= row < size and 0 <= col < size):
        print(f"The squirrel is out of the field.")
        print(f"Hazelnuts collected: {collected}")
        ended_by_out_of_field = True
        break

if not commands and not ended_by_out_of_field and not ended_by_collected and not ended_by_trap:
    print("There are more hazelnuts to collect.")
    print(f"Hazelnuts collected: {collected}")

