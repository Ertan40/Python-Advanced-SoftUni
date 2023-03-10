from collections import deque
orders = deque(int(o) for o in input().split(", ") if 0 < int(o) <= 10)
employees = list(map(int, input().split(", ")))
total_count = 0

while orders and employees:
    current_order = orders.popleft()
    current_capacity = employees.pop()

    if current_order > current_capacity:
        total_count += current_capacity
        remained = current_order - current_capacity
        orders.appendleft(remained)
        continue
    total_count += current_order

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_count}")
    print(f"Employees: {', '.join([str(e) for e in employees])}")
elif orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(o) for o in orders])}")


