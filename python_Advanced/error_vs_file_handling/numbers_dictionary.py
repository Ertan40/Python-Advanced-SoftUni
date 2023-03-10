numbers_dictionary = {}
line = input()

try:
    while line != "Search":
        number = int(input())
        numbers_dictionary[line] = number
        line = input()

    else:
        while line != "Remove":
            searched = input()
            if searched in numbers_dictionary.keys():
                print(numbers_dictionary[searched])
            else:
                print(f' Number {searched} does not exist in dictionary')
            line = input()

        else:
            while line != "End":
                searched = input()
                if searched in numbers_dictionary.keys():
                    del numbers_dictionary[searched]
                else:
                    print(f' Number {searched} does not exist in dictionary')
                line = input()

            print(numbers_dictionary)

except ValueError:
    print('The variable number must be an integer')
    print(numbers_dictionary)