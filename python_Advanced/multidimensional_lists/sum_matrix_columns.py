############ sum matrix columns ################
rows, cols = [int(i) for i in input().split(", ")]
matrix = []

for row in range(rows):
    matrix.append([int(i) for i in input().split()])

for col in range(cols):
    total_cols = 0
    for row in range(rows):
        total_cols += matrix[row][col]
    print(total_cols)
####################### second - way ##############
# rows, cols = [int(i) for i in input().split(", ")]
# matrix = []
# sum_cols = [0] * cols
# for _ in range(rows):
#     matrix.append([int(i) for i in input().split()])
#
# for row in range(rows):
#     for col in range(cols):
#         sum_cols[col] += matrix[row][col]
#
# [print(x) for x in sum_cols]
############# sum matrix elements ################
# rows, cols = [int(i) for i in input().split(", ")]
# total_sum = 0
# matrix = []
# for _ in range(rows):
#     matrix.append([int(i) for i in input().split(", ")])
#
# for row in range(rows):
#     for col in range(cols):
#         total_sum += matrix[row][col]
# print(total_sum)
# print(matrix)