def even_odd_filter(**kwargs):

    data = kwargs # {'odd': [1, 2, 3, 4, 10, 5], 'even': [3, 4, 5, 7, 10, 2, 5, 5, 2]}
    filtered = {}
    for command in data:
        filtered[command] = filtered.get(command, [])  # {'odd': [], 'even': []}
        if command == "even":
            filtered[command] = [digit for digit in data[command] if digit % 2 == 0]
        elif command == "odd":
            filtered[command] = [digit for digit in data[command] if digit % 2 != 0]
            
    sorted_data = {}
    for operation, values in (sorted(filtered.items(), key=lambda x: -len(x[1]))):
        sorted_data[operation] = values
    return sorted_data
    # new_data = {item: value for (item, value) in data.items()}

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))