# TODO: описать базовый класс
class Register:
    """
    Базовый класс для представления регистра процессора.

    Атрибуты:
        name (str): Имя регистра (например, 'AX', 'BX').
        size (int): Размер регистра в битах (например, 8, 16, 32).
        value (int): Текущее значение регистра.
    """

    def __init__(self, name: str, size: int, value: int = 0):
        self.name = name
        self.size = size
        self._value = value  # Скрытый атрибут для ограничения прямого доступа

    def __str__(self):
        """Возвращает строковое представление регистра для пользователя."""
        return f"Register {self.name}: {self._value:#0{self.size // 4 + 2}x}"

    def __repr__(self):
        """Возвращает строковое представление регистра для разработчика."""
        return f"Register(name={self.name!r}, size={self.size!r}, value={self._value!r})"

    def read(self):
        """
        Чтение значения из регистра.
        """
        return self._value

    def write(self, value: int):
        """
        Запись значения в регистр.

        Аргументы:
            value (int): Значение, которое будет записано в регистр.

        Исключение:
            ValueError: Если значение превышает размер регистра.
        """
        if value < 0 or value >= (1 << self.size):
            raise ValueError(f"Значение {value} превышает размер регистра ({self.size} бит).")
        self._value = value


# TODO: описать дочерний класс

class GeneralPurposeRegister(Register):
    """
    Класс для представления общего регистра процессора.

    Атрибуты:
        name (str): Имя регистра (унаследован).
        size (int): Размер регистра (унаследован).
        value (int): Текущее значение регистра (унаследован).
        is_high (bool): Флаг, указывающий, используется ли старшая половина регистра.
    """

    def __init__(self, name: str, size: int, value: int = 0, is_high: bool = False):
        super().__init__(name, size, value)
        self.is_high = is_high  # Флаг для старшей половины регистра

    def __str__(self):
        """Возвращает строковое представление регистра с учетом старшей половины."""
        high_low = "HIGH" if self.is_high else "LOW"
        return f"GeneralPurposeRegister {self.name} ({high_low}): {self._value:#0{self.size // 4 + 2}x}"

    def write(self, value: int):
        """
        Переопределенный метод записи значения в регистр.

        Причина перегрузки:
        Для общего регистра дополнительно проверяется, используется ли старшая половина.
        """
        if self.is_high:
            if value < 0 or value >= (1 << (self.size // 2)):
                raise ValueError(f"Значение {value} превышает размер старшей половины регистра.")
            self._value = (self._value & 0x00FF) | (value << (self.size // 2))
        else:
            super().write(value)
