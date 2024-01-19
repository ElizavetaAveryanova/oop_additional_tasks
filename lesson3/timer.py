"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
import time

class Timer:
    def __enter__(self):
        """Магический метод, который запускает таймер"""
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Магический метод, который останавливает таймер
        и выводит время выполнения блока кода"""
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f'Execution time:{elapsed_time}')


with Timer() as timer:
    time.sleep(7)


