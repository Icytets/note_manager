username = input("Введите ваше имя: ")
title = input("Введите название заметки 1: ")
title2 = input("Введите название заметки 2: ")
title3 = input("Введите название заметки 3: ")
content = input("Введите описание заметки: ")
status = input("Введите статус \"Выполнил/Не выполнил\"")
created_date = input("Введите дату создания в формате dd.mm.yyyy: ")
issue_date = input("Введите дату дедлайна в формате dd.mm.yyyy: ")
note = [
    username,
    title,
    content,
    status,
    created_date,
    issue_date,
    [title2, title3]
]
print("\nЗаметка от пользователя: " + note[0],
      "Заголовок: " + note[1],
      "Описание: " + note[2],
      "Статус: " + note[3],
      "Время создания: " + note[4],
      "Дедлайн: " + note[5], sep = "\n")