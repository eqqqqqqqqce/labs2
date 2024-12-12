# TODO: Подробно описать три произвольных класса
import doctest

class Table:
    def __init__(self, material: str, length: float, width: float, height: float):
        """
        создание объекта "Стол"

        :param material: Материал стола
        :param length: Длина стола в сантиметрах
        :param width: Ширина стола в сантиметрах
        :param height: Высота стола в сантиметрах

        примеры:
        >>> table = Table("дерево", 120, 80, 75)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        self.material = material

        if not all(isinstance(dim, (int, float)) for dim in (length, width, height)):
            raise TypeError("Длина, ширина и высота должны быть типа int или float")

        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Длина, ширина и высота должны быть положительными числами")

        self.length = length
        self.width = width
        self.height = height

    def surface_area(self) -> float:
        """
        вычисляет площадь поверхности стола.

        :return: Площадь поверхности в квадратных сантиметрах

        примеры:
        >>> table = Table("дерево", 120, 80, 75)
        >>> table.surface_area()
        9600
        """
        return self.length * self.width

    def description(self) -> str:
        """
        возвращает текстовое описание стола.

        :return: Описание стола

        примеры:
        >>> table = Table("дерево", 120, 80, 75)
        >>> table.description()
        'Стол из материала дерево размером 120 см х 80 см х 75 см.'
        """
        return f'Стол из материала {self.material} размером {self.length} см х {self.width} см х {self.height} см.'

class Cat:
    def __init__(self, name: str, age: int, breed: str):
        """
        создание объекта "Кошка"

        :param name: Имя кошки
        :param age: Возраст кошки в годах
        :param breed: Порода кошки

        примеры:
        >>> cat = Cat("Маркиза", 3, "сиамская")
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        self.name = name

        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст должен быть неотрицательным целым числом")
        self.age = age

        if not isinstance(breed, str):
            raise TypeError("Порода должна быть строкой")
        self.breed = breed

    def meow(self) -> str:
        """
        возвращает звук, который издает кошка

        :return: Звук кошки

        примеры:
        >>> cat = Cat("Маркиза", 3, "сиамская")
        >>> cat.meow()
        'мяу!'
        """
        return "мяу!"

    def description(self) -> str:
        """
        возвращает текстовое описание кошки

        :return: Описание кошки

        примеры:
        >>> cat = Cat("Маркиза", 3, "сиамская")
        >>> cat.description()
        'Кошка по имени Маркиза, 3 года, порода: сиамская.'
        """
        return f'Кошка по имени {self.name}, {self.age} года, порода: {self.breed}.'

    def birthday(self) -> None:
        """
        увеличивает возраст кошки на один год

        примеры:
        >>> cat = Cat("Маркиза", 3, "сиамская")
        >>> cat.birthday()
        >>> cat.age
        4
        """
        self.age += 1


class Telegram:
    def __init__(self, user_count: int, creation_year: int):
        """
        создание объекта "Telegram"

        :param user_count: Количество пользователей
        :param creation_year: Год создания

        примеры:
        >>> tg = Telegram(950000000, 2013)
        """
        if not isinstance(user_count, int) or user_count < 0:
            raise ValueError("Количество пользователей должно быть положительным целым числом")
        self.user_count = user_count

        if not isinstance(creation_year, int):
            raise TypeError("Год создания должен быть целым числом")
        self.creation_year = creation_year

    def add_user(self) -> int:
        """
        увеличивает количество пользователей на один

        примеры:
        >>> tg = Telegram(950000000, 2013)
        >>> tg.add_user()
        >>> tg.user_count
        950000001
        """
        self.user_count += 1

    def platform_age(self) -> int:
        """
        возвращает возраст платформы в годах

        :return: Возраст социальной сети

        примеры:
        >>> tg = Telegram(950000000, 2013)
        >>> tg.platform_age()
        11
        """
        return 2024 - self.creation_year

    def description(self) -> str:
        """
        возвращает текстовое описание социальной сети

        :return: Описание Telegram

        примеры:
        >>> tg = Telegram(950000000, 2013)
        >>> tg.description()
        'Социальная сеть Telegram с 950000000 пользователей основана в 2013 году.'
        """
        return f'Социальная сеть Telegram с {self.user_count} пользователей основана в {self.creation_year} году.'

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации