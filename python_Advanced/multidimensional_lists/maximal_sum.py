import sys
rows, cols = [int(i) for i in input().split()]
matrix = [[int(i) for i in input().split()] for _ in range(rows)]

max_sum = -sys.maxsize  # max_sum = float("-inf")
biggest_square = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_row = matrix[row][col:col + 3]
        second_row = matrix[row + 1][col:col + 3]
        third_row = matrix[row + 2][col:col + 3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if current_sum > max_sum:
            max_sum = current_sum
            biggest_square = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
for nums in biggest_square: # or [print(*biggest_square[row]) for row in range(3)]
    print(*nums)
