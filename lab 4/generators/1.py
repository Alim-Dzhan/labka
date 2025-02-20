def my_generator(N):
    x = 0
    while x <= N:
        yield x**2
        x += 1


N = int(input()) 
gen = my_generator(N)

for square in gen:
    print(square)
