
x_file = input()
y_file = input()

try:
    with open(x_file, 'r') as file1, open(y_file, 'a') as file2:
        for line in file1:
            file2.write(line)
    print(f"Содержимое из '{x_file}' успешно добавлено в '{y_file}'.")
except FileNotFoundError:
    print("Ошибка: Один из файлов не найден.")

