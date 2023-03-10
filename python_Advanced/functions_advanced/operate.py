def operate(*args):
    operator, numbers = args[0], args[1:]
    result = None

    if operator == "+":
        result = sum([digit for digit in args[1:]])

        return result
    elif operator == "-":
        first_num = args[1]
        for num in args[2:]:
            first_num -= num
            result = first_num
        return result
    elif operator == "*":
        first_num = 1
        for num in args[1:]:
            first_num *= num
            result = first_num
        return result
    elif operator == "/":
        first_num = args[1]
        for num in args[2:]:
            first_num /= num
            result = first_num
        return result



print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))