import re

text = input()

words = re.findall(r'[A-Z][a-z]*', text)

print(words)
