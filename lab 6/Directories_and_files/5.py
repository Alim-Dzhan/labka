
my_list = ["apple", "banana", "cherry", "date", "elderberry"]

with open("my_list.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")  

print("Список успешно записан в файл 'my_list.txt'.")



"""
import os
from string import ascii_uppercase

mylist = ['A', 'B', 'C', 'D']
with open(r'/Users\dzhan\OneDrive\Рабочий стол\VS\python\lab 6\Directories_and_files/file2.txt', 'w') as file:
    for i in mylist:
        file.write(i + '\n')
file.close()
"""

