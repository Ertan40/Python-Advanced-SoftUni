def find_count(board, row, col):
    moves = [[row - 2, col - 1],
             [row - 2, col + 1],
             [row - 1, col - 2],
             [row - 1, col + 2],
             [row + 1, col - 2],
             [row + 1, col + 2],
             [row + 2, col - 1],
             [row + 2, col + 1]
             ]
    result = 0
    for r, c in moves:
        if 0 <= r < n and 0 <= c < n and board[r][c] == "K":
            result += 1
    return result


n = int(input())
board = [[i for i in input()] for _ in range(n)]
# board = []
# for _ in range(n):
#     board.append(list(input()))
removed_knights_counter = 0
while True:
    max_knight_count = 0
    knight_row = 0
    knight_col = 0
    for row in range(n):
        for col in range(n):
            if board[row][col] == "0":
                continue

            count = find_count(board, row, col)
            if count > max_knight_count:
                max_knight_count = count
                knight_row = row
                knight_col = col
    if max_knight_count == 0:
        break

    board[knight_row][knight_col] = "0"
    removed_knights_counter += 1
print(removed_knights_counter)
