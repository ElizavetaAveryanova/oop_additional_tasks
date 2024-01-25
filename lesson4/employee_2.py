"""
Для класса Employee, опишите магический метод сложения таким образом, чтобы результатом сложения
было число, а прибавлять можно было только числа или другие объекты дочерних классов Employee
"""

class Employee:
    def __init__(self, pay):
        self.pay = pay

    def __add__(self, other):
        if isinstance(other, (int, float)) and not isinstance(other, Client):
            return self.pay + other
        elif isinstance(other, Employee) and not isinstance(other, Client):
            return self.pay + other.pay
        else:
            raise TypeError("Сложение невозможно")

    def __radd__(self, other):
        if isinstance(other, (int, float)) and not isinstance(other, Client):
            return other + self.pay
        elif isinstance(other, Employee) and not isinstance(other, Client):
            return other.pay + self.pay
        else:
            raise TypeError("Сложение невозможно")


class Client:
    def __init__(self, pay):
        self.pay = pay


class Developer(Employee):
    pass


class Manager(Employee):
    pass

# код для проверки
users = [Employee(50000), Client(100000), Developer(50000), Manager(50000)]

total_salary = 0
for user in users:
    if not isinstance(user, Client):
        total_salary = total_salary + user

print(total_salary)
# Вывод: 150000
