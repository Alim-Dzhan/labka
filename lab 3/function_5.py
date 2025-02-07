from itertools import permutations
def print_permutations():
    user_input = input("Enter a string: ")
    perms = [''.join(p) for p in permutations(user_input)]
    print("Permutations:", perms)
print_permutations()