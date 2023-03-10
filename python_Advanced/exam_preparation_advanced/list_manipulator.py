def list_manipulator(numbers, command, position, *args):

    if command == "add" and position == "beginning":
        numbers = list(args) + numbers

    if command == "add" and position == "end":
        numbers = numbers + list(args)

    if command == "remove" and position == "end":
        if args:
            for num in range(args[-1]):
                numbers.pop()
        if not args:
            numbers.pop()
    if command == "remove" and position == "beginning":
        if args:
            for num in range(args[-1]):
                numbers.pop(0)
        if not args:
            numbers.pop(0)

    return numbers



print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))