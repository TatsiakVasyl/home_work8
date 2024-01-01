from collections import defaultdict
from datetime import date, datetime


def get_birthdays_per_week(users):

    birthdays_per_week = defaultdict(list)
    today = date.today()

    for user in users:
        user_birthday = user["birthday"].replace(year=today.year)
        if user_birthday < today:
            user_birthday = user_birthday.replace(year=today.year+1)
        delta = user_birthday - today

        if delta.days >= 7:
            continue

        birthday_day_of_week = user_birthday.strftime('%A')

        if birthday_day_of_week in ["Saturday", "Sunday"]:
            birthday_day_of_week = "Monday"

        birthdays_per_week[birthday_day_of_week].append(user["name"])

    return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Teylor", "birthday": date(1980, 4, 3)},
        {"name": "Bill Gates", "birthday": date(1955, 10, 28)}
    ]

    result = get_birthdays_per_week(users)
    print(result)

    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")





