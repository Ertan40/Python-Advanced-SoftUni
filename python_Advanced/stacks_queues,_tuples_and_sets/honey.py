from collections import deque
bees = deque(list(map(int, input().split())))
nectar = list(map(int, input().split()))
symbols = deque(input().split())
total_honey = 0

while nectar and bees:
    if nectar[-1] >= bees[0]:
        current_symbol = symbols.popleft()
        if current_symbol == "+":
            total_honey += bees[0] + nectar[-1]
        elif current_symbol == "-":
            total_honey += abs(bees[0] - nectar[-1])
        elif current_symbol == "*":
            total_honey += abs(bees[0] * nectar[-1])
        elif current_symbol == "/":
            if bees[0] > 0 and nectar[-1] > 0:
                total_honey += abs(bees[0] / nectar[-1])
        bees.popleft()
        nectar.pop()
    elif nectar[-1] < bees[0]:
        nectar.pop()

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(b) for b in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(n) for n in nectar)}")


