import model
import view


def input_choice():
    while True:
        user_choice = view.get_value()
        if user_choice == "1":
            view.printout_bd(model.preview_base())
        elif user_choice == "2":
            model.add_entry()
            view.printout_bd(model.preview_base())
        elif user_choice == "3":
            model.delete_entry()
            view.printout_bd(model.preview_base())
        elif user_choice == "4":
            model.find_by_surname()
        elif user_choice == "q":
            print("Выход")
            break
        else:
            print("Некорректный ввод команды")
