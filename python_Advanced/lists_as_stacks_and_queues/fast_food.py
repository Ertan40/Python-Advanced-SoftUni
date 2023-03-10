quantity_of_food = int(input())
each_order = input().split()
each_order_to_int = [int(i) for i in each_order]
completed_orders = []

if quantity_of_food >= sum(each_order_to_int):
    print(max(each_order_to_int))
    print("Orders complete")
else:
    for num in each_order:
        quantity_of_food -= int(num)
        completed_orders.append(num)
        if quantity_of_food < int(num):
            break
    orders_left = [i for i in each_order if i not in completed_orders]
    print(max(each_order_to_int))
    print(f"Orders left: {' '.join(orders_left)}")



