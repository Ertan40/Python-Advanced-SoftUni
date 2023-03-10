n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])
    sum_primary = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if row == col:
                sum_primary += matrix[row][col]

print(sum_primary)
############################## with function ##########################
# def get_diagonal(mat):
#     sum_diagonal = 0
#     for r in range(len(mat)):
#         for c in range(len(mat)):
#             if r == c:
#                 sum_diagonal += mat[r][c]
#     return sum_diagonal
#
# 
# n = int(input())
# matrix = []
# for _ in range(n):
#     matrix.append([int(i) for i in input().split()])
#
# print(get_diagonal(matrix))

