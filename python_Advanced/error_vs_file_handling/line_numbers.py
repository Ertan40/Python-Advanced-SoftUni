import os
from pathlib import Path


def file_reader(full_path):
    try:
        with open(full_path, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            return "".join(lines)

    except FileNotFoundError:
        print('File not found')


def line_numbers(folder, file):
    file_path = folder + file

    lines = [line for line in file_reader(file_path).split("\n")]

    line_numbers = []
    for l in lines:
        letters = [letter for letter in l if letter.isalpha()]
        punctuation = [p for p in l if p.isascii and p not in letters and p.isspace() is False]
        # print(punctuation)

        new_line = f'Line: {lines.index(l) + 1} {l} ({len(letters)})({len(punctuation)})'
        line_numbers.append(new_line)

    return line_numbers


def add_to_new_file(folder, file):
    # check if file already exists and remove it if it does
    path_to_files = Path(folder)
    files_in_folder = path_to_files.iterdir()

    for item in files_in_folder:
        if item.name == file:
            os.remove(item)
            print('File deleted')

    # create new file and append the results
    full_path = folder + file
    with open(full_path, 'a', encoding="utf-8") as f:
        for l in line_numbers('C:/Users/hp/Desktop/', 'compare_text.txt'):
            text = l + '\n'
            f.write(text)

    return full_path


if __name__ == '__main__':
    line_numbers('C:/Users/hp/Desktop/', 'compare_text.txt')

    print(add_to_new_file('C:/Users/hp/Desktop/', 'mylines.txt'))
    print(file_reader('C:/Users/hp/Desktop/mylines.txt'))