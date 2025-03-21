import os

def check_path_access(path):
    return {
        "Exists": os.path.exists(path),
        "Readable": os.access(path, os.R_OK),
        "Writable": os.access(path, os.W_OK),
        "Executable": os.access(path, os.X_OK)
    }

path = "."  
access_info = check_path_access(path)
for key, value in access_info.items():
    print(f"{key}: {value}")

"""
import os
from string import ascii_uppercase
    print('Path exists:', os.access(r'/Users\dzhan\OneDrive\Рабочий стол\VS\python\lab 6', os.F_OK))
print('Path readable:', os.access(r'/Users\dzhan\OneDrive\Рабочий стол\VS\python\lab 6', os.R_OK))
print('Path writable:', os.access(r'/Users\dzhan\OneDrive\Рабочий стол\VS\python\lab 6', os.W_OK))
print('Path executable:', os.access(r'/Users\dzhan\OneDrive\Рабочий стол\VS\python\lab 6', os.X_OK))
"""