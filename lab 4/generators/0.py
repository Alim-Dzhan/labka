# Generators

def my_generators():
    yield 1
    yield 3
    yield 2

gen = my_generators()
print(next(gen))
print(next(gen))
print(next(gen))

for num in my_generators():
    print(num)




def example():
    yield "hello"
    yield "world"

gen = example()
print(next(gen))
print(next(gen))
