"""
Условие: Удалите повторяющиеся слова из предложения, 
сохраняя порядок первого появления.

"""
def remove_dublicate_words(line):
    normal = []
    for i in line:
        if i not in normal:
            normal.append(i)
    return ' '.join(normal)

line = remove_dublicate_words(input().split())
print(line)