first_numbers = set(map(int, input().split()))  # [1, 2, 3, 4, 5]
second_numbers = set(map(int, input().split()))  # [1, 2, 3]
lines = int(input())

for c in range(lines):
    command = input().split() # ['Add', 'First', '5', '6']
    if command[0] == "Add":
        if command[1] == "First":
            for num in range(len(command) - 2):
                first_numbers.add(int(command.pop())) # {1, 2, 3, 4, 5, 6}

        elif command[1] == "Second":
            for num in range(len(command) - 2):
                second_numbers.add(int(command.pop()))
    elif command[0] == "Remove":
        if command[1] == "First":
            numbers_to_be_removed = set()
            for num in range(len(command) - 2):
                numbers_to_be_removed.add(int(command.pop()))
            first_numbers = first_numbers.difference(numbers_to_be_removed)

        elif command[1] == "Second":
            numbers_to_be_removed = set()
            for num in range(len(command) - 2):
                numbers_to_be_removed.add(int(command.pop()))
            second_numbers = second_numbers.difference(numbers_to_be_removed)

    elif command[0] == "Check":
        diff = second_numbers.issubset(first_numbers)
        if diff:
            print("True")
        else:
            print("False")

sorted_first_numbers = sorted(first_numbers)
sorted_second_numbers = sorted(second_numbers)

print(*sorted_first_numbers, sep=", ")
print(*sorted_second_numbers, sep=", ")

#################### second_way: not my solution ####################################

# first_sequence = set(int(number) for number in input().split())
# second_sequence = set(int(number) for number in input().split())
# number_of_commands = int(input())
#
# for _ in range(number_of_commands):
#     data = [int(item) if item.isdigit() else item for item in input().split()]
#     command = data[0] + data[1]
#
#     if command == 'AddFirst':
#         [first_sequence.add(digit) for digit in data[2::]]
#     elif command == 'AddSecond':
#         [second_sequence.add(digit) for digit in data[2::]]
#     elif command == 'RemoveFirst':
#         [first_sequence.discard(number) for number in data[2::]]
#     elif command == 'RemoveSecond':
#         [second_sequence.discard(number) for number in data[2::]]
#     elif command == 'CheckSubset':
#         if second_sequence.issubset(first_sequence):
#             print(True)
#         elif not second_sequence.issubset(first_sequence):
#             print(False)
#
# sorted_first_sequence = sorted(first_sequence)
# sorted_second_sequence = sorted(second_sequence)
#
# print(*sorted_first_sequence, sep=', ')
# print(*sorted_second_sequence, sep=', ')

############################################################
# first = set(int(i) for i in input().split())
# second = set(int(i) for i in input().split())
#
# functions = {
#     "Add First": lambda x: [first.add(el) for el in x],
#     "Add Second": lambda x: [second.add(el) for el in x],
#     "Remove First": lambda x: [first.discard(el) for el in x],
#     "Remove Second": lambda x: [second.discard(el) for el in x],
#     "Check Subset": lambda: print(True) if first.issubset(second) or second.issubset(first) else print(False)
# }
#
# for _ in range(int(input())):
#
#     first_command, *data = input().split()
#     command = first_command + " " + data.pop(0)
#     if data:
#         functions[command]([int(x) for x in data])
#     else:
#         functions[command]()
#
# print(*sorted(first), sep=", ")
# print(*sorted(second), sep=", ")