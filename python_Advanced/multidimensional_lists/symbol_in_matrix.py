n = int(input())

matrix = [] # => [['A', 'B', 'C'], ['D', 'E', 'F'], ['X', '!', '@']]
for _ in range(n):
    matrix.append(list(input())) # or matrix = [list(input()) for _ in range(n)]

symbol = input()
is_found = False

for row in range(n):
    if is_found:
        break
    for col in range(n):
        if matrix[row][col] == symbol:
            is_found = True
            print(f"({row}, {col})")
            break

if not is_found:
    print(f"{symbol} does not occur in the matrix")

###################### with function ##############################
# def find_symbol(matrix, symbol):
#     for row in range(n):
#         for col in range(n):
#             if matrix[row][col] == symbol:
#                 return row, col
#     return None
#
#
# n = int(input())
# matrix = [list(input()) for _ in range(n)] # => [['A', 'B', 'C'], ['D', 'E', 'F'], ['X', '!', '@']]
# symbol = input()
# result = find_symbol(matrix, symbol)
#
# if result:
#     row, col = result
    print(f"({row}, {col})")
else:
    print(f"{symbol} does not occur in the matrix")

