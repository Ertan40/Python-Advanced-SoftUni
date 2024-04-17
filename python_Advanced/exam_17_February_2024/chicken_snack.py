from collections import deque


amount_of_money = [int(a) for a in input().split()]   # [9, 5, 8, 18]
prices_of_food = deque(list(map(int, input().split())))   # deque([18, 12, 10, 5])
food_count = 0

while amount_of_money and prices_of_food:
    money = amount_of_money[-1]
    price = prices_of_food[0]
    if money == price:
        amount_of_money.pop()
        prices_of_food.popleft()
        food_count += 1
    elif money > price:
        curr_money = amount_of_money.pop()
        diff = curr_money - price
        if amount_of_money:
            amount_of_money[-1] += diff
            prices_of_food.popleft()
        food_count += 1
    else:
        amount_of_money.pop()
        prices_of_food.popleft()

if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif 1 < food_count < 4:
    print(f"Henry ate: {food_count} foods.")

elif food_count == 1:
    print(f"Henry ate: {food_count} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")