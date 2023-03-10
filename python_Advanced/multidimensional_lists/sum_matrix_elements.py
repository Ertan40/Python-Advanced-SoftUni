rows, cols = [int(i) for i in input().split(", ")]
total_sum = 0
matrix = []
for _ in range(rows):
    matrix.append([int(i) for i in input().split(", ")])

for row in range(rows):
    for col in range(cols):
        total_sum += matrix[row][col]

print(total_sum)
print(matrix)


# matrix = []   # just an example
#
# for _ in range(3):
#     row = []
#     for i in range(3):
#         row.append(i)
#     matrix.append(row)
# print(matrix)