size = 6
matrix = [input().split(" ") for _ in range(size)]
rovers_movement_commands = input().split(", ")
# ['down', 'right', 'down', 'right', 'down', 'left', 'left', 'left']
row_pos = []
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "E":
            row_pos.append([row, col])

row, col = int(row_pos[0][0]), int(row_pos[0][1])
water_deposit, metal_deposit, concrete_deposit = 0, 0, 0
is_suitable = False

while rovers_movement_commands:
    curr_command = rovers_movement_commands.pop(0)
    if curr_command == "down":
        row += 1
    elif curr_command == "up":
        row += -1
    elif curr_command == "right":
        col += 1
    elif curr_command == "left":
        col += -1

    if not (0 <= row < size and 0 <= col < size):
        if curr_command == "left":
            new_pos = [row, size - 1]
        if curr_command == "right":
            new_pos = [row, 0]
        if curr_command == "up":
            new_pos = [size - 1, col]
        if curr_command == "down":
            new_pos = [0, col]
        row, col = new_pos[0], new_pos[1]

    if matrix[row][col] == "R":
        print(f"Rover got broken at ({row}, {col})")
        break
    elif matrix[row][col] == "W":
        water_deposit += 1
        print(f"Water deposit found at ({row}, {col})")
    elif matrix[row][col] == "C":
        concrete_deposit += 1
        print(f"Concrete deposit found at ({row}, {col})")
    elif matrix[row][col] == "M":
        metal_deposit += 1
        print(f"Metal deposit found at ({row}, {col})")
    if water_deposit >= 1 and concrete_deposit >= 1 and metal_deposit >= 1:
        is_suitable = True

if is_suitable:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")