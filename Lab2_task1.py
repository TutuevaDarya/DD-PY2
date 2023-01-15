BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):  # создаем класс книг с 3 атрибутами
        if not isinstance(id_, int):  # обозначаем проверки атрибута id
            raise TypeError("Уникальный идентификатор книги должен быть целым -  int")
        if id_ <= 0:
            raise ValueError("Уникальный идентификатор книги должен быть положительным числом")
        self.id_ = id_

        if not isinstance(name, str):  # обозначаем проверки атрибута name
            raise TypeError("Название книги должно быть в формате строки -  str")
        self.name = name

        if not isinstance(pages, int):  # обозначаем проверки атрибута pages
            raise TypeError("Число страниц книги должно быть целым числом -  int")
        if pages <= 0:
            raise ValueError("Число страниц книги должно быть положительным числом")
        self.pages = pages

    def __str__(self) -> str:  # объявляем метод __str__
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:  # объявляем метод __repr__
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
