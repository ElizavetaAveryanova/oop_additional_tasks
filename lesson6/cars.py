"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""

import datetime
class Car:
    def __init__(self, brand, model, year):
        current_year = datetime.datetime.now().year
        if year > current_year:
            raise Exception('Эта машина еще не была выпущена')
        self.brand = brand
        self.model = model
        self.year = year


# код для проверки
car = Car('Toyota', 'Corolla', 2022)

car = Car('Toyota', 'Corolla', 3000)
# raises Exception('Эта машина еще не была выпущена')
