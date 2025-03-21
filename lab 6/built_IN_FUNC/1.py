from functools import reduce

def multiply_numbers(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers = [2, 3, 4]
result = multiply_numbers(numbers)
print(result) 

