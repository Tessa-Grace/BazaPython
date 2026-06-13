
def hello_decorator(func):
    """
    'Привет!' вначале.

    Условие: Создайте декоратор hello_decorator,
    который перед вызовом функции выводит строку 'Привет!'.
    """
    def hello():
        print('Привет!')
        func()
    return hello

@hello_decorator
def say_name():
    print('Меня зовут ...')

say_name()