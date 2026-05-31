"""
Условие: Создайте матрицу с помощью вложенных list comprehensions
Условие: Транспонируйте матрицу (поменяйте строки и столбцы местами)
"""
matrix = [[i * 3 + j for j in range(1, 4)] for i in range(3)]
transp = [[matrix[j][i] for j in range(3)] for i in range(3)]
print(matrix)
print(transp)