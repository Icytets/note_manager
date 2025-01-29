from datetime import datetime

def get_current_date():
    return datetime.today()

def calculate_date_difference(issue_date_str):
    deadline_date = datetime.strptime(issue_date_str, "%d-%m-%Y").date()
    today = datetime.now().date()
    difference = (deadline_date - today).days
    return difference

print("Текущая дата: "+ get_current_date().strftime("%d-%m-%Y"))

issue_date = str(input("Введите дату дедлайна (в формате день-месяц-год): "))

try:
    days_until_issue = calculate_date_difference(issue_date)

    if days_until_issue > 0:
        print(f"До дедлайна осталось {days_until_issue} дней.")
    elif days_until_issue == 0:
        print("Сегодня последний день дедлайна!")
    else:
        print(f"Дедлайн уже прошел на {-days_until_issue} дней.")
except ValueError:
    print("Ошибка: Пожалуйста, введите дату в правильном формате (в формате день-месяц-год).")



