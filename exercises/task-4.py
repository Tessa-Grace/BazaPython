"""
Задача 4: Поиск всех индексов элемента.
Условие: Найдите все индексы заданного элемента в списке.
"""
def find_indexes(ls, element):
    ans = []
    for i in range(len(ls)):
        if ls[i] == element:
            ans.append(i)
    print(ans)

find_indexes(list(map(int, input().split())), int(input()))