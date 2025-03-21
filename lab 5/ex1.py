"""
# date
import datetime

now=datetime.datetime.now()
new_date=now.replace(second=0)
print(new_date)

# gen

def generators(n):
    x=0
    while x<n:
        yield x**2
        x+=1

n=int(input())
gen=generators(n)
for t in gen:
    print(t)
    """

def gener(n):
    for i in range(0, n+1, 2):
        print(i)
n=int(input())
gener(n)




