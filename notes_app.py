
import os
import presenter


def button_click():
    os.system('cls')
    print("Добро пожаловать в \"Записки\"! \n")
    notebook = presenter.load_from_file()
    notebook.sort(key=lambda d: d['date'])

    while True:
        print("Выберите действие: \n1 - создать запись \n2 - прочитать запись \n3 - прочитать все записи \n4 - редактировать запись \n5 - удалить запись")
        key = input()
        os.system('cls')
        match key:
            case "1":
                presenter.create_note(notebook)
            case "2":
                presenter.show_note(notebook)
            case "3":
                presenter.show_all_notes(notebook)
            case "4":
                presenter.edit_note(notebook)
            case "5":
                presenter.delete_note(notebook)
            case _:
                print("Такой команды нет( ")


button_click()