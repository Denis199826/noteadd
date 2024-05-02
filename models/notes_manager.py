import os
import json
from models.note import Note

class NotesManager:
    def __init__(self, notes_file="notes.json"):
        # Инициализация менеджера заметок с указанием файла для хранения заметок
        self.notes_file = notes_file
        self.notes = self.load_notes()

    def load_notes(self):
        # Загрузка заметок из файла
        if os.path.exists(self.notes_file):
            with open(self.notes_file, "r") as file:
                notes_data = json.load(file)
                return [Note.from_dict(note) for note in notes_data]
        else:
            return []

    def save_notes(self):
        # Сохранение заметок в файл
        with open(self.notes_file, "w") as file:
            json.dump([note.to_dict() for note in self.notes], file)

    def create_note(self, title, content):
        # Создание новой заметки
        note = Note(title, content)
        self.notes.append(note)
        self.save_notes()

    def read_notes(self):
        # Вывод списка всех заметок
        for index, note in enumerate(self.notes):
            print(f"{index + 1}. {note.title}")

    def edit_note(self, note_index, new_title, new_content):
        # Редактирование заметки
        if 1 <= note_index <= len(self.notes):
            self.notes[note_index - 1].title = new_title
            self.notes[note_index - 1].content = new_content
            self.save_notes()
        else:
            print("Неверный индекс заметки")

    def delete_note(self, note_index):
        # Удаление заметки
        if 1 <= note_index <= len(self.notes):
            del self.notes[note_index - 1]
            self.save_notes()
        else:
            print("Неверный индекс заметки")