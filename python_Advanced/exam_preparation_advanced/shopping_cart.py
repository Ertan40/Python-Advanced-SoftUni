def shopping_cart(*args):

    limit = {"Soup": 3,
             "Pizza": 4,
             "Dessert": 2,
             }
    my_meal = {
        "Soup": [],
        "Pizza": [],
        "Dessert": [],
    }
    for command in args:
        if command == "Stop":
            break
        else:
            meal = command[0]
            product = command[1]
            if len(my_meal[meal]) < limit[meal] and product not in my_meal[meal]:
                my_meal[meal].append(product)
    output = ""
    for meal, products in sorted(my_meal.items(), key=lambda x: (-len(x[1]), x[0])):
        output += f"{meal}:\n"
        for product in sorted(products):
            output += " " + f"- {product}\n"

    if len(my_meal["Pizza"]) == 0 and len(my_meal["Soup"]) == 0 and len(my_meal["Dessert"]) == 0:
        output = "No products in the cart!"
    return output


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))