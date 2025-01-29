status = ["Выполнено", "В процессе", "Отложено"]

print("Текущий статус заметки: " + status[1])

print("\nВыберите новый статус заметки: \n1. Выполнено \n2. В процессе \n3. Отложено")

change_status = int(input())

while change_status:
    if change_status == 1:
        print("Текущий статус заметки: " + status[0])
        break
    if change_status == 2:
        print("Текущий статус заметки: " + status[1])
        break
    if change_status == 3:
        print("Текущий статус заметки: " + status[2])
        break
    else:
        print("Введен некорректный вариант! Повторите попытку")
        change_status = int(input())