def round_result(num):
    """
    Декоратор для округления.

    Условие: Создайте декоратор round_result, который
    принимает кол-во знаков после запятой и округляет
    результат функции до указанного кол-ва знаков.
    """
    
    def decorator(func):
        def num_round(a, b):
            res = func(a, b)
            return round(res, num)
        return num_round
    return decorator


@round_result(3)
def divide(a, b):
    return a / b

print(divide(10, 3))