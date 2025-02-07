def sphere_volume(radius):
    return (4/3) * 3.1415 * (radius ** 3)

def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]