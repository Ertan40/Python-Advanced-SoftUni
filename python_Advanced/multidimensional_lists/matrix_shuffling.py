rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

command = input()
while command != "END":
    operation, *data = [int(x) if x.isdigit() else x for x in command.split()]

    if operation != "swap" or len(data) != 4 or any([True for x in data if x < 0 or x > len(matrix)]):
        print("Invalid input!")

    elif operation == "swap":
        row1, col1, row2, col2 = data
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for row in range(len(matrix)):
            print(' '.join(matrix[row]))
    command = input()
############################### with function #########################################################
# def check_valid_indexes(indexes):
#     if {indexes[0], indexes[2]}.issubset(valid_rows) and {indexes[1], indexes[3]}.issubset(valid_cols):
#         return True
#     return False
#
#
# def swap_command(command, indexes):
#     if check_valid_indexes(indexes) and command == "swap" and len(indexes) == 4:
#         row1, col1, row2, col2 = indexes
#         matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
#         for num in matrix:
#             print(*num)
#     else:
#         print("Invalid input!")
#
#
# rows, cols = [int(i) for i in input().split()]
# matrix = [input().split() for _ in range(rows)]
# valid_rows = range(rows)
# valid_cols = range(cols)
# while True:
#     command_type, *data = [int(i) if i.isdigit() else i for i in input().split()]
#     if command_type == "END":
#         break
#     swap_command(command_type, data)


