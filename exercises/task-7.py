"""
Найдите все дубликаты в списке, используя множества
"""
def find_dublicates(numbers):
    unique = set()
    dublicates = set()
    for i in numbers:
        if i in unique:
            dublicates.add(i)
        else:
            unique.add(i)
    return list(dublicates)

dupes = find_dublicates(list(map(int, input().split())))
print(f'Дубликаты: {dupes}')
# 