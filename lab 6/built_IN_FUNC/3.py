import re

def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z]', '', s).lower()
    
    return s == s[::-1]

txt =input()

if is_palindrome(txt):
    print("YES")
else:
    print("NO")

