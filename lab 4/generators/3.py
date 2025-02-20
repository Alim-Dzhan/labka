def divides(N):
    for x in range(0, N + 1):
        if x % 3 == 0 and x % 4 == 0:
            yield x
            
N = int(input())
print(list(divides(N)))