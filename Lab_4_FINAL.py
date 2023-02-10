class Tax:
    """ Базовый класс - налог """

    def __init__(self, name: str, t_object: str, t_period: int, t_base: float):
        """
        Создание и подготовка к работе объекта - налог (в соответствии с НК РФ)
        :param name: название налога
        :param t_object: название объекта налогообложения
        :param t_period: налоговый период (в днях)
        :param t_base: исчисленная налоговая база (в руб.)
        """
        self._name = name
        self._t_object = t_object
        self._t_period = t_period
        self.t_base = t_base

    def __str__(self):
        return f"Название налога - {self.name}. Объект налогообложения - {self.t_object}. " \
               f"Налоговый период - {self.t_period} дней. Налоговая база - {self.t_base} руб."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, t_object={self.t_object!r}, t_period={self.t_period}, " \
               f"t_base={self.t_base})"

    @property
    def name(self) -> str:
        """"Возвращает название налога."""
        return self._name

    @property
    def t_object(self) -> str:
        """"Возвращает объект налогообложения."""
        return self._t_object

    @property
    def t_period(self) -> int:
        """"Возвращает налоговый период в днях."""
        return self._t_period

    @property
    def t_base(self) -> float:
        """"Возвращает исчисленную в руб. базу налогообложения за налоговый период."""
        return self.t_base

    @t_base.setter
    def t_base(self, t_base: float) -> None:
        """Устанавливает налоговую базу за налоговый период."""
        if not isinstance(t_base, float):
            raise TypeError("Налоговая база исчисляется в руб. и должна иметь тип float")
        if t_base < 0:
            raise ValueError("Налоговая база за налоговый период должна быть неотрицательным числом")
        self.t_base = t_base

    def is_tax_base(self) -> bool:
        """"Проверяет не нулевая ли налоговая база - есть ли налоговая база за налоговый период."""
        return self.t_base > 0

    def tax_payable(self, t_rate: float) -> float:
        """
        Вычисляет налог для уплаты за налоговый период
        :t_rate: ставка налогообложения по конкретному налогу на конкретный объект н/о за налоговый период
        Примеры:
        tax_1 = Tax("Enterprise_profit_tax", "profit_company", 365, 111000000.5)
        tax_to_pay = tax_1.tax_payable(0.2)
        print(tax_1.is_tax_base())
        """
        return self.t_base * t_rate


class Physical(Tax):
    """ Дочерний класс - налог на доходы физического лица """
    def __init__(self, name: str, t_object: str, t_period: int, t_base: float, t_deduction: float):
        """
        Создание и подготовка к работе объекта налог на доходы физ. лица (в соответствии с НК РФ)
        :param t_deduction: размер налогового вычета
        """
        super().__init__(name, t_object, t_period, t_base)  # берем параметры базового класса
        self._t_deduction = t_deduction

    def __str__(self):
        return f"Название налога - {self.name}. Объект налогообложения - {self.t_object}. " \
               f"Налоговый период - {self.t_period} дней. Налоговая база - {self.t_base} руб." \
               f"Размер налогового вычета - {self.t_deduction} руб."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, t_object={self.t_object!r}, t_period={self.t_period}, " \
               f"t_base={self.t_base}, t_deduction={self.t_deduction})"

    @property
    def t_deduction(self) -> float:
        """"Возвращает сумму налогового вычета"""
        return self._t_deduction

    def is_tax_base(self) -> bool:
        """ Так же проверяем наличие налоговой базы  """
        is_tax_base = super().is_tax_base()
        return is_tax_base

    def ph_tax_payable(self, t_rate: float) -> float:
        """
        Вычисляет сумму налога на доход физ.лица для уплаты за налоговый период
        :param t_rate: ставка налогообложения по налогу на доход физ.лица за конкретный объект н/о
        Примеры:
        Petr_tax = Physical("Petr_tax_2022", "wage", 365, 4000000., 100000.)
        Petr_tax_to_pay = Petr_tax.ph_tax_payable(0.13)
        print(Petr_tax.is_tax_base())
        """
        return (self.t_base - self.t_deduction) * t_rate  # перегружаем, тк формула исчисления отлична от tax_payable


if __name__ == "__main__":
    a = Tax("VAD_2020", "value_added", 365, 500000000.)
    b = Physical("Anna_tax_2022", "lottery_prize", 365, 5000000., 10000.)
    print(b.ph_tax_payable(0.35))
    print(a.is_tax_base())
    pass
