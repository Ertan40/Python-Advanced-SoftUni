def words_sorting(*args):
    # ('escape', 'charm', 'mythology')
    my_dict = {}
    as_list = list(args)
    for word in as_list:
        value = 0
        for w in word:
            value += ord(w)
        if word not in my_dict:
            my_dict[word] = value  # {'escape': 625, 'charm': 523, 'mythology': 1004}
    total_value = 0
    for key, value in my_dict.items():
        total_value += value
        output = ""
        if total_value % 2 == 0:
            for key1, value1 in sorted(my_dict.items(), key=lambda x: x[0]):
                output += f"{key1} - {value1}\n"

        elif total_value % 2 != 0:
            for key2, value2 in sorted(my_dict.items(), key=lambda x: -x[1]):
                output += f"{key2} - {value2}\n"

    return output




print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))