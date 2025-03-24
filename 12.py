# №1. Сходства
value = 10
additional = 5


def not_change1(val, add):
    val = val + add  # Реализуется метод __add__
    return val


def not_change2(val, add):
    val += add  # Реализуется все тот же метод __add__
    return val


# Результаты будут одинаковые, так как метод __iadd__, который вызывается
# функцией += определен только для списков
print("Result a = a + b:\t ", not_change1(value, additional))
print("Result a += b:\t\t ", not_change2(value, additional))
print()

# №2. Различия в реализации
value = ["1", "2", "3"]
additional = "4"


def change_not_error(val, add):
    val += add
    # Вызывается метод list_inplace_concat,
    # который позволяет добавлять любые итерируемые объекты
    return val


def change_error(val, add):
    val = val + add
    # Вызывается метод list_concat,
    # который позволяет добавлять строго только списки
    # ВЫДАСТ ОШИБКУ!
    return val


print("Result a += b:", change_not_error(value, additional))
#print("Result a = a + b:", change_error(value, additional))
print()

# №3. Различия в изменяемости объектов

value = [10, 11, 12]
additional = [345]
print(id(value)) # Исходный id


def change_id(val, add): # Будет вызван __iadd__, который не изменяет объекты
    val += add
    return id(val)


def not_change_id(val, add): # Будет вызван __add__, который изменяет объекты
    val = val + add
    return id(val)


print(change_id(value, additional)) # id не изменился
print(not_change_id(value, additional)) # id новый!
