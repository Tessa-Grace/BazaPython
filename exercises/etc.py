'''
pets = [
    ('Барсик', 'Маша', 'Петрова', 17),
    ('Джек', 'Галина', 'Лагунова', 45),
    ('Муся', 'Александр', 'Каракулов', 28),
    ('Буся', 'Маша', 'Петрова', 17),
    ('Кира', 'Вова', 'Пухарев', 54),
]

res = {}
for pet, name, sur, age in pets:
    owner = (name, sur, age)
    res.setdefault(owner, []).append(pet)
print(res)

# ИЛИ
result = {}
for pet, *owner in pets:
    result.setdefault(tuple(owner), []).append(pet)

##### 10.4 № 1 #####
res = {}
n = int(input())
for i in range(n):
    key, value = input().split(': ')
    res[key.lower()] = value

m = int(input())
for i in range(m):
    i = input().lower()
    print(res.get(i, 'Не найдено'))

#######

st1 = tuple(c for c in input().lower() if c.isalpha())
st2 = tuple(c for c in input().lower() if c.isalpha())

first = {}
for i in st1:
    first[i] = first.get(i, 0) + 1
print(first)

second = {}
for i in st2:
    second[i] = second.get(i, 0) + 1
print(second)

if first == second:
    print('YES')
else:
    print('NO')

'''
class Graph:
    LIMIT_Y = [0, 10]
    
    def set_data(self, data):
        self.data = data
        
    def draw(self):
        res = (str(i) for i in self.data if self.LIMIT_Y[0] <= i <= self.LIMIT_Y[1])
        print(*res)

graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()
