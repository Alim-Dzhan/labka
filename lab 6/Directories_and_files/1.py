
import os

def list_files_and_dirs(path):
    all_items = os.listdir(path)
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]
    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    return directories, files, all_items

path = "."  
dirs, files, all_items = list_files_and_dirs(path)
print(f"Directories: {dirs}")
print(f"Files: {files}")
print(f"All items: {all_items}")
"""
import os
from string import ascii_uppercase
location1 = r'/Users\dzhan\OneDrive\Рабочий стол\VS\python\lab 6'
print([name for name in os.listdir(location1)]) 
print([name for name in os.listdir(location1) if os.path.isdir(os.path.join(location1, name))]) 
print([name for name in os.listdir(location1) if not os.path.isdir(os.path.join(location1, name))]) 
"""