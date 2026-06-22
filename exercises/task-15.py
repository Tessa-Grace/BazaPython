def palindrom(st):
    """ Проверка, является ли строка палиндромом"""
    print(st == st[::-1])

palindrom(input())