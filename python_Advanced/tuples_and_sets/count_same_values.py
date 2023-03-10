numbers = tuple(map(float, input().split())) # (-2.5, 4.0, 3.0, -2.5, -5.5, 4.0, 3.0, 3.0, -2.5, 3.0)
unique = []
my_dict = {}
for num in numbers:
    if num not in unique:
        unique.append(num) # [-2.5, 4.0, 3.0, -5.5]

for number in unique:
    number_count = numbers.count(number)
    my_dict[number] = str(f"{number_count} times")

for key, value in my_dict.items():
    print(f"{key} - {value}")

###############    second way   #########################
# numbers = tuple(map(float, input().split()))
# unique = []
# for num in numbers:
#     if num not in unique:
#         unique.append(num) # [-2.5, 4.0, 3.0, -5.5]
# for number in unique:
#     print(f"{number} - {numbers.count(number)} times")