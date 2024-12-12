from task_1 import Table, Cat, Telegram

if __name__ == "__main__":
    table = Table("дерево", 120, 80, 75)
    cat = Cat("Маркиза", 3, "сиамская")
    tg = Telegram(950000000, 2013)

    try:
        table.surface_area(cat)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        cat.birthday(table)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        tg.platform_age(table)
    except TypeError:
        print('Ошибка: неправильные данные')
