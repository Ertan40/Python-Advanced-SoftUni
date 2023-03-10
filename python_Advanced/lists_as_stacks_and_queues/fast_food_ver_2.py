from collections import deque
quantity_of_food = int(input())
orders = deque(map(int, input().split()))
print(max(orders))

for _ in range(len(orders)):
    if orders[0] <= quantity_of_food:
        quantity_of_food -= orders.popleft()
    else:
        break
if orders:
    # orders_into_str = map(str, orders)
    # print(f"Orders left: {' '.join(orders_into_str)}")
    result = ""
    for _ in range(len(orders)):
        result += str(orders.popleft()) + " "
    print(f"Orders left: {result}")
else:
    print("Orders complete")