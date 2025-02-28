import re
text=input()
if re.search(r'^a.+b*$',text):
    print("True")
else:
    print("False")