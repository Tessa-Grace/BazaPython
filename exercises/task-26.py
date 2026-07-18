def log_call(func):
    def wrapper(num1, num2):
        """
        Декоратор: логирование вызова функции

        Написать декоратор log_call, который:
        - выводит имя функции пеерд вызовом
        - выводит результат после выполнения

        Применить к функции сложения двух чисел
        """
        print(func.__name__)
        res = func(num1, num2)
        print(res)
        return res
    return wrapper

@log_call
def summ(num1, num2):
    return num1 + num2

num1, num2 = int(input()), int(input())
summ(num1, num2)