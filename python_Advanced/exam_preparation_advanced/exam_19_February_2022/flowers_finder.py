from collections import deque
vowels = deque(list(map(str, input().split())))  # vowels.popleft()  vowels[0]
consonants = list(map(str, input().split()))     # consonants.pop()  consonants[-1]
flowers = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
is_found = False

while vowels and consonants and not is_found:

    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    for key, flower in flowers.items():
        if current_vowel in flower:
            flowers[key] = flowers[key].replace(current_vowel, "")
        if current_consonant in flower:
            flowers[key] = flowers[key].replace(current_consonant, "")
        if not flowers[key]:
            word_found = key
            is_found = True
            break
if is_found:
    print(f"Word found: {''.join(word_found)}")
else:
    print(f"Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")





