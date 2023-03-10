from collections import deque
chocolate = list(map(int, input().split(", ")))  # [20, 24, -5, 17, 22, 60, 26] from end
milk = deque(list(map(int, input().split(", "))))  # deque([26, 60, 22, 17, 24, 10, 55]) from start
milkshake_counter = 0
milkshake_goal = 5

while milkshake_counter < milkshake_goal and chocolate and milk:
    removed_below_zero = False
    if chocolate[-1] <= 0:
        chocolate.pop()
        removed_below_zero = True
    if milk[0] <= 0:
        milk.popleft()
        removed_below_zero = True
    if not removed_below_zero:
        if chocolate[-1] == milk[0]:
            milkshake_counter += 1
            chocolate.pop()
            milk.popleft()
        elif chocolate[-1] != milk[0]:
            milk.append(milk.popleft())
            chocolate[-1] -= 5

if milkshake_counter == milkshake_goal:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join(str(c) for c in chocolate)}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join(str(m) for m in milk)}")
else:
    print("Milk: empty")
