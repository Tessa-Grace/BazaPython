"""
Задача 2: Вывести четные числа
Напишите функцию, которая принимает число N и выводит все четные числа от 1 до N (вкл)
"""
def even_number(num):
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i)

even_number(int(input()))