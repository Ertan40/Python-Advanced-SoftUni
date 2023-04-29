players = input().split(", ")
matrix = [input().split() for _ in range(6)]
first_player, second_player = players[0], players[1]
move = 0
player_to_rest = []

while True:
    current_player = ""
    other_player = ""
    move += 1
    if move % 2 == 0:
        current_player = second_player
        other_player = first_player
    else:
        current_player = first_player
        other_player = second_player
    coordinate = input()  # coordinate = list(int(x) for x in input() if x.isnumeric())
    row, col = int(coordinate[1]), int(coordinate[4])

    if current_player in player_to_rest:
        player_to_rest.remove(current_player)
        continue
    elif matrix[row][col] == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        player_to_rest.append(current_player)
    elif matrix[row][col] == "T":
        print(f"{current_player} is out of the game! The winner is {other_player}.")
        break
    elif matrix[row][col] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break



