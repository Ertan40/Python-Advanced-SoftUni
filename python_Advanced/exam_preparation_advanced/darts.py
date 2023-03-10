player1, player2 = input().split(", ")
matrix = [[int(row) if row.isdigit() else row for row in input().split()]for _ in range(7)]
scoreboard = {"player1": {"name": player1,
                             "score": 501,
                             "throws": 0},
                 "player2": {"name": player2,
                             "score": 501,
                             "throws": 0}}
move = 0
while scoreboard["player1"]["score"] > 0 and scoreboard["player2"]["score"] > 0:
    curr_player = ""
    move += 1
    if move % 2 != 0:
        curr_player = "player1"
    else:
        curr_player = "player2"
    scoreboard[curr_player]["throws"] += 1
    coordinate = input()
    if len(coordinate) == 6:
        row = int(coordinate[1])
        col = int(coordinate[4])
        if 0 <= row < 7 and 0 <= col < 7:
            if matrix[row][col] == "B":
                print(f"{scoreboard[curr_player]['name']} won the game with {scoreboard[curr_player]['throws']} throws!")
                break
            elif str(matrix[row][col]).isdigit():
                scoreboard[curr_player]['score'] -= matrix[row][col]
            elif matrix[row][col] == "T":
                points = (matrix[0][col] + matrix[6][col] + matrix[row][0] + matrix[row][6]) * 3
                scoreboard[curr_player]['score'] -= points
            elif matrix[row][col] == "D":
                points = (matrix[0][col] + matrix[6][col] + matrix[row][0] + matrix[row][6]) * 2
                scoreboard[curr_player]['score'] -= points

    if scoreboard[curr_player]["score"] <= 0:
        print(f'{scoreboard[curr_player]["name"]} won the game with {scoreboard[curr_player]["throws"]} throws!')
        break

