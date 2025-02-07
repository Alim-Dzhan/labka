def check(N):
    if N < 2:
        return False
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True

def filter_prime(numbers):
    list = []
    for num in numbers:
        if check(num):
            list.append(num)
    return list

numbers = list(map(int, input().split()))
primes = filter_prime(numbers)
print(primes)