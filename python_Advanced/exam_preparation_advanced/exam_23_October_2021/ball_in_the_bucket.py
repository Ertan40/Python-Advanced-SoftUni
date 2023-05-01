board = [[int(i) if i.isdigit() else i for i in input().split()]for _ in range(6)]
prizes = {"Football": [100, 199],
          "Teddy Bear": [200, 299],
          "Lego Construction Set": [300],
}
total_points = 0

for x in range(3):
    data = input()
    if len(data) == 6:
        row, col = int(data[1]), int(data[4])
        if row in range(0, 6) and col in range(0, 6):
            if board[row][col] == "B":
                row, col = [int(data[1]), int(data[4])]
                board[row][col] = 0
                row, col = [5, col]
                while True:
                    if row < 0:
                        break
                    if str(board[row][col]).isdigit():
                        total_points += board[row][col]
                        board[row][col] = 0
                    row += -1

if total_points < 100:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
elif total_points >= 100:
    if prizes["Football"][0] <= total_points <= prizes["Football"][1]:
        print(f"Good job! You scored {total_points} points, and you've won Football.")
    elif prizes["Teddy Bear"][0] <= total_points <= prizes["Teddy Bear"][1]:
        print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
    elif prizes["Lego Construction Set"][0] >= total_points:
        print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")






