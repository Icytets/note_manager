username = input("Введите ваше имя: ")
title = input("Введите название заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус \"Выполнил/Не выполнил\"")    #True
created_date = input("Введите дату создания в формате dd.mm.yyyy: ")
issue_date = input("Введите дату дедлайна в формате dd.mm.yyyy: ")

print("\nЗаметка от пользователя: " + username,
      "Заголовок: " + title,
      "Описание: " + content,
      "Статус: " + status,
      "Время создания: " + created_date,
      "Дедлайн: " + issue_date, sep = "\n")