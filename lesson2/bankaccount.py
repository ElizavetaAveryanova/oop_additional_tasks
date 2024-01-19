"""
Напишите класс BankAccount, имеющий следующие свойства и методы:

- __init__(self, balance): конструктор, принимающий начальный баланс счета
- balance: свойство, которое возвращает текущий баланс счета
- deposit(self, amount): метод, который позволяет внести деньги на счет
- withdraw(self, amount): метод, который позволяет снять деньги со счета
- close(self): метод, который закрывает счет и возвращает оставшиеся на нем деньги

Для свойства balance используйте декоратор @property.
"""


class BankAccount:
    def __init__(self, balance):
        """Конструктор, принимающий начальный баланс счета"""
        self.__balance = balance

    @property
    def balance(self):
        """Свойство, которое возвращает текущий баланс счета"""
        return self.__balance

    def deposit(self, amount):
        """Метод, который позволяет внести деньги на счет"""
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        """Метод, который позволяет снять деньги со счета"""
        self.__balance -= amount
        return self.__balance

    def close(self):
        """Метод, который закрывает счет и возвращает оставшиеся на нем деньги"""
        self.__balance -= self.__balance
        return self.__balance


# код для проверки 
account = BankAccount(1000)
print(account.balance)  # 1000

account.deposit(500)
print(account.balance)  # 1500

account.withdraw(200)
print(account.balance)  # 1300

account.close()
print(account.balance)  # 0
