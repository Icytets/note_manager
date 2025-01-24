username = "Борис"
title = "Приступить к выполнению Задания"
content = " Приступить к выполнению задания Grade 1. Этап 1: Задание 1. Сделать первую заметку"
status = True
created_date = "16.01.2025"
issue_date = "16.01.2025"

if status == True:
    status = "Выполнено"
else:
    status = "Не выполнено"


print("Заметка от пользователя: " + username,
      "Заголовок: " + title,
      "Описание: " + content,
      "Статус: " + status,
      "Время создания: " + created_date,
      "Дедлайн: " + issue_date, sep ="\n")