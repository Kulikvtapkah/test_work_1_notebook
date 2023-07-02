
import json


def load(path):
    notes = []
    try:

        with open(path) as saved_notes:
            notes_content = saved_notes.read()
            notes = json.loads(notes_content)
        saved_notes.close()
    except:
        print("Что-то пошло не так(")
    return notes


def save(notebook: list, path):
    notebook.sort(key=lambda d: d['date'])

    try:
        with open(path, 'w') as notes_to_save:
            json.dump(notebook, notes_to_save, sort_keys=True, indent=2)
        notes_to_save.close()

    except:
        print(
            "Что-то пошло не так. Заметки не сохранены(")
