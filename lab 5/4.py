import re
text=input()
if re.search(r'[A-Z][a-z]+',text):
    print("True")
else:
    print("False")