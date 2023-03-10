def eat_cookies(presents_left, nice_kids):
    for x, y in directions.items():
        r = santa_pos[0] + x
        c = santa_pos[1] + y
        if neighborhood[r][c].isaplha():
            if neighborhood[r][c] == "V":
                nice_kids += 1
                neighborhood[r][c] = "-"
                presents_left -= 1
        if not presents_left:
            break
    return presents_left, nice_kids

presents = int(input())
size = int(input())
neighborhood = []
santa_pos = []
total_nice_kids = 0
kids_visited = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}
for row in range(size):
    neighborhood.append(input().split())
    if "S" in neighborhood[row]:
        santa_pos = [row, neighborhood[row].index("S")]
        neighborhood[row][santa_pos[1]] = "-"
    if "V" in neighborhood[row]:
        total_nice_kids += neighborhood[row].count("V")


command = input()
while command != "Christmas morning":

    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1]
    ]
    house = neighborhood[santa_pos[0]][santa_pos[1]]
    if house == "V":
        kids_visited += 1
        presents -= 1
    if house == "C":
        presents, kids_visited = eat_cookies(presents, kids_visited)

    neighborhood[santa_pos[0]][santa_pos[1]] = "-"

    if not presents or total_nice_kids == kids_visited:
        break
    command = input()
neighborhood[santa_pos[0]][santa_pos[1]] = "S"

if not presents and kids_visited < total_nice_kids:
    print("Santa ran out of presents!")
[print(*row) for row in neighborhood]

if total_nice_kids == kids_visited:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - kids_visited} nice kid/s.")