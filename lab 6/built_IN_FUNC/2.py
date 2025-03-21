#task 2
def count_case_letters(string):
    upper_count = sum(1 for char in string if char.isupper()) 
    lower_count = sum(1 for char in string if char.islower()) 
    return upper_count, lower_count

txt= "Hello World"
upper, lower = count_case_letters(txt)
print(f"Uppercase: {upper}, Lowercase: {lower}")












