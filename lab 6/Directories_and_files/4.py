file_path = input()

try:
    with open(file_path, 'r') as file:
      
        line_count = sum(1 for line in file)
    print(f"Количество строк в файле '{file_path}': {line_count}")
except FileNotFoundError:
    print(f"Ошибка: Файл '{file_path}' не найден.")

"""
import os
from string import ascii_uppercase

with open(r'/Users\dzhan\OneDrive\Рабочий стол\VS\python\lab 6\Directories_and_files/file2.txt', 'r') as file:
    x = len(file.readlines())
    print("Number of lines:", x)

"""


