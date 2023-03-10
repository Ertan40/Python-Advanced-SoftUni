from collections import deque
queue = deque()
pumps = int(input())

for i in range(pumps):
    gus_pump = input().split()
    fuel = int(gus_pump[0])
    distance = int(gus_pump[1])
    queue.append([fuel, distance]) # deque([[1, 5], [10, 3], [3, 4]])

for attempt in range(pumps):
    fuel_tank = 0
    pumps_tracker = 0
    for gus_pump in queue:
        fuel, distance_to_next_pump = int(gus_pump[0]), int(gus_pump[1])
        fuel_tank += fuel
        if fuel_tank < distance_to_next_pump:
            break
        else:
            fuel_tank -= distance_to_next_pump
            pumps_tracker += 1
    if pumps_tracker == len(queue):
        print(attempt)
        break
    queue.rotate(-1) # deque([[10, 3], [3, 4], [1, 5]])
