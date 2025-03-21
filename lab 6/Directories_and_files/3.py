import os


path = input()

if os.path.exists(path):
    print(f"Путь '{path}' существует.")

    dir_name = os.path.dirname(path)

    file_name = os.path.basename(path)

    print(f"Имя каталога: {dir_name}")
    print(f"Имя файла: {file_name}")
else:
    print(f"Путь '{path}' не существует.")





