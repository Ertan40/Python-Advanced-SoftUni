import re
from collections import deque


def file_reader(full_path):
    try:
        with open(full_path, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            return "".join(lines)

    except FileNotFoundError:
        print('File not found')


def even_lines(folder, file):
    file_path = folder + file
    special_chars = r"[.|,|-]|]|[?|!]"

    lines = [re.sub(special_chars, '@', line) for line in file_reader(file_path).split("\n")]
    # print(lines)

    even = deque([e.split() for e in lines if lines.index(e) % 2 == 0])
    # print(even)

    reversed = []
    while even:
        r = even.popleft()[::-1]
        reversed.append(r)

    result = [" ".join(s) for s in reversed]
    return result


for nl in even_lines('C:/Users/hp/Desktop/', 'compare_text.txt'):
    print(nl)