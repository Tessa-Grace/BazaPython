"""
Two Sum
Условие: Дан массив целых чисел nums и целое число target.
Верните индексы двух чисел, сумма которых равна target
"""
def twoSum(nums, target):
    ans = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                ans.append([i, j])
    print(ans)

twoSum(list(map(int, input().split())), int(input()))