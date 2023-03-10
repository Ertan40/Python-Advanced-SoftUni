def shop_from_grocery_list(budget, grocery_list, *args):

    for product, price in args:
        if budget - price >= 0 and product in grocery_list:
            budget -= price
            grocery_list.remove(product)
        elif budget - price < 0 and product in grocery_list:
            break
    # (('cola', 5.8), ('tomato', 10.0), ('tomato', 20.45))    args
    # (('cola', 5.8), ('tomato', 10.0), ('meat', 22))
    # (('cola', 15.8), ('chocolate', 30), ('tomato', 15.85), ('chips', 50), ('meat', 22.99))
    result = []
    if not grocery_list:
        result.append(f'Shopping is successful. Remaining budget: {budget:.2f}.')
    else:
        result.append(f'You did not buy all the products. Missing products: {", ".join(grocery_list)}.')

    return "\n".join(result)


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))


