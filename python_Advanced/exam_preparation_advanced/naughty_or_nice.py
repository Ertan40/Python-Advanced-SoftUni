def naughty_or_nice_list(*args, **kwargs):
 # (([(3, 'Amy'), (1, 'Tom'), (7, 'George'), (3, 'Katy')], '3-Nice', '1-Naughty'), {'Amy': 'Nice', 'Katy': 'Naughty'})
    kids = {"Nice": [], "Naughty": [], "Not_found": []}
    santa_list = args[0] # [[(3, 'Amy'), (1, 'Tom'), (7, 'George'), (3, 'Katy')]]
    for i in range(1, len(args)):
        number, name = args[i].split("-")
        number = int(number)
        counter = 0
        for kid_n, kid_number in santa_list:
            if kid_n == number:
                counter += 1
        if counter == 1:
            for index, kid in enumerate(santa_list):
                if kid[0] == number:
                    kids[name].append(kid[1])
                    santa_list.pop(index)
# {'Amy': 'Nice', 'Katy': 'Naughty'}
    for name, value in kwargs.items():
        count = 0
        for kid_n, kid_name in santa_list:
            if name == kid_name:
                count += 1
        if count == 1:
            for index, kid in enumerate(santa_list):
                if name == kid[1]:
                    kids[value].append(name)
                    santa_list.pop(index)
    for _, name in santa_list:
        kids["Not_found"].append(name)
    output = ""
    for type_of_kid, names in kids.items():
        if names:
            output += f"{type_of_kid}: {', '.join(names)}\n"

    return output


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))


# def naughty_or_nice_list(santa_list, *args, **kwargs):
#  # (([(3, 'Amy'), (1, 'Tom'), (7, 'George'), (3, 'Katy')], '3-Nice', '1-Naughty'), {'Amy': 'Nice', 'Katy': 'Naughty'})
#     nice_kids, naughty_kids = [], []
#     result = []
#     for data in args:
#         number, type_of_kid = data.split("-")
#         kids = []
#         for info in santa_list:
#             if info[0] == int(number):
#                 kids.append(info)
#                 if len(kids) == 1:
#                     if type_of_kid == "Nice":
#                         nice_kids.extend(kids)
#                     else:
#                         naughty_kids.extend(kids)
#                     santa_list.remove(*kids)
#     other_kids = []
#     for name, type_of_kid in kwargs.items():
#         for info in santa_list:
#             if info[1] == name:
#                 other_kids.append(info)
#                 if len(other_kids) == 1:
#                     if type_of_kid == "Nice":
#                         nice_kids.extend(other_kids)
#                     else:
#                         naughty_kids.extend(other_kids)
#                     santa_list.remove(*other_kids)
#     if nice_kids:
#         result.append(f"Nice: {', '.join([k[1] for k in nice_kids])}")
#     if naughty_kids:
#         result.append(f"Naughty: {', '.join([k[1] for k in naughty_kids])}")
#     if santa_list:
#         result.append(f"Not found: {', '.join([k[1] for k in santa_list])}")
#     return "\n".join(result)