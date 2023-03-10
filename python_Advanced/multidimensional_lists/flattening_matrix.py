rows = int(input())

matrix = []
for _ in range(rows):
    matrix.append([int(i) for i in input().split(", ")])

flattening = [num for sublist in matrix for num in sublist]
print(flattening)
