def forecast(*args):  # (('Sofia', 'Sunny'), ('London', 'Cloudy'), ('New York', 'Sunny'))
    locations = {
               "Sunny": [],
               "Cloudy": [],
               "Rainy": [],
               }
    for city, weather in sorted(args):
        locations[weather].append(city)

    result = []
    for key in locations:
        for value in locations[key]:
            result.append(f"{value} - {key}")
    return "\n".join(result)

# output:
# New York - Sunny
# Sofia - Sunny
# London - Cloudy
# my_dict = dict((x, y) for x, y in sorted(args))
# {'London': 'Cloudy', 'New York': 'Sunny', 'Sofia': 'Sunny'}


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))