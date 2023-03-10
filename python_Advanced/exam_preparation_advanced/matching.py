males = [int(x) for x in input().split()]
females = [int(x) for x in input().split()]
matches = 0
while males and females:
    if females[0] <= 0:
        females.pop(0)
        continue
    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] % 25 == 0:
        females.pop(0)
        if females:
            females.pop(0)
        continue
    if males[-1] % 25 == 0:
        males.pop()
        if males:
            males.pop()
        continue
    first_female = females.pop(0)
    last_male = males.pop()
    if first_female == last_male:
        matches += 1
    else:
        males.append(last_male - 2)
print(f'Matches: {matches}')
if males:
    print(f'Males left: {", ".join(str(x) for x in males[::-1])}')
else:
    print(f'Males left: none')
if females:
    print(f'Females left: {", ".join(str(x) for x in females)}')
else:
    print(f'Females left: none')