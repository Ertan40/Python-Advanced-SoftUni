def age_assignment(*args, **kwargs):

    result = []
    for name, age in kwargs.items():
        for curr_name in args:
            if curr_name.startswith(name):
                name = curr_name
                result.append(f"{name} is {age} years old.")

    return "\n".join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
