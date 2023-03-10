n = int(input())

matrix = [[int(i) for i in input().split()]for _ in range(n)]
primary, secondary = 0, 0
for i in range(n):
    primary += matrix[i][i]
    secondary += matrix[n-i-1][i]

print(abs(primary - secondary))

# n = int(input())
# matrix = [[int(i) for i in input().split(" ")]for _ in range(n)]
#
# primary_diagonals = [matrix[row][row] for row in range(n)]
# secondary_diagonals = [matrix[row][n-row-1] for row in range(n-1, -1, -1)]

print(abs(sum(primary_diagonals) - sum(secondary_diagonals)))