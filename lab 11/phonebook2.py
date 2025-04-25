import psycopg2
import csv

# Настройки подключения к базе данных
DB_CONFIG = {
    'host': "localhost",
    'dbname': "phnbook2",
    'user': "postgres",
    'password': "Alimzhan05032007"
}

# Функция для подключения к базе данных
def connect():
    return psycopg2.connect(**DB_CONFIG)

# 1. Функция: поиск по частичному совпадению (имя, фамилия, телефон)
def search_pattern(pattern: str):
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
                return cur.fetchall()
    except Exception as e:
        print(f"Ошибка при поиске по шаблону: {e}")

# 2. Процедура: добавление или обновление пользователя по имени/телефону
def upsert_user(name: str, phone: str):
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL upsert_user(%s, %s)", (name, phone))
        print(f"Пользователь добавлен или обновлен: {name} -> {phone}")
    except Exception as e:
        print(f"Ошибка при добавлении/обновлении пользователя: {e}")

# 3.  массовая вставка пользователей с проверкой
def bulk_insert(names: list, phones: list):
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL bulk_insert_users(%s, %s)", (names, phones))
        print("Массовая вставка завершена. Неверные телефоны (если есть) записаны в базе данных.")
    except Exception as e:
        print(f"Ошибка при массовой вставке пользователей: {e}")

# 4. Функция: отображение с пагинацией (лимит/смещение)
def paginated_view(limit: int, offset: int):
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM paginate_phonebook(%s, %s)", (limit, offset))
                return cur.fetchall()
    except Exception as e:
        print(f"Ошибка при получении пагинированных данных: {e}")

# 5. удаление по имени или телефону
def delete_by_name_or_phone(pattern: str):
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL delete_by_name_or_phone(%s)", (pattern,))
        print(f"Записи, соответствующие шаблону: {pattern}, удалены.")
    except Exception as e:
        print(f"Ошибка при удалении записей: {e}")

# Дополнительные помощники (взаимодействие с консолью/CSV)
# Вставка одного пользователя через консоль
def insert_from_console():
    name = input("Имя: ")
    phone = input("Телефон: ")
    upsert_user(name, phone)

# Вставка данных из CSV файла
def insert_from_csv(path: str):
    names, phones = [], []
    try:
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 2:
                    names.append(row[0])
                    phones.append(row[1])
        bulk_insert(names, phones)
    except Exception as e:
        print(f"Ошибка при чтении CSV файла: {e}")

# Запрос всех записей
def query_all():
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM phonebook2 ORDER BY id")
                return cur.fetchall()
    except Exception as e:
        print(f"Ошибка при запросе всех пользователей: {e}")

# Запрос по имени
def query_by_name(name: str):
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM phonebook2 WHERE name = %s", (name,))
                return cur.fetchall()
    except Exception as e:
        print(f"Ошибка при запросе по имени: {e}")


def menu():
    while True:
        print("\n--- МЕНЮ КНИГИ СВЯЗИ ---")
        print("1. Вставить одного пользователя (консоль)")
        print("2. Массовая вставка из CSV")
        print("3. Добавить или обновить пользователя")
        print("4. Поиск по шаблону")
        print("5. Пагинированный просмотр")
        print("6. Удалить по имени или телефону")
        print("7. Показать всех")
        print("8. Выход")

        choice = input("Введите выбор: ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            insert_from_csv(input("Путь к CSV файлу: "))
        elif choice == '3':
            upsert_user(input("Имя: "), input("Телефон: "))
        elif choice == '4':
            for row in search_pattern(input("Шаблон: ")):
                print(row)
        elif choice == '5':
            try:
                limit = int(input("Лимит: "))
                offset = int(input("Смещение: "))
                for row in paginated_view(limit, offset):
                    print(row)
            except ValueError:
                print("Неверный ввод для лимита/смещения")
        elif choice == '6':
            delete_by_name_or_phone(input("Имя или телефон для удаления: "))
        elif choice == '7':
            for row in query_all():
                print(row)
        elif choice == '8':
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    menu()


#  C:\Users\dzhan\OneDrive\Рабочий стол\VS\python\lab 10\contacts.csv