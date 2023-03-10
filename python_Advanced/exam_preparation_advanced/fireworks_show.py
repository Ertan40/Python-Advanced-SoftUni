from collections import deque
fireworks = deque(list(map(int, input().split(", "))))  # fireworks_effects[0] or fireworks_effects.popleft()
explosive_power = list(map(int, input().split(", ")))  # explosive_power[-1] or explosive_power.pop()
palm_counter, willow_counter, crossette_counter = 0, 0, 0
success = False

while True:
    if not fireworks or not explosive_power:
        if palm_counter >= 3 and willow_counter >= 3 and crossette_counter >= 3:
            success = True
        break
    if palm_counter >= 3 and willow_counter >= 3 and crossette_counter >= 3:
        success = True
        break
    current_firework = fireworks[0]
    current_explosive = explosive_power[-1]
    if current_firework <= 0:
        fireworks.popleft()
        continue
    elif current_explosive <= 0:
        explosive_power.pop()
        continue

    power_of_firework = current_firework + current_explosive
    if power_of_firework % 3 == 0 and power_of_firework % 5 != 0:
        palm_counter += 1
        fireworks.popleft()
        explosive_power.pop()
    elif power_of_firework % 3 != 0 and power_of_firework % 5 == 0:
        willow_counter += 1
        fireworks.popleft()
        explosive_power.pop()
    elif power_of_firework % 3 == 0 and power_of_firework % 5 == 0:
        crossette_counter += 1
        fireworks.popleft()
        explosive_power.pop()
    else:
        current_firework -= 1
        fireworks.popleft()
        fireworks.append(current_firework)

if success:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")
if fireworks:
    print(f"Firework Effects left: {', '.join(str(firework) for firework in fireworks)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(power) for power in explosive_power)}")
print(f"Palm Fireworks: {palm_counter}")
print(f"Willow Fireworks: {willow_counter}")
print(f"Crossette Fireworks: {crossette_counter}")

# ------------------------------------- second way ------------------------
# from collections import deque
#
# fireworks = deque(int(x) for x in input().split(", ") if 0 < int(x))
# explosives = [int(x) for x in input().split(", ") if 0 < int(x)]
# palm_firework, willow_firework, crossette_firework = 0, 0, 0
# firework_show = False
# while True:
#     if not fireworks or not explosives:
#         if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
#             firework_show = True
#             break
#     if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
#         firework_show = True
#         break
#     firework = fireworks.popleft()
#     explosive = explosives.pop()
#     sum_of_values = firework + explosive
#
#     if sum_of_values % 3 == 0 and sum_of_values % 5 != 0:
#         palm_firework += 1
#
#     elif sum_of_values % 5 == 0 and sum_of_values % 3 != 0:
#         willow_firework += 1
#
#     elif sum_of_values % 5 == 0 and sum_of_values % 3 == 0:
#         crossette_firework += 1
#
#     else:
#         fireworks.append(firework - 1)
#         explosives.append(explosive)
#
# if firework_show:
#     print("Congrats! You made the perfect firework show!")
# else:
#     print("Sorry. You can't make the perfect firework show.")
# if fireworks:
#     print(f"Firework Effects left: {', '.join(str(f) for f in fireworks)}")
# if explosives:
#     print(f"Explosive Power left: {', '.join(str(f) for f in explosives)}")
#
# print(f"Palm Fireworks: {palm_firework}")
# print(f"Willow Fireworks: {willow_firework}")
# print(f"Crossette Fireworks: {crossette_firework}")