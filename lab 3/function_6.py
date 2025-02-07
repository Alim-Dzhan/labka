def reverse_words():
    user_input = input("sentence: ")
    words = user_input.split()
    result = ' '.join(reversed(words))  
    return result

print(reverse_words())