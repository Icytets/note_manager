print("Добро пожаловать в \"Менеджер заметок\"! Вы можете добавить новую заметку.")
notes = {
    'username': [],
    'title': [],
    'content': [],
    'status': [],
    'created_date': [],
    'issue_date': [],
}

while True:
    notes['username'].append(input("Введите ваше имя: "))
    notes['title'].append(input("Введите название заметки: "))
    notes['content'].append(input("Введите описание заметки: "))
    notes['status'].append(input("Введите статус \"Выполнил/Не выполнил\""))
    notes['created_date'].append(input("Введите дату создания в формате dd-mm-yyyy: "))
    notes['issue_date'].append(input("Введите дату дедлайна в формате dd-mm-yyyy: "))

    continue_input = input("Хотите добавить еще одну заметку? (да/нет): ")
    if continue_input.lower() != 'да':
        break

print("\nВаши заметки:\n")
for i in range(len(notes['title'])):
    print(f"Заметка {i + 1}:")
    print(f"  Имя пользователя: {notes['username'][i]}")
    print(f"  Заголовок: {notes['title'][i]}")
    print(f"  Описание: {notes['content'][i]}")
    print(f"  Статус: {notes['status'][i]}")
    print(f"  Дата создания: {notes['created_date'][i]}")
    print(f"  Дата дедлайна: {notes['issue_date'][i]}")
    print("-" * 40)