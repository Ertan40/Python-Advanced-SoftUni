def plant_garden(available_space, *args, **kwargs):
    allowed_plants = {}  # {'rose': 2.5, 'tulip': 1.2, 'sunflower': 3.0} allowed_type: space
    plant_requests = {}  # {'rose': 10, 'tulip': 20}   plant_type: quantity
    planted_plants = {}

    # Populate allowed plants from args
    for data in args:
        plant_name, space = data
        allowed_plants[plant_name] = float(space)

    # Populate plant requests from kwargs
    for plant_type, quantity in kwargs.items():
        plant_requests[plant_type] = int(quantity)

    # Sort requests alphabetically
    sorted_plant_requests = dict(sorted(plant_requests.items()))

    # Process each plant request
    for plant, quantity in sorted_plant_requests.items():
        if plant not in allowed_plants:
            continue  # Skip if plant not allowed
        space_per = allowed_plants[plant]
        max_possible = int(available_space // space_per)
        planted = min(quantity, max_possible)
        if planted > 0:
            planted_plants[plant] = planted
            available_space -= planted * space_per

        if available_space <= 0.0:
            break

    # Prepare output
    output = []
    all_planted = all(kwargs[plant] <= planted_plants.get(plant, 0) for plant in sorted_plant_requests if plant in allowed_plants)
    
    if all_planted:
        output.append(f"All plants were planted! Available garden space: {available_space:.1f} sq meters.")
    else:
        output.append("Not enough space to plant all requested plants!")

    output.append("Planted plants:")
    for plant, quantity in planted_plants.items():
        output.append(f"{plant}: {quantity}")

    return '\n'.join(output)


print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))


# Sort by values   # plants = {'rose': 10, 'tulip': 20}
# sorted_plants = dict(sorted(plants.items(), key=lambda x: x[1]))
# Sort by keys alphabetically (ascending)   {'rose': 10, 'tulip': 20}
# sorted_plants_by_keys_ascending = dict(sorted(plants.items()))
# Sort by keys alphabetically (descending)  {'tulip': 20, 'rose': 10}
# sorted_plants_by_keys_descending = dict(sorted(plants.items(), reverse=True))