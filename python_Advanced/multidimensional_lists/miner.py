n = int(input())
commands = input().split() # ['up', 'right', 'right', 'up', 'right']
matrix = []
minor_position = []
collected_coal, total_coal = 0, 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}
for row in range(n):
    matrix.append(input().split())  # [['*', '*', '*', 'e'], ['*', '*', 'c', '*'], ['*', 's', '*', 'c']]
    if "s" in matrix[row]:
        minor_position = [row, matrix[row].index("s")]
        matrix[row][minor_position[1]] = "*"
    total_coal += matrix[row].count("c")
for command in commands:
    r, c = minor_position[0] + directions[command][0], minor_position[1] + directions[command][1]
    if not (0 <= r < n and 0 <= c < n):
        continue
    minor_position = [r, c]
    if matrix[r][c] == "c":
        collected_coal += 1
        if total_coal == collected_coal:
            print(f"You collected all coal! ({r}, {c})")
            break
    elif matrix[r][c] == "e":
        print(f"Game over! ({r}, {c})")
        break
    matrix[r][c] = "*"
else:
    print(f"{total_coal-collected_coal} pieces of coal left. ({r}, {c})")
