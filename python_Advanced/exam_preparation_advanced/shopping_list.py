def shopping_list(budget, **kwargs): # (100, {'microwave': (70, 2), 'skirts': (15, 4), 'coffee': (1.5, 10)})

    my_dict = {}
    for product, items in kwargs.items():
        if items not in my_dict:
            my_dict[product] = []
        my_dict[product] = [float(items[0]), items[1]]
    # {'microwave': [70.0, 2], 'skirts': [15.0, 4], 'coffee': [1.5, 10]}
    basket = {}
    if budget >= 100:
        for product, items in my_dict.items():
            if product not in basket and len(basket) < 5:
                basket[product] = 0
                if items[0] * items[1] <= budget:
                    basket[product] += items[0] * items[1]
                    budget -= items[0] * items[1]
        output = []
        for product, price in basket.items():
            if price > 0:
                output.append(f"You bought {product} for {price:.2f} leva.")

        return "\n".join(output)

    if budget < 100:
         return "You do not have enough budget."


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

# --------------------------- second-way ----------------------

# def shopping_list(budget, **kwargs):
#     # {'microwave': (70, 2), 'skirts': (15, 4), 'coffee': (1.5, 10)}
#     bought_products = []
#     if budget < 100:
#         return "You do not have enough budget."
#     for product, (price, quantity) in kwargs.items():
#         total_price = float(price) * int(quantity)
#         if len(bought_products) < 5 and total_price <= budget:
#             budget -= total_price
#             bought_products.append(f"You bought {product} for {total_price:.2f} leva.")
#
#     return "\n".join(bought_products)
#
# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))
#
# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))
#
# print(shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     ))