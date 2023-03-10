from collections import deque
people = deque()

while True:
    name = input()
    if name == "End":
        break
    if name == "Paid":
        print("\n".join(people))
        people.clear()
    else:
        people.append(name)
print(f"{len(people)} people remaining.")
