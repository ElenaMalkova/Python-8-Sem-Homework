
def printout_bd(myresult):
    for i in myresult:
        print(*i)


def get_value():
    return input("\nЧто вы хотите сделать?\n1 - посмотреть базу\n2 - добавить запись\n3 - удалить запись\n4 - найти по фамилии\nq - выход\nВведите номер опции: ")


def get_entry():
    new_entry = []
    new_entry.append(int(input("Введите ID сотрудника: ")))
    new_entry.append(input("Введите имя сотрудника: "))
    new_entry.append(input("Введите фамилию сотрудника: "))
    new_entry.append(input("Введите должность сотрудника: "))
    new_entry.append(int(input("Введите зарплату сотрудника: ")))
    new_entry.append(int(input("Введите бонус сотрудника: ")))
    return tuple(new_entry)


def get_deleted_id():
    return int(input("Введите id записи для удаления: "))


def get_surname_to_find():
    surname = [input("Введите фамилию сотрудника, которого вы хотите найти: ")]
    return tuple(surname)
