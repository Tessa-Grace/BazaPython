def length(numbers):
    """
    Найти кол-во положительных чисел.

    Дан список чисел. Нужно посчитать, 
    сколько в списке положительных чисел
    """
    pos = [i for i in numbers if i > 0]
    return len(pos)

res = length(list(map(int, input().split())))
print(res)