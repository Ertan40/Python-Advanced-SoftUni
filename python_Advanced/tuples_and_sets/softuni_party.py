number_of_guests = int(input())
guest_list = set()
arrived_quests = set()

for i in range(number_of_guests):
    guest_list.add(input())

arrival = input()
while arrival != "END":
    arrived_quests.add(arrival)
    arrival = input()
# print(guest_list)  # {'SVQXQCbc ', 'Ce8vwPmE ', '9NoBUajQ ', 'tSzE5t0p ', '7IK9Yo0h '}
# print(arrived_quests) # {'9NoBUajQ ', 'Ce8vwPmE ', 'SVQXQCbc '}
not_arrived = sorted(guest_list.difference(arrived_quests))
print(len(not_arrived))
for code in not_arrived:
    print(code)