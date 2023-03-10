def start_spring(**kwargs):
    new_dict = {}
    for object, type in kwargs.items():
        if type not in new_dict:
            new_dict[type] = []
        new_dict[type].append(object)
    # for value, key in kwargs.items():
    #     new_dict[key] = new_dict.get(key, []) + [value]
    # {'flower': ['Water Lilly', 'Dahlia', 'Tulip'], 'bird': ['Swifts', 'Swallows'], 'tree': ['Callery Pear']}
    output = ""
    for type, object in sorted(new_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        output += f"{type}:\n"
        for items in sorted(object):
            output += f"-{items}\n"
    return output


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))