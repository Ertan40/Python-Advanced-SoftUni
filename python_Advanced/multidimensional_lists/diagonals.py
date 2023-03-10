n = int(input())

matrix = [[int(i) for i in input().split(", ")]for _ in range(n)]

primary_diagonals = [matrix[row][row] for row in range(n)]
secondary_diagonals = [matrix[row][n-row-1] for row in range(n-1, -1, -1)]

print(f"Primary diagonal: {', '.join(str(i) for i in primary_diagonals)}. Sum: {sum(primary_diagonals)}")
print(f"Secondary diagonal: {', '.join([str(i) for i in secondary_diagonals][::-1])}. Sum: {sum(secondary_diagonals)}")

############################ longer version ####################################
# matrix = [[int(i) for i in input().split(", ")]for i in range(int(input()))]
# # matrix = []
# # for i in range(int(input())): # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# #     matrix.append([int(i) for i in input().split(", ")])
# sum_primary = 0
# primary_nums = []
# for row in range(len(matrix)):
#     for col in range(len(matrix)):
#         if row == col:
#             sum_primary += matrix[row][col]
#             primary_nums.append(matrix[row][col])
# sum_secondary = 0
# secondary_nums = []
# for row in range(len(matrix)):
#     for col in range(len(matrix)):
#         if row == len(matrix) - col - 1:
#             sum_secondary += matrix[row][col]
#             secondary_nums.append(matrix[row][col])
#
# print(f"Primary diagonal: {', '.join(str(i) for i in primary_nums)}. Sum: {sum_primary}")
# print(f"Secondary diagonal: {', '.join(str(i) for i in secondary_nums)}. Sum: {sum_secondary}")
