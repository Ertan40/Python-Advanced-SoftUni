from collections import deque
times = deque(list(map(int, input().split())))
tasks = list(map(int, input().split()))

# deque([10, 15, 12, 18, 22, 6])
# [12, 16, 5, 6, 9, 1]
presents_are_made = False
duck_type = {"Darth Vader Ducky": 0, "Thor Ducky": 0, "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}
while times and tasks:
    time = times.popleft()
    task = tasks.pop()
    total = time * task
    if total > 240:
        times.append(time)
        tasks.append(task - 2)
    if 0 <= total <= 60:
        duck_type["Darth Vader Ducky"] += 1
    elif 61 <= total <= 121:
        duck_type["Thor Ducky"] += 1
    elif 121 <= total <= 180:
        duck_type["Big Blue Rubber Ducky"] += 1
    elif 181 <= total <= 240:
        duck_type["Small Yellow Rubber Ducky"] += 1

    if duck_type["Darth Vader Ducky"] >= 1 and duck_type["Thor Ducky"] >= 1 and duck_type["Big Blue Rubber Ducky"] >= 1 and duck_type["Small Yellow Rubber Ducky"] >= 1:
        presents_are_made = True

count1 = duck_type["Darth Vader Ducky"]
count2 = duck_type["Thor Ducky"]
count3 = duck_type["Big Blue Rubber Ducky"]
count4 = duck_type["Small Yellow Rubber Ducky"]

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {count1}")
print(f"Thor Ducky: {count2}")
print(f"Big Blue Rubber Ducky: {count3}")
print(f"Small Yellow Rubber Ducky: {count4}")




