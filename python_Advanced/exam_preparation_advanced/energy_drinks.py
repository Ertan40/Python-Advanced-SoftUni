from collections import deque

caffeine = list(map(int, input().split(", ")))  # caffeine.pop() or caffeine[-1]
energy_drinks = deque(list(map(int, input().split(", "))))  # energy_drinks.popleft() or energy_drinks[0]
limit = 300
accepted_caffeine = 0

while caffeine and energy_drinks:
    curr_caffeine = caffeine[-1]
    drink = energy_drinks[0]
    result = curr_caffeine * drink

    if result + accepted_caffeine <= limit:
        caffeine.pop()
        energy_drinks.popleft()
        accepted_caffeine += result
    elif result + accepted_caffeine > limit:
        caffeine.pop()
        energy_drinks.append(energy_drinks.popleft())
        accepted_caffeine -= 30
        if accepted_caffeine < 0:
            accepted_caffeine = 0
            
if energy_drinks:
    print(f"Drinks left: {', '.join([str(i) for i in energy_drinks])}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {accepted_caffeine} mg caffeine.")


