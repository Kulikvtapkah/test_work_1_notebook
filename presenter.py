import os
import model
import console_view
import path_config as c
from datetime import datetime


def new_note():
    return {"date": f"{datetime.today()}", "header": console_view.get_header(),
            "Main text": console_view.get_main_text()}


def load_from_file():

    return model.load(c.path())


def create_note(notebook: list):
    console_view.user_info("Добавим записку:\n")
    notebook.append(new_note())
    model.save(notebook, c.path())


def show_note(notebook: list):
    console_view.user_info("Читаем записку:\n")
    try:
        index = console_view.get_id() - 1
        console_view.show_note(notebook, index)

    except:
        console_view.user_info(
            "Нет записи с таким номером \n")


def show_all_notes(notebook):
    os.system('cls')
    console_view.user_info("Все записки:\n")
    for i in range(len(notebook)):
        console_view.show_note(notebook, i)


def edit_note(notebook: list):
    console_view.user_info("Редактируем записку:\n")
    try:
        index = console_view.get_id() - 1
        console_view.show_note(notebook, index)
        console_view.user_info("Запись будет заменена:\n")
        notebook[index] = new_note()
        model.save(notebook, c.path())

    except:
        console_view.user_info(
            "Нет записи с таким номером \n")


def delete_note(notebook: list):
    console_view.user_info("Удаляем записку:\n")
    try:
        index = console_view.get_id() - 1
        notebook.pop(index)

        console_view.user_info(f"Запись {index + 1} удалена:\n")
        model.save(notebook, c.path())

    except:
        console_view.user_info(
            "Нет записи с таким номером \n")
