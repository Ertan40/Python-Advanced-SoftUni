from collections import deque
materials = deque(int(b) for b in input().split()) # materials[-1]
magic_values = deque((int(b) for b in input().split())) # magic_values[0]
crafted = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}
while materials and magic_values:
    material = materials.pop() if magic_values[0] or not materials[0] else 0
    magic_value = magic_values.popleft() if material or not magic_values[0] else 0
    if not magic_value:
        continue
    # if materials[-1] == 0 or magic_values[0] == 0:
    #     if materials[-1] == 0:
    #         materials.pop()
    #     if magic_values[0] == 0:
    #         magic_values.popleft()
    #     continue
    product = magic_value * material
    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        materials.append(material + magic_value)
    elif product > 0:
        materials.append(material + 15)
if {"Doll", "Woody train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(m) for m in materials][::-1])}")
if magic_values:
    print(f"Magic left: {', '.join(str(m) for m in magic_values)}")
for toy in sorted(set(crafted)):
    print(f"{toy}: {crafted.count(toy)}")
# [print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]
