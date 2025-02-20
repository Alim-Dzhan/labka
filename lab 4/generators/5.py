def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())  
gen = countdown(n)

for number in gen:
    print(number)
