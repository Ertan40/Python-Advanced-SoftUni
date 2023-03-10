from collections import deque
from datetime import datetime, timedelta


robots = {r.split("-")[0]: [int(r.split("-")[1]), 0] for r in input().split(";")}
# {'ROB': [15, 0], 'SS2': [10, 0], 'NX8000': [3, 0]}
factory_time = datetime.strptime(input(), "%H:%M:%S") # input: 8:00:00 factory_time += timedelta(0, 1)
products = deque()

while True:
    product = input()
    if product == "END":
        break
    products.append(product)
while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()

    robots = {r[0]: [r[1][0], r[1][1] - 1] if r[1][1] != 0 else r[1] for r in robots.items()}
    free_robots = list(filter(lambda x: x[1][1] == 0, robots.items()))

    if not free_robots:
        products.append(product)
        continue
    robots[free_robots[0][0]][1] = free_robots[0][1][0]
    print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")




















# data = input().split(";") # ['ROB-15', 'SS2-10', 'NX8000-3']
# robots = {}
# factory_time = datetime.strptime(input(), "%H:%M:%S")
#
# for robs in data: # for robs in input().split(";")
#     name, num = robs.split("-")
#     robots[name] = [num, 0] # {'ROB': ['15', 0], 'SS2': ['10', 0], 'NX8000': ['3', 0]}
#
# robots = {robs.split("-")[0]: [int(robs.split("-")[1]), 0] for robs in input().split(";")}
#          # {name: [time_needed, time_for_curr_task]}
#          # {'ROB': ['15', 0], 'SS2': ['10', 0], 'NX8000': ['3', 0]}
