from collections import deque

customers = deque(list(map(int, input().split(", "))))
taxis = list(map(int, input().split(", ")))
# deque([4, 6, 8, 5, 1])
# [1, 9, 15, 10, 6]
total_time = 0

while customers and taxis:
    customer = customers.popleft()
    taxi = taxis.pop()
    if taxi >= customer:
        total_time += customer
    else:
        customers.appendleft(customer)

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(c) for c in customers)}")
