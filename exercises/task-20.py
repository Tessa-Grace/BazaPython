class Rectangle:
    """
    Класс Прямоугольник

    Условие: Создайте класс Rectangle, который:
    1. Принимает width и height
    2. Имеет метод area() - возвращает площадь
    3. Имеет метод perimeter() - возвращает периметр

    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(width, height):
        """ Возвращает площадь"""
        return width * height

    def perimeter(width, height):
        """ Возвращает периметр"""
        return 2 * (width + height)

width, height = int(input()), int(input())
rect_area = Rectangle.area(width, height)
rect_perimeter = Rectangle.perimeter(width, height)
print(f'Площадь равна: {rect_area}')
print(f'Периметр равен: {rect_perimeter}')