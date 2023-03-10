from collections import deque
cups = deque(list(map(int, input().split()))) # deque([int(cup) for cup in input().split()])
bottles = list(map(int, input().split())) # [int(bottle) for bottle in input().split()]
wasted_water = 0

while cups and bottles:
    current_cup = cups[0]  # cups.popleft()
    current_bottle = bottles[-1]  # bottles.pop()
    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
        cups.popleft()
        bottles.pop()
    elif current_bottle < current_cup:
        current_cup -= current_bottle
        bottles.pop()
        if current_cup <= 0:
            cups.popleft()
        else:
            cups[0] = current_cup
if bottles:
    result = ""
    for b in bottles:
        result += str(b) + " "
    print(f"Bottles: {result}", end=' ')
    # print(f"Bottles: {' '.join(str(bottle) for bottle in bottles)}")
if cups:
    result = ""
    for c in cups:
        result += str(c) + " "
    print(f"Cups: {result}", end=' ')
    # print(f"Cups: {' '.join(str(cup) for cup in cups)}") then remove  \n
print(f"\nWasted litters of water: {wasted_water}")

