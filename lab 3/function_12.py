def histogram(list):
    for num in list:
        print('*' * num)
        
list = input().split()
list = [int(n) for n in list]

histogram(list)