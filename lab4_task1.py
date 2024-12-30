# TODO: описать базовый класс

class Animal:
    """
    Базовый класс для создания различных животных.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Конструктор для класса Animal.

        :param name: Имя животного.
        :param age: Возраст животного в годах.
        """
        self.__name = name  # Непубличный атрибут, чтобы не допустить изменения имени напрямую
        self.__age = age  # Непубличный атрибут для возраста

    def speak(self) -> str:
        """
        Метод, который возвращает звук, издаваемый животным.
        По умолчанию возвращает 'Some sound'.

        :return: Звук, издаваемый животным.
        """
        return "Some sound"

    def __str__(self) -> str:
        """
        Возвращает строковое представление животного.

        :return: Строка с именем и возрастом животного.
        """
        return f"{self.__name}, {self.__age} years old"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление животного.

        :return: Строка в формате <ClassName: name, age>.
        """
        return f"<Animal: {self.__name}, {self.__age}>"

# TODO: описать дочерний класс

class Dog(Animal):
    """
    Класс, представляющий собаку, наследует от класса Animal.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Конструктор для класса Dog.

        :param name: Имя собаки.
        :param age: Возраст собаки в годах.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)
        self.__breed = breed  # Непубличный атрибут для породы

    def speak(self) -> str:
        """
        Переопределение метода speak для собаки.

        :return: Звук, издаваемый собакой.

        Обоснование: Каждое животное может издавать уникальные звуки, поэтому метод
        speak для класса Dog переопределяется, чтобы вернуть "Woof!".
        """
        return "Woof!"

    def __str__(self) -> str:
        """
        Переопределение строкового представления для класса Dog.

        :return: Строка с именем, возрастом и породой собаки.
        """
        return f"{super().__str__()}, Breed: {self.__breed}"

    def __repr__(self) -> str:
        """
        Переопределение формального строкового представления для класса Dog.

        :return: Строка в формате <ClassName: name, age, breed>.
        """
        return f"<Dog: {self._Animal__name}, {self._Animal__age}, {self.__breed}>"


class Cat(Animal):
    """
    Класс, представляющий кошку, наследует от класса Animal.
    """

    def __init__(self, name: str, age: int, color: str) -> None:
        """
        Конструктор для класса Cat.

        :param name: Имя кошки.
        :param age: Возраст кошки в годах.
        :param color: Цвет кошки.
        """
        super().__init__(name, age)
        self.__color = color  # Непубличный атрибут для цвета

    def speak(self) -> str:
        """
        Переопределение метода speak для кошки.

        :return: Звук, издаваемый кошкой.

        Обоснование: Каждое животное может издавать уникальные звуки, поэтому метод
        speak для класса Cat переопределяется, чтобы вернуть "Meow!".
        """
        return "Meow!"

    def __str__(self) -> str:
        """
        Переопределение строкового представления для класса Cat.

        :return: Строка с именем, возрастом и цветом кошки.
        """
        return f"{super().__str__()}, Color: {self.__color}"

    def __repr__(self) -> str:
        """
        Переопределение формального строкового представления для класса Cat.

        :return: Строка в формате <ClassName: name, age, color>.
        """
        return f"<Cat: {self._Animal__name}, {self._Animal__age}, {self.__color}>"

# пример использования классов
if __name__ == "__main__":
    dog = Dog("Sobaka", 3, "Golden Retriever")
    cat = Cat("Kot", 2, "Brown")

    print(dog)      # Вывод: Sobaka, 3 years old, Breed: Golden Retriever
    print(cat)      # Вывод: Kot, 2 years old, Color: Brown
    print(dog.speak())  # Вывод: Woof!
    print(cat.speak())  # Вывод: Meow!