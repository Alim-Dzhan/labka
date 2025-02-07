def unique_list(lists):
    new_list = []
    for value in lists:
        if value not in new_list:
            new_list.append(value)
    return new_list

lists = input().split()
lists = [int(num) for num in lists]

print(unique_list(lists))