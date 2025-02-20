def even_numbers(N):
    for x in range(0, N+1, 2):
        print(x, end=", " if x + 2 < N+1 else "")
        
N = int(input()) 

even_numbers(N)

