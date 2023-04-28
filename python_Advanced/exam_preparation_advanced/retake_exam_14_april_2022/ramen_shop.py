from collections import deque
bowls = list(map(int, input().split(", ")))
customers = deque(list(map(int, input().split(", "))))
while bowls and customers:
    bowl = bowls[-1]  # bowls.pop()
    customer = customers[0]  # customers.popleft()
    if bowl == customer:
        bowls.pop()
        customers.popleft()
        continue
    elif bowl > customer:
        bowl -= customer
        customers.popleft()
        bowls.pop()
        bowls.append(bowl)
    elif bowl < customer:
        customer -= bowl
        bowls.pop()
        customers.popleft()
        customers.appendleft(customer)
if not customers:
    print("Great job! You served all the customers.")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
if bowls:
    print(f"Bowls of ramen left: {', '.join(str(b) for b in bowls)}")
if customers:
    print(f"Customers left: {', '.join(str(c) for c in customers)}")


