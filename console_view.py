

def get_header():
    print("Введите заголовок >> ")
    return input()


def get_main_text():
    print("Введите текст записки >> ")
    return input()


def get_id():
    print("Введите номер записки >> ")
    index = -1
    try:
        index = int(input())
        print('----------------------')
    except ValueError:
        print("Неверый индекс(")
    return index


def user_info(message):
    print(message)


def show_note(notebook: list, index):
    note: dict = notebook[index]
    print(
        f"Запись {index + 1} от {note.get('date')}\n {note.get('header')}\n {note.get('Main text')}\n")
