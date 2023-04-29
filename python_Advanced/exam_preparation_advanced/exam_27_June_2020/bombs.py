from collections import deque

effects = deque(list(map(int, input().split(", "))))  # bomb_effects.popleft()
casings = list(map(int, input().split(", ")))   # bomb_casings.pop()
bombs = {"Datura": 0,
         "Cherry": 0,
         "Smoke Decoy": 0,
         }
is_bombs_pouch = False
while effects and casings:
    effect = effects.popleft()
    casing = casings.pop()
    created_bomb = effect + casing
    if 40 <= created_bomb < 60:
        bombs["Datura"] += 1
        # effects.popleft()
        # casings.pop()
    elif 60 <= created_bomb < 120:
        bombs["Cherry"] += 1
        # effects.popleft()
        # casings.pop()
    elif created_bomb >= 120:
        bombs["Smoke Decoy"] += 1
        # effects.popleft()
        # casings.pop()
    else:
        casings.append(casing - 5)
    if bombs["Datura"] >= 3 and bombs["Cherry"] >= 3 and bombs["Smoke Decoy"] >= 3:
        is_bombs_pouch = True
        break
if is_bombs_pouch:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")
if effects:
    print(f"Bomb Effects: {', '.join([str(e) for e in effects])}")
else:
    print(f"Bomb Effects: empty")
if casings:
    print(f"Bomb Casings: {', '.join([str(c) for c in casings])}")
else:
    print(f"Bomb Casings: empty")

for name, quantity in sorted(bombs.items()):
    print(f"{name} Bombs: {quantity}")

