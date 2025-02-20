def my_generator(a, b):
    for x in range(a, b+1):  
        yield x**2

a = int(input())
b = int(input())
gen = my_generator(a, b)

for square in gen:
    print(square)





    