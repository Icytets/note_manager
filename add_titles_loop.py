titles = []

while True:
    title = input("Введите заголовок заметки (или 'стоп' для завершения): ")

    if title.lower() == 'стоп' or title == '':
        break

    if title:
        titles.append(title)

print("\nСписок добавленных заголовков:")
for title in titles:
    print(f"- {title}")
