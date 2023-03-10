import sys
start_row, start_col = [int(i) for i in input().split(", ")]
matrix = []
for _ in range(start_row): # matrix = [[int(col) for col in input().split(", ")] for row in range(start_row)]
    matrix.append([int(i) for i in input().split(", ")])
    # [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]
best_square = {
    "sum": -sys.maxsize,
    "numbers": [],
}
for row in range(start_row):
    for col in range(start_col):
        if 0 <= row + 2 <= start_row and 0 <= col + 2 <= start_col:
            current_numbers = []
            for check_row in range(row, row + 2):
                for check_col in range(col, col + 2):
                    current_numbers.append(matrix[check_row][check_col]) # [5, 6, 1, 0]
            if sum(current_numbers) > best_square["sum"]:
                best_square["sum"] = sum(current_numbers)
                best_square["numbers"] = current_numbers

print(*best_square["numbers"][:2])
print(*best_square["numbers"][2:])
print(sum(best_square["numbers"]))
