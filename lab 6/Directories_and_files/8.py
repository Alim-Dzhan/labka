import os


file_path = input("Введите путь к файлу для удаления: ")

path_exists = os.access(file_path, os.F_OK)

if not path_exists:
    print('Путь не существует')
else:
    os.remove(file_path)
    print("Файл успешно удалён")


"""
import os
from string import ascii_uppercase


path = r'/Users\dzhan\OneDrive\Рабочий стол\VS\python\lab 6\Directories_and_files/file.txt'
path_bool = os.access(path, os.F_OK)
if path_bool == False:
    print('Path does not exist')
elif path_bool == True:
    os.remove(path)
    print("File has been removed")
    """

