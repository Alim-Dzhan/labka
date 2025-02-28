def snake_to_camel(snake_str):
    words = snake_str.split('_')
    
    camel_str = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_str

snake_string = input()
camel_string = snake_to_camel(snake_string)
print(camel_string)
