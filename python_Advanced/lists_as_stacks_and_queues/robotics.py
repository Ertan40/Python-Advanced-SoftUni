from collections import deque
data = input().split(";") # ['ROB-15', 'SS2-10', 'NX8000-3'] data[0].split("-")[0] = ROB
free_robots_dict = {}
working_robots_dict = {}
product_deque = deque()
working_deque = deque()
for robs in data:
    robot_data = robs.split("-")
    working_robots_dict[robot_data[0]] = int(robot_data[1]) # {'ROB': 15, 'SS2': 10, 'NX8000': 3}
    free_robots_dict[robot_data[0]] = -1 # {'ROB': -1, 'SS2': -1, 'NX8000': -1}

starting_time = list(map(int, input().split(":"))) # [8, 0, 0] or [7, 59, 59]
hh = starting_time[0]
mm = starting_time[1]
ss = starting_time[2]
while True:
    product = input()
    if product == "End":
        break
    product_deque.append(product)  # deque(['detail ', 'glass ', 'wood ', 'apple '])
while product_deque or working_deque:
    ss += 1
    if product_deque:
        working_deque.append(product_deque.popleft())
    if ss == 60:
        ss = 0
        mm += 1
    if mm == 60:
        mm = 0
        hh += 1
    if hh == 24:
        hh = 0
    for rob in free_robots_dict:
        if working_deque:
            if free_robots_dict[rob] == -1:
                free_robots_dict[rob] = 0
                print(f"{rob} - {working_deque.popleft()} [{hh:02d}:{mm:02d}:{ss:02d}]")
                continue
            elif free_robots_dict[rob] > -1:
                free_robots_dict[rob] += 1
                if free_robots_dict[rob] >= working_robots_dict[rob]:
                    free_robots_dict[rob] = -1
                    if working_deque:
                        free_robots_dict[rob] = 0
                        print(f"{rob} - {working_deque.popleft()} [{hh:02d}:{mm:02d}:{ss:02d}]")
                        continue
        else:
            if free_robots_dict[rob] > -1:
                free_robots_dict[rob] += 1
                if free_robots_dict[rob] >= working_robots_dict[rob]:
                    free_robots_dict[rob] = -1
    else:
        if working_deque:
            product_deque.append(working_deque.popleft())




