from collections import deque
energies = deque(int(e) for e in input().split())
materials = list(map(int, input().split()))
total_used_energy = 0
created_toys = 0
counter = 0
while energies and materials:
    energy = energies.popleft()
    if energy < 5:
        continue
    material = materials.pop()
    counter += 1
    if counter % 15 == 0:
        if energy >= material * 2:
            created_toys += 1
            energies.append(energy - material * 2)
            total_used_energy += material * 2
        else:
            energies.append(energy * 2)
            materials.append(material)
    elif counter % 3 == 0:
        if energy >= material * 2:
            created_toys += 2
            energy -= material * 2
            energies.append(energy + 1)
            total_used_energy += material * 2
        else:
            energy *= 2
            energies.append(energy)
            materials.append(material)
    elif counter % 5 == 0:
        if energy >= material:
            energy -= material
            energies.append(energy)
            total_used_energy += material
        else:
            energy *= 2
            energies.append(energy)
            materials.append(material)
    elif energy >= material:
        created_toys += 1
        energy -= material
        energy += 1
        energies.append(energy)
        total_used_energy += material
    else:
        energies.append(energy * 2)
        materials.append(material)
print(f"Toys: {created_toys}")
print(f"Energy: {total_used_energy}")
if energies:
    print(f"Elves left: {', '.join(str(e) for e in energies)}")
if materials:
    print(f"Boxes left: {', '.join(str(m) for m in materials)}")