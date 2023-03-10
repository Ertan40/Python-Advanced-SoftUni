def concatenate(*args, **kwargs):

    result = ""
    for word in args:  # or result = ''.join(args)
        result += word  # SoftUNIIsGrate!

    for key, value in kwargs.items():
        if key in result:
            result = result.replace(key, value)

    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))