from collections import deque

textiles = deque(int(x) for x in input().split(" "))
medicaments = [int(x) for x in input().split(" ")]
items = {"Patch": 0, "Bandage": 0, "MedKit": 0}
healing_item = {30: "Patch", 40: "Bandage", 100: "MedKit"}

while medicaments and textiles:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    item = medicament + textile
    if item in healing_item:
        new_item = healing_item[item]
        items[new_item] += 1
    elif item > 100:
        items["MedKit"] += 1
        remained = (item - 100)
        medicaments[-1] += remained
    else:
        medicaments.append(medicament + 10)


if not textiles and medicaments:
    print("Textiles are empty.")
if not medicaments and textiles:
    print("Medicaments are empty.")

if not textiles and not medicaments:
    print(f"Textiles and medicaments are both empty.")

for key, value in sorted(items.items(), key=lambda x: (-x[1], x[0])):
    if value > 0:
        print(f"{key} - {(value)}")

if textiles:
    print(f"Textiles left: {', '.join(str(m) for m in textiles)}")
if medicaments:
    print(f"Medicaments left: {', '.join(str(m) for m in medicaments[::-1])}")



# textiles = [int(x) for x in input().split()]
# medicaments = [int(x) for x in input().split()]
#
# healing_items = {
#     30: 'Patch',
#     40: 'Bandage',
#     100: 'MedKit'
# }
#
# items = {
#     'Patch': 0,
#     'Bandage': 0,
#     'MedKit': 0
# }
# while textiles and medicaments:
#     textile = textiles.pop(0)
#     medicament = medicaments.pop()
#     item = textile + medicament
#     if item in healing_items:
#         new_item = healing_items[item]
#         items[new_item] += 1
#     elif item > 100:
#         items['MedKit'] += 1
#         remainig = item - 100
#         medicaments[-1] += remainig
#     else:
#         medicament += 10
#         medicaments.append(medicament)
#
# if not textiles and not medicaments:
#     print('Textiles and medicaments are both empty.')
# else:
#     print('Textiles are empty.') if not textiles else print('Medicaments are empty.')
#
# sorted_items = sorted(items.items(), key=lambda x: (-x[1], x[0]))
# for name, values in sorted_items:
#     if values > 0:
#         print(f'{name} - {values}')
#
# if medicaments:
#     print(f'Medicaments left: {", ".join(str(x) for x in medicaments[::-1])}')
# if textiles:
#     print(f'Textiles left: {", ".join(str(x) for x in textiles)}')





# if materials:
#     print(f"Materials left: {', '.join(str(m) for m in materials)}")
# if magic_levels:
#     print(f"Magic left: {', '.join(str(m) for m in magic_levels)}")
# for toy in sorted(set(crafted)):
#     print(f"{toy}: {crafted.count(toy)}")