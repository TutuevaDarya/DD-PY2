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


class Library:
    def __init__(self, books: list = None):  # инициируем класс библиотека, где есть атрибут - список книг
        if books is None:  # если пользователь не передал список книг, то создаем пустой список
            books = []
        self.books = books

    def get_next_book_id(self):  # объявляем метод, возвращающий идентификатор для добавления новой книги в библиотеку
        if len(self.books) == 0:  # если список книг в библиотеке пуст, то возвращаем индекс 1
            return 1
        else:  # если в библиотеке есть книги, возвращаем id последней книги+1
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int):  # объявляем метод возвращающий индекс книги в списке из атр.экз.класса
        for value, books in enumerate(BOOKS_DATABASE):
            if books["id"] == id_ and "id" in books:  # если книга с искомым id есть в списке, вернем ее индекс из списк
                return value
            else:  # если книги с искомым id в списке нет, то говорим об этом пользователю
                return ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(get_index_by_book_id(1))  # проверяем индекс книги с id = 1
