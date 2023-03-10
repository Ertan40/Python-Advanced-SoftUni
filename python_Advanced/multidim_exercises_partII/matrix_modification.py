n = int(input())
matrix = [[int(i) for i in input().split()]for _ in range(n)]

command = input()
while command != "END":
    command_type, *data = command.split()
    value, row, col = int(data[-1]), int(data[0]), int(data[1])
    # command_type, row, col, value = [int(x) if x[-1].isdigit() else x for x in command.split()]
    if not(0 <= row < n and 0 <= col < n):
    # if row < 0 or col < 0 or row >= n or col >= n:
        print(f"Invalid coordinates")
        command = input()
        continue

    if command_type == "Add":
        matrix[row][col] += value
    elif command_type == "Subtract":
        matrix[row][col] -= value
    command = input()
for num in matrix:
    print(*num)