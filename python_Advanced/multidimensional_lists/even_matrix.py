matrix = [[int(i) for i in input().split(", ") if int(i) % 2 == 0] for _ in range(int(input()))]
print(matrix)
########################################################
# rows = int(input())
# matrix = []
# for _ in range(rows):
#     matrix.append([int(i) for i in input().split(", ") if int(i) % 2 == 0])
#
# print(matrix)
########################################################
# matrix = [[j for j in range(2)] for i in range(3)]

# matrix = [[0, 1, 3], [0, 1], [0, 1]]
# flattened = [num for sublist in matrix for num in sublist]
# print(flattened) => [0, 1, 3, 0, 1, 0, 1]