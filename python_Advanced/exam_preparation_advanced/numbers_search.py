def numbers_searching(*args):
    # (1, 2, 4, 2, 5, 4)
    numbers = list(args)
    unique_list = []
    duplicate_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
        elif num not in duplicate_list:
            duplicate_list.append(num)
    missing_numbers = []
    for num in range(min(numbers), max(numbers)):
        if num not in numbers:
            missing_numbers.append(num)
    missing_numbers.append(sorted(duplicate_list))

    return missing_numbers

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))