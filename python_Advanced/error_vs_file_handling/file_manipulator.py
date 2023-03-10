while command != 'End':
    command = command.split('-')

    action = command[0]
    file_name = command[1]
    full_path = os.getcwd() + '/' + file_name

    if action == 'Create':
        create_file('file.txt')
        print(f'Created {file_name}')

    elif action == 'Add':
        content = command[2] + '\n'

        with open(full_path, 'a', encoding="utf-8") as f:
            f.write(content)
        print(f'Added {content} to {file_name}')

    elif action == 'Replace':
        old_string = command[2]
        new_string = command[3]

        try:
            with open(full_path, 'r', encoding="utf-8") as f:
                lines = f.readlines()

            for l in lines:
                if old_string in l:
                    with open(full_path, 'a', encoding="utf-8") as fwr:
                        l = l.replace(old_string, new_string)
                        fwr.write(l)
                        print(l)

        except FileNotFoundError:
            print('An error occured')


    elif action == 'Delete':
        delete_files(file_name)

    command = input()