import re
text=input()

pattern=r'[ ,.]'
replaces= ":"

result=re.sub(pattern, replaces, text)
print(result)



