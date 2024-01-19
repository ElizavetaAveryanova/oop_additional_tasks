"""
Создай класс `Number` c полем `value` (указывается при инициализации)

Создай экземпляр, например `x = Number(7)`

Добавь методы:

`.get()` возвращает текущее value

`.add(<значение>)` добавляет указанное число к value

`.substract(<значение>)` вычитает указанное число из value
"""

class Number:
    """Класс `Number` c полем `value` (указывается при инициализации)"""

    def __init__(self, value):
        self.value = value

    def get(self):
        """Метод get()` возвращает текущее value"""
        return self.value

    def add(self, new_v):
        """Метод add(<значение>)` добавляет указанное число к value"""
        self.value += new_v
        return self.value

    def substract(self, sub_v):
        """Метод substract(<значение>)` вычитает указанное число из value"""
        self.value -= sub_v
        return self.value


# код для проверки 
n = Number(7)
print(n.get())  # 7
n.add(3)
print(n.get())  # 10
n.substract(5)
print(n.get())  # 5
