class Note:
    def __init__(self, title, content):
        # Инициализация заметки с заголовком и содержимым
        self.title = title
        self.content = content

    def to_dict(self):
        # Преобразование объекта заметки в словарь
        return {"title": self.title, "content": self.content}

    @staticmethod
    def from_dict(note_dict):
        # Создание объекта заметки из словаря
        return Note(note_dict["title"], note_dict["content"])