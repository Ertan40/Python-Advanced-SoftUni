from collections import deque
queue = deque()
starting_quantity = int(input())

while True:
    name = input()
    if name == "Start":
        break
    queue.append(name)
while True:
    command = input()
    if command == "End":
        break
    command_args = command.split() # refill {Liters}
    if len(command_args) == 2:
        starting_quantity += int(command_args[1])
    # {Liters}
    else:   # liters = int(command_args[0]  # person = queue.popleft()
        if int(command_args[0]) > starting_quantity:
            print(f"{queue.popleft()} must wait")
        else:
            print(f"{queue.popleft()} got water")
            starting_quantity -= int(command_args[0])
print(f"{starting_quantity} liters left")