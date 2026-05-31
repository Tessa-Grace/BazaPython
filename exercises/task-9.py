"""
Условие: Создайте функцию, которая оставляет только элементы,
встречающиеся ровно один раз
"""
def keep_unique_only(numbers):
    ans = []
    for i in range(len(numbers)):
        if numbers.count(numbers[i]) == 1:
            ans.append(numbers[i])
    return ans

unique_only = keep_unique_only(list(map(int, input().split())))
print(unique_only)