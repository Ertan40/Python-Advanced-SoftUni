text = tuple(input()) # ('S', 'o', 'f', 't', 'U', 'n', 'i', ' ', 'r', 'o', 'c', 'k', 's')

unique_text = sorted(set(text))

for ch in unique_text:
    print(f"{ch}: {text.count(ch)} time/s")