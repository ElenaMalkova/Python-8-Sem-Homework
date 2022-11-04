import sqlite3
import view

bd = sqlite3.connect("Database.db")
cursor = bd.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS personnel(
    id INTEGER PRIMARY KEY,
    name TEXT,
    last_name TEXT,
    position TEXT,
    salary INT,
    bonus INT
)''')


baza = [(1, "Петр", "Сидоров", "директор", 100000, 30000),
        (2, "Василий", "Иванов", "менеджер по продажам", 60000, 20000),
        (3, "Сергей", "Сергеев", "маркетолог", 50000, 10000),
        (4, "Антон", "Михеев", "водитель", 40000, 5000),
        (5, "Ирина", "Жукова", "менеджер по продажам", 60000, 15000),
        (6, "Полина", "Кравцова", "бухгалтер", 70000, 25000)]


try:
    cursor.executemany('INSERT INTO personnel VALUES(?, ?, ?, ?, ?, ?)', baza)
    bd.commit
except:
    print('Данные уже есть')


def preview_base():
    return cursor.execute('SELECT * FROM personnel')


def add_entry():
    new_entry = [view.get_entry()]
    cursor.executemany(
        'INSERT INTO personnel VALUES (?, ?, ?, ?, ?, ?)', new_entry)
    bd.commit()


def delete_entry():
    id = view.get_deleted_id()
    cursor.execute(f'DELETE FROM personnel WHERE id = {id};')
    bd.commit()


def find_by_surname():
    surname = view.get_surname_to_find()
    cursor.execute(f'SELECT * FROM personnel WHERE last_name LIKE "{surname}"')
    one = cursor.fetchall()
    print(one)
