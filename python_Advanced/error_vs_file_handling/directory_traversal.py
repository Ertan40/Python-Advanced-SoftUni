import os
from pathlib import Path

def list_contents(folder):
    path_to_files = Path(folder)
    files_in_folder = [f for f in path_to_files.iterdir() if f.is_file()]

    contents = {f.name.split('.')[-1]: f.name for f in files_in_folder}
    ascending = dict(sorted(contents.items(), key=lambda c: c[0]))

    print(contents)
    return ascending

def generate_audit_file(file_name):
    #desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    #desktop = os.path.normpath(os.path.expanduser("~/Desktop"))   # windows and linux
    desktop = Path.home() / 'Desktop'

    full_path = str(desktop) + '/' + file_name
    print(full_path)

    with open(full_path, 'w', encoding='utf-8') as fr:
        for file_extension, file in list_contents(desktop).items():
            extension = f'.{file_extension}'
            files = f'---{file}'

            output = extension + '\n' + files + '\n'
            fr.write(output)

if __name__ == '__main__':
    generate_audit_file('report.txt')