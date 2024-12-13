# TODO: Подробно описать три произвольных класса


# TODO: описать класс
class CPU:
    """
    Класс, описывающий центральный процессор (CPU).
    """

    def __init__(self, clock_speed: float, cores: int):
        """
        :param clock_speed: тактовая частота в ГГц (должна быть больше 0).
        :param cores: количество ядер (должно быть целым числом > 0).
        """
        if clock_speed <= 0:
            raise ValueError("Clock speed must be greater than 0.")
        if not isinstance(cores, int) or cores <= 0:
            raise ValueError("Cores must be a positive integer.")

        self.clock_speed = clock_speed
        self.cores = cores

    def calculate_performance(self, load: float = 1.0) -> float:
        """
        Рассчитывает производительность CPU на заданной нагрузке.

        :param load: нагрузка в диапазоне от 0.0 до 1.0.
        :return: производительность в условных единицах.

        >>> cpu = CPU(3.5, 4)
        >>> cpu.calculate_performance(0.5)
        7.0
        """
        if not (0.0 <= load <= 1.0):
            raise ValueError("Load must be between 0.0 and 1.0.")
        return self.clock_speed * self.cores * load

    def overclock(self, increment: float) -> None:
        """
        Увеличивает тактовую частоту на заданное значение.

        :param increment: прирост частоты в ГГц (должен быть > 0).
        :raises ValueError: если increment <= 0.

        >>> cpu = CPU(3.5, 4)
        >>> cpu.overclock(0.5)
        >>> cpu.clock_speed
        4.0
        """
        if increment <= 0:
            raise ValueError("Increment must be greater than 0.")
        self.clock_speed += increment


# TODO: описать ещё класс
class Memory:
    """
    Класс, описывающий оперативную память (RAM).
    """

    def __init__(self, size_gb: int, frequency_mhz: int):
        """
        :param size_gb: объём памяти в ГБ (должен быть > 0).
        :param frequency_mhz: частота памяти в МГц (должна быть > 0).
        """
        if size_gb <= 0:
            raise ValueError("Memory size must be greater than 0.")
        if frequency_mhz <= 0:
            raise ValueError("Frequency must be greater than 0.")

        self.size_gb = size_gb
        self.frequency_mhz = frequency_mhz

    def can_handle_application(self, app_memory: int) -> bool:
        """
        Проверяет, сможет ли память обработать приложение.

        :param app_memory: требуемый объём памяти в ГБ.
        :return: True, если памяти достаточно, иначе False.

        >>> ram = Memory(16, 3200)
        >>> ram.can_handle_application(8)
        True
        """
        if app_memory < 0:
            raise ValueError("Application memory requirement must be non-negative.")
        return self.size_gb >= app_memory

    def upgrade(self, additional_size: int) -> None:
        """
        Увеличивает объём памяти.

        :param additional_size: добавляемый объём в ГБ (должен быть > 0).
        :raises ValueError: если additional_size <= 0.

        >>> ram = Memory(16, 3200)
        >>> ram.upgrade(8)
        >>> ram.size_gb
        24
        """
        if additional_size <= 0:
            raise ValueError("Additional size must be greater than 0.")
        self.size_gb += additional_size


# TODO: и ещё один
class Storage:
    """
    Класс, описывающий накопитель (Storage).
    """

    def __init__(self, capacity_tb: float, type: str):
        """
        :param capacity_tb: ёмкость в ТБ (должна быть > 0).
        :param type: тип накопителя ("HDD" или "SSD").
        """
        if capacity_tb <= 0:
            raise ValueError("Capacity must be greater than 0.")
        if type not in ("HDD", "SSD"):
            raise ValueError("Type must be either 'HDD' or 'SSD'.")

        self.capacity_tb = capacity_tb
        self.type = type

    def available_space(self, used_space: float) -> float:
        """
        Вычисляет доступное место на накопителе.

        :param used_space: занятое место в ТБ (должно быть >= 0).
        :return: доступное место в ТБ.

        >>> storage = Storage(2.0, "SSD")
        >>> storage.available_space(0.5)
        1.5
        """
        if used_space < 0 or used_space > self.capacity_tb:
            raise ValueError("Used space must be between 0 and the total capacity.")
        return self.capacity_tb - used_space

    def upgrade(self, additional_capacity: float) -> None:
        """
        Увеличивает ёмкость накопителя.

        :param additional_capacity: добавляемая ёмкость в ТБ (должна быть > 0).
        :raises ValueError: если additional_capacity <= 0.

        >>> storage = Storage(1.0, "HDD")
        >>> storage.upgrade(1.0)
        >>> storage.capacity_tb
        2.0
        """
        if additional_capacity <= 0:
            raise ValueError("Additional capacity must be greater than 0.")
        self.capacity_tb += additional_capacity
