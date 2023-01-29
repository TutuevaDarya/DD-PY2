class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property  # выполняем 3 пункт задания - пишем св-ва, не позволяющие менять название, автора книги
    def author(self):
        return self._author

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):  # выполняем 1 пункт задания - применяем наследование от базового класса Book
    """ Производный класс - бумажной книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # перегружаем аттрибуты базового класса, чтобы использовать в производном
        self._pages = None
        self._pages = pages

    @property  # выполняем 4 пункт задания - прописываем св-во - геттер для страниц
    def pages(self) -> int:
        return self._pages

    @pages.setter  # прописываем сеттер для страниц
    def pages(self, number_pages):
        if isinstance(number_pages, int):  # проверяем, что число страниц целое
            if number_pages <= 0:  # проверяем, что число страниц больше 0, страницы есть в книге
                raise ValueError("Ошибка - число страниц не положительное")
            else:
                self.pages = number_pages
        else:
            raise TypeError("Ошибка - число страниц должно быть целым числом")

    def __str__(self):  # выполняем 2 пункт задания - перегружаем метод __str__, чтобы выводить доп.аттрибут - страницы
        basic_str = super.__str__(self)  # наследуем инфо от базового класса
        return f"{basic_str}. Количество страниц в книге - {self.pages}"

    def __repr__(self):  # также перегружаем метод __repr__, чтобы выводить обязательный аттрибут - страницы
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

class AudioBook(Book):  # выполняем 1 пункт задания - применяем наследование от базового класса Book
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # перегружаем аттрибуты базового класса, чтобы использовать в производном
        self._duration = None
        self._duration = duration

    @property  # выполняем 4 пункт задания - прописываем св-во - геттер для длительности аудио-книги
    def duration(self) -> float:
        return self._duration

    @duration.setter  # прописываем сеттер для длительности аудио-книги
    def duration(self, number_time):
        if isinstance(number_time, float):  # проверяем, что длительность - типа float
            if number_time <= 0:  # проверяем, что длительность больше 0, книга записана
                raise ValueError("Ошибка - длительность аудио-книги не положительная")
            else:
                self.duration = number_time
        else:
            raise TypeError("Ошибка - длительность книги должна быть float")

    def __str__(self):  # выполняем 2 пункт задания - перегружаем метод __str__, чтобы выводить доп.аттрибут - длит.
        basic_str = super.__str__(self)  # наследуем инфо от базового класса
        return f"{basic_str}. Длительность аудио-книги - {self.duration}"

    def __repr__(self):  # также перегружаем метод __repr__, чтобы выводить обязательный аттрибут - длительность
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
