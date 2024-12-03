import os

working_directory = os.getcwd()
folder_name = 'texts'
relative_folder_path = os.path.join(working_directory, folder_name)
files = os.listdir(relative_folder_path)
files.sort()

for idx, file_name in enumerate(files, start=1):
    with open(os.path.join(relative_folder_path, file_name), 'r', encoding='utf-8') as file:
        print(file_name)
        lines = sum(1 for _ in file)
        print(lines)
        with open(os.path.join(relative_folder_path, file_name), 'r', encoding='utf-8') as f:
            for line in f:
                print(line.strip())
            print()

files.sort(key=lambda x: sum(1 for _ in open(os.path.join(relative_folder_path, x), encoding='utf-8')))
final_file_path = os.path.join(relative_folder_path, 'final_file.txt')

with open(final_file_path, 'w', encoding='utf-8') as final_file:
    for file_name in files:
        with open(os.path.join(relative_folder_path, file_name), 'r', encoding='utf-8') as file:
            final_file.write(file.read())

print('\nОбщий файл:')
with open(final_file_path, 'r', encoding='utf-8') as final_file:
    for line in final_file:
        print(line.strip())