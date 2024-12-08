from collections import deque
# deque([32, 42, 7, 28, 3])
# [1, 5, 6]
bees = deque([int(b) for b in input().split(" ")])
bee_eaters = [int(b) for b in input().split(" ")]

while bees and bee_eaters:
    current_bees = bees.popleft()
    current_bee_eaters = bee_eaters.pop()
    while current_bees > 0 and current_bee_eaters > 0:
        if current_bee_eaters * 7 <= current_bees:
            current_bees -= current_bee_eaters * 7
            current_bee_eaters = 0
        else:
            current_bee_eaters -= (current_bees // 7)
            current_bees = 0

    if current_bees > 0 and current_bee_eaters == 0:
        bees.append(current_bees)
    elif current_bees == 0 and current_bee_eaters > 0:
        bee_eaters.append(current_bee_eaters)


print("The final battle is over!")
if not bees and not bee_eaters:
    print("But no one made it out alive!")
if bees:
    print(f"Bee groups left: {', '.join(str(b) for b in bees)}")
if bee_eaters:
    print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters))}")