import doctest


class IT:
    def __init__(self, exp_years: int, number_proj: int):
        """
        Создание и подготовка к работе объекта "IT" - сотрудника программиста
        :param exp_years: Число лет опыта работы программистом
        :param number_proj: Количество проектов, в которых участвует как исполнитель
        Примеры:
        >>> it_Sasha = IT(5, 3)  # инициализация экземпляра класса - программиста Саши
        """
        if not isinstance(exp_years, int):
            raise TypeError("Число лет опыта работы должно быть целым -  int")
        if exp_years <= 0:
            raise ValueError("Программист должен иметь опыт работы")
        self.exp_years = exp_years

        if not isinstance(number_proj, int):
            raise TypeError("Количество проектов измеряется целыми числами")
        if number_proj < 0:
            raise ValueError("Количество актуальных проектов не должно быть отрицательным")
        self.number_proj = number_proj

    def is_free_it(self) -> bool:
        """
        Функция которая проверяет свободен ли программист
        :return: Действительно ли у программиста сейчас 0 актуальных проектов?
        Примеры:
        >>> it_Dima = IT(2, 0)
        >>> it_Dima.is_free_it()
        """
        ...

    def add_number_proj(self, proj: int) -> None:
        """
        Добавление актуального проекта в работу, включение в проектную команду программиста.
        :param proj: Количество добавлемых проектов
        Примеры:
        >>> it_Vlad = IT(3, 2)
        >>> it_Vlad.add_number_proj(1)
        """
        if not isinstance(proj, int):
            raise TypeError("Количество добавляемых проектов всегда целое - int")
        if proj <= 0:
            raise ValueError("Количество добавляемых проектов всегда положительное")
        ...

    def index_exp_years(self, exp_years: int) -> None:
        """
        Индексация опыта работы программиста по прошествии лет работы в компании
        :param exp_years: Начисление лет опыта работы
        :return: Начисленное число лет опыта работы
        Примеры:
        >>> it_Oleg = IT(10, 3)
        >>> it_Oleg.index_exp_years(1)
        """
        ...


class Prod_manager:
    def __init__(self, workforce: int, operations: list):
        """
        Создание и подготовка к работе объекта "Менеджер производства".
        :param workforce: Число людей - сотрудников производства, которым управляет менеджер
        :param operations: Список операций - переделов на производстве, которым управляет менеджер
        Примеры:
        >>> prod_manager_Igor = Prod_manager(100, ["прокатка", 'сборка'])  # инициализация экземпляра класса
        """
        if not isinstance(workforce, int):
            raise TypeError("Число подотчетных сотрудников может быть только целым")
        if workforce <= 0:
            raise ValueError("Число подотчетных сотрудников может быть только положительным")
        self.workforce = workforce

        if not isinstance(operations, list):
            raise TypeError("Перечень операций задается только списком!")
        self.operations = operations

    def add_workforce(self, workforce: int) -> None:
        """
        Добавление подчиненных сотрудников в команду менеджера производства.
        :param workforce: Число добавляемых сотрудников
        Примеры:
        >>> prod_manager_Igor = Prod_manager(100, ["прокатка", 'сборка'])
        >>> prod_manager_Igor.add_workforce(10)
        """
        if not isinstance(workforce, int):
            raise TypeError("Число добавляемых сотрудников только int!")
        if workforce <= 0:
            raise ValueError("Число добавляемых сотрудников только положительное")
        ...

    def add_operations(self, operation: str) -> None:
        """
        Добавление в полномочия менеджера производства производственной операции.
        :param operation: Название производственной операции
        Примеры:
        >>> prod_manager_Igor = Prod_manager(100, ["прокатка", 'сборка'])
        >>> prod_manager_Igor.add_operations('упаковка')
        """
        ...


class Fin_man:
    def __init__(self, overall_funds: float, used_funds: float):
        """
        Создание и подготовка к работе объекта "Финансовый менеджер".
        :param overall_funds: Суммарный объем денежных средств в управлении
        :param used_funds: Объем денежных средств, уже размещенных в ценных бумагах
        Примеры:
        >>> fin_man_Darya = Fin_man(1000.0, 100.0)  # инициализация экземпляра класса
        """
        if not isinstance(overall_funds, float):
            raise TypeError("Суммарный объем ДС в управлении только float")
        if overall_funds <= 0:
            raise ValueError("Суммарный объем ДС в управлении должен быть положительным числом")
        self.Overall_funds = overall_funds

        if not isinstance(used_funds, float):
            raise TypeError("Объем денежных средств, уже размещенных в ценных бумагах только float")
        if used_funds <= 0:
            raise ValueError("Объем денежных средств, уже размещенных в ценных бумагах должен быть положительным")
        self.Used_funds = used_funds

    def all_funds_used(self) -> bool:
        """
        Функция которая проверяет все ли денежные средства уже размещены в ценных бумагах
        :return: Равна ли сумма размещенных в ЦБ денежных средств суммарному объему средств в управлении
        Примеры:
        >>> fin_man_Darya = Fin_man(1000.0, 100.0)
        >>> fin_man_Darya.all_funds_used()
        """
        ...

    def use_funds(self, funds: float) -> None:
        """
        Размещение денежных средств в управлении в ценных бумагах.
        :param funds: Объем денежных средств в управлении, которые тратятся на покупку ценных бумаг.
        :raise ValueError: Если количество денег на покупку новых ценных бумаг превышает остаток неиспользованных денег,
        то вызываем ошибку
        Примеры:
        >>> fin_man_Darya = Fin_man(1000.0, 100.0)
        >>> fin_man_Darya.use_funds(200.0)
        """
        if not isinstance(funds, float):
            raise TypeError("Количество денег на покупку новых ценных бумаг должно быть float")
        if funds <= 0:
            raise ValueError("Количество денег на покупку новых ценных бумаг должно быть положительным числом")
        ...

    def return_funds(self, return_fund: float) -> None:
        """
        Продажа ЦБ (ценных бумаг) и возвращение денежных средств.
        :param return_fund: Кол-во денег от продажи ценных бумаг
        :raise ValueError: Если кол-во денег от продажи ценных бумаг превышает количество средств, размещенных в ЦБ,
        то возвращается ошибка.
        :return: Кол-во средств переведенных из состояния "ценные бумаги" в реальные деньги.
        Примеры:
        >>> fin_man_Darya = Fin_man(1000.0, 300.0)
        >>> fin_man_Darya.return_funds(100.0)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
