size = int(input())
racing_number = input()
kilometers_passed = 0
matrix = []    # matrix = [input().split() for _ in range(size)]
for _ in range(size):
    matrix.append(input().split())

tunnel_pos = []
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "T":
            tunnel_pos.append([row, col])

last_tunnel_pos = tunnel_pos[1]   # [3, 1]
row, col = [0, 0]
race_is_over = False
command = input()

while command != "End":
    if matrix[row][col] == "F":
        matrix[row][col] = "C"
        kilometers_passed += 10
        race_is_over = True
        break
    if command == "down":
        row += 1
        if matrix[row][col] == ".":
            kilometers_passed += 10
        if matrix[row][col] == "T":
            matrix[row][col] = "."
            row, col = [last_tunnel_pos[0], last_tunnel_pos[1]]
            matrix[row][col] = "."
            kilometers_passed += 30
    if command == "right":
        col += 1
        if matrix[row][col] == ".":
            kilometers_passed += 10
        if matrix[row][col] == "T":
            matrix[row][col] = "."
            row, col = [last_tunnel_pos[0], last_tunnel_pos[1]]
            matrix[row][col] = "."
            kilometers_passed += 30
    if command == "up":
        row += -1
        if matrix[row][col] == ".":
            kilometers_passed += 10
        if matrix[row][col] == "T":
            matrix[row][col] = "."
            row, col = [last_tunnel_pos[0], last_tunnel_pos[1]]
            matrix[row][col] = "."
            kilometers_passed += 30
    if command == "left":
        col += -1
        if matrix[row][col] == ".":
            kilometers_passed += 10
        if matrix[row][col] == "T":
            matrix[row][col] = "."
            row, col = [last_tunnel_pos[0], last_tunnel_pos[1]]
            matrix[row][col] = "."
            kilometers_passed += 30
    command = input()

if command == "End":
    if matrix[row][col] == ".":
        matrix[row][col] = "C"
    print(f"Racing car {racing_number} DNF.")
if race_is_over:
    print(f"Racing car {racing_number} finished the stage!")
print(f"Distance covered {kilometers_passed} km.")
for path in matrix:
    print(''.join(path))