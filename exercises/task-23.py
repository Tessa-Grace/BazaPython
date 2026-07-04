def cycle(ls, k):
    """
    Повернуть список вправо на K шагов.

    Дан список и число K. Нужно циклически сдвинуть вправо на K шагов.
    """
    for i in range(k):
        last = ls.pop()
        ls.insert(0, last)
    print(ls)

ls = list(map(int, input().split()))
k = int(input())
cycle(ls, k)