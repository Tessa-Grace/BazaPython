'''
Условие: Запись последовательности чисел в файл.
Напишите функцию save_numbers(filename, n), которая 
записывает в файл все числа от 1 до n включительно.
Каждое число должно находиться на новой строке.
'''

def save_numbers(filename, n):
    with open(filename, 'w', encoding='utf-8') as output:
        print(*range(1, n + 1), sep='\n', file=output)

file = input()
number = int(input())
save_numbers(file, number)
