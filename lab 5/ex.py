import re
txt=input()
x= re.findall("[^a-c]", txt)
print(x)


def generator():
    yield 