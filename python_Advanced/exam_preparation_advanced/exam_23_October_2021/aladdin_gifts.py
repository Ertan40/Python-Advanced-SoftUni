from collections import deque

materials = list(map(int, input().split()))  # materials.pop() materials[-1]
magic_levels = deque(list(map(int, input().split())))  # magic_levels.popleft()   magic_levels[0]
crafted = []
presents = {"Gemstone": [100, 199],
            "Porcelain Sculpture": [200, 299],
            "Gold": [300, 399],
            "Diamond Jewellery": [400, 499],
            }
while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()
    gift = material + magic

    if gift < 100:
        if gift % 2 == 0:
            material *= 2
            magic *= 3
            gift = material + magic
        elif gift % 2 != 0:
            gift *= 2
    elif gift > 499:
         gift /= 2

    if presents["Gemstone"][0] <= gift <= presents["Gemstone"][1]:
        crafted.append("Gemstone")
    elif presents["Porcelain Sculpture"][0] <= gift <= presents["Porcelain Sculpture"][1]:
        crafted.append("Porcelain Sculpture")
    elif presents["Gold"][0] <= gift <= presents["Gold"][1]:
        crafted.append("Gold")
    elif presents['Diamond Jewellery'][0] <= gift <= presents["Diamond Jewellery"][1]:
        crafted.append("Diamond Jewellery")

if ("Gemstone" in crafted and "Porcelain Sculpture" in crafted) \
     or ("Gold" in crafted and "Diamond Jewellery" in crafted):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(m) for m in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(m) for m in magic_levels)}")
for toy in sorted(set(crafted)):
    print(f"{toy}: {crafted.count(toy)}")