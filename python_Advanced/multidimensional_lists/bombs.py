n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
# [[8, 3, 2, 5], [6, 4, 7, 9], [9, 9, 3, 6], [6, 8, 1, 2]]
coordinates = [[int(i) for i in coordinate.split(",")]for coordinate in input().split()]
# [[1, 2], [2, 1], [2, 0]]
directions = (
    (-1, 0),   # up
    (1, 0),    # down
    (0, 1),    # right
    (0, -1),   # left
    (-1, 1),   # top-right
    (-1, -1),  # top-left
    (1, -1),   # bottom-left
    (1, 1),    # bottom-right
    (0, 0),    # current
)
for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue

    for x, y in directions:
        r, c = row + x, col + y
        if 0 <= r < n and 0 <= c < n:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0

alive_cells = []
for row in range(n):  # alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]
    for num in matrix[row]:
        if num > 0:
            alive_cells.append(num)
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for nums in matrix:  # [print(*matrix[r], sep=" ") for r in range(n)]
    print(*nums)