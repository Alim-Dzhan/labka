import re

text = input()
pattern = r'[a-z]+(?:_[a-z]+)*'

matches = re.findall(pattern, text)


if matches:
    print("Найденные последовательности:", matches)
else:
    print("Совпадений не найдено.")

