from task_1 import CPU, Memory, Storage  # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
    # TODO: инстанцировать все описанные классы, создав три объекта.C()
    cpu = CPU(3.5, 4)
    ram = Memory(16, 3200)
    storage = Storage(2.0, "SSD")

    try:
        # TODO: вызвать метод с некорректными аргументами(b)
        cpu.calculate_performance(1.5)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        cpu.overclock(-0.5)
    # TODO: вызвать метод с некорректными аргументами(a)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        # TODO: вызвать метод с некорректными аргументами(a)
        ram.can_handle_application(-1)
    except ValueError:
        print('Ошибка: неправильные данные')
