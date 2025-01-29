notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену'},
    {'username': 'Данила', 'title': 'Учеба', 'content': 'Подготовиться к экзамену'},
]

def display_notes():
    print("Текущие заметки: \n")
    for i, note in enumerate(notes):
        print(f"Заметка {i + 1}:")
        print(f"Имя пользователя: {note['username']}")
        print(f"Заголовок: {note['title']}")
        print(f"Описание: {note['content']}")
        print("-" * 40)

def delete_note_by_username_or_title(search_term):
    global notes
    new_notes = [note for note in notes if note['username'] != search_term and note['title'] != search_term]

    if len(new_notes) == len(notes):
        print("Заметка не найдена.")
    else:
        notes = new_notes
        print("Заметка успешно удалена.")


display_notes()

delete_note = input("Введите имя пользователя или заголовок для удаления заметки: ")
delete_note_by_username_or_title(delete_note)

print("\nОбновленные заметки: \n")
display_notes()


