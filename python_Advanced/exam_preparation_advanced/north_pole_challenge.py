rows, cols = [int(x) for x in input().split(", ")]
decorations, gifts, cookies = 0, 0, 0
collected_dec, collected_gifts, collected_cookies = 0, 0, 0

matrix = []
for row in range(rows):
    new_row = [x for x in input().split()]
    matrix.append(new_row)
    if "Y" in new_row:
        start_pos = [row, new_row.index("Y")]
    if "D" in new_row:
        decorations += new_row.count("D")
    if "G" in new_row:
        gifts += new_row.count("G")
    if "C" in new_row:
        cookies += new_row.count("C")
row, col = int(start_pos[0]), int(start_pos[1])
directions = {"up": [-1, 0], "down": [1, 0], "right": [0, 1], "left": [0, -1]}
is_collected = False
last_pos = []

command = input()
while command != "End":
    curr_command = command.split("-")
    direction = curr_command[0]  # left
    steps = int(curr_command[1])
    matrix[start_pos[0]][start_pos[1]] = "x"
    for step in range(steps):
        row = row + directions[direction][0]
        col = col + directions[direction][1]
        if not (0 <= row < rows and 0 <= col < cols):
            if direction == "left":
                new_pos = [row, cols - 1]
            if direction == "right":
                new_pos = [row, 0]
            if direction == "up":
                new_pos = [rows - 1, col]
            if direction == "down":
                new_pos = [0, col]
            row, col = new_pos[0], new_pos[1]
        if matrix[row][col] == "D":
            decorations -= 1
            collected_dec += 1
        elif matrix[row][col] == "G":
            gifts -= 1
            collected_gifts += 1
        elif matrix[row][col] == "C":
            cookies -= 1
            collected_cookies += 1
        matrix[row][col] = "x"
        last_pos.append([row, col])
        if decorations == 0 and gifts == 0 and cookies == 0:
            is_collected = True
            break
    if is_collected:
        break
    command = input()

if is_collected:
    print("Merry Christmas!")
print(f"You've collected:")
print(f"- {collected_dec} Christmas decorations")
print(f"- {collected_gifts} Gifts")
print(f"- {collected_cookies} Cookies")
matrix[last_pos[-1][0]][last_pos[-1][1]] = "Y"
for m in matrix:
    print(*m)