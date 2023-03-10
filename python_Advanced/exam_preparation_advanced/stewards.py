from collections import deque
seats = input().split(", ")
first_sequence = deque(list(map(int, input().split(", "))))
second_sequence = deque(list(map(int, input().split(", "))))
total_rotations = 0
total_match = []

while True:
    if len(total_match) >= 3 or total_rotations >= 10:
        break
    first = first_sequence.popleft()
    second = second_sequence.pop()
    match = chr(first + second)
    curr_first = str(first) + match  # 20B
    curr_second = str(second) + match  # 46B
    if curr_first in seats:
        total_match.append(curr_first)
        seats.remove(curr_first)
    elif curr_second in seats:
        total_match.append(curr_second)
        seats.remove(curr_second)
    elif curr_first not in seats and curr_second not in seats:
        first_sequence.append(first)
        second_sequence.appendleft(second)
    total_rotations += 1

print(f"Seat matches: {', '.join(str(m) for m in total_match)}")
print(f"Rotations count: {total_rotations}")



