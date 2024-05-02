from models.notes_manager import NotesManager

def main():
    manager = NotesManager()

    while True:
        print("\nМенеджер заметок")
        print("1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Введите ваш выбор: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержимое заметки: ")
            manager.create_note(title, content)
            print("Заметка успешно создана.")

        elif choice == "2":
            print("\nВсе заметки:")
            manager.read_notes()

        elif choice == "3":
            manager.read_notes()
            note_index = int(input("Введите индекс заметки для редактирования: "))
            new_title = input("Введите новый заголовок: ")
            new_content = input("Введите новое содержимое: ")
            manager.edit_note(note_index, new_title, new_content)
            print("Заметка успешно отредактирована.")

        elif choice == "4":
            manager.read_notes()
            note_index = int(input("Введите индекс заметки для удаления: "))
            manager.delete_note(note_index)
            print("Заметка успешно удалена.")

        elif choice == "5":
            print("Выход...")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()