import psycopg2
import csv

# Подключение к базе данных
conn = psycopg2.connect(
    database="PP2",
    user="postgres",
    password="Alimzhan05032007",
    host="localhost",
    port="5432" 
)
cur = conn.cursor()

# Создание таблицы
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    phone VARCHAR(20) UNIQUE
)
""")
conn.commit()

def insert_from_csv(file_path):
    file_path = input("Enter path to CSV file: ")
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) != 2:
                    print(f"⚠️ Skipping invalid row: {row}")
                    continue
                try:
                    cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", row)
                    conn.commit()  # Коммитим каждую вставку отдельно
                except psycopg2.IntegrityError as e:
                    conn.rollback()  # Отменяем только неудачную вставку
                    print(f"⚠️ Failed to insert {row}: {e.pgerror.strip()}")
                except Exception as e:
                    conn.rollback()
                    print(f"❌ Unexpected error inserting {row}: {e}")
        print("✅ CSV import complete.")
    except FileNotFoundError:
        print("❌ CSV file not found.")


# Ввод пользователя
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    try:
        cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("✅ Contact added.")
    except psycopg2.Error as e:
        print("❌ Error inserting data:", e.pgerror.strip())

# Обновление данных
def update_contact():
    phone = input("Enter phone of contact to update: ")
    print("1. Change name\n2. Change phone")
    choice = input("Choose option: ")
    if choice == '1':
        new_name = input("Enter new name: ")
        cur.execute("UPDATE phonebook SET first_name = %s WHERE phone = %s", (new_name, phone))
    elif choice == '2':
        new_phone = input("Enter new phone: ")
        cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (new_phone, phone))
    else:
        print("❌ Invalid option.")
        return
    conn.commit()
    print("✅ Contact updated.")

# Удаление по имени или номеру
def delete_contact():
    identifier = input("Enter name or phone to delete: ")
    cur.execute("DELETE FROM phonebook WHERE first_name = %s OR phone = %s", (identifier, identifier))
    conn.commit()
    print("✅ Contact deleted (if existed).")

# Просмотр всех контактов
def view_all_contacts():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    if not rows:
        print("📭 PhoneBook is empty.")
    else:
        print("\n📱 PhoneBook Entries:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")

# Фильтрация по имени или номеру
def filter_contacts():
    value = input("Enter name or phone to search: ")
    cur.execute("SELECT * FROM phonebook WHERE first_name = %s OR phone = %s", (value, value))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(f"🔍 ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    else:
        print("❌ No matching contacts found.")

# Главное меню
def menu():
    while True:
        print("\n📖 PhoneBook Menu:")
        print("1. Upload from CSV")
        print("2. Add contact manually")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. View all contacts")
        print("6. Filter contacts")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            insert_from_csv("contacts.csv")
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            view_all_contacts()
        elif choice == '6':
            filter_contacts()
        elif choice == '0':
            print("👋 Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

menu()

cur.close()
conn.close()

''' 
DROP TABLE IF EXISTS phonebook;
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    phone VARCHAR(20) UNIQUE
);

INSERT INTO phonebook (first_name, phone)
VALUES 
('John', '87771234567'),
('Ali', '87001234567'),
('Nursultan', '87007775566');

SELECT * FROM phonebook;
'''
# C:\Users\dzhan\OneDrive\Рабочий стол\VS\python\lab 10\contacts.csv