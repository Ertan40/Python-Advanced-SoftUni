def math_operations(*args, **kwargs):
    # ((2.1, 12.56, 0.0, -3.899, 6.0, -20.65), {'a': 1, 's': 7, 'd': 33, 'm': 15})
    for num in range(len(args)):
        key = list(kwargs.keys())[num % 4] # a s d m
        if key == "a":
            kwargs[key] += args[num]
        elif key == "s":
            kwargs[key] -= args[num]
        elif key == "m":
            kwargs[key] *= args[num]
        elif key == "d":
            if args[num] != 0:
                kwargs[key] /= args[num]
    result = []
    for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
        result.append(f"{key}: {value:.1f}")

    return "\n".join(result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))