class Figure:
    """
    Возвращает площадь прямоугольника.

    Условие: Создайте базовый класс Figure и класс Rectangle,
    который наследуется от него. В классе Rectangle реализуйте метод area(),
    возвращающий площадь прямоугольника.
    """

    def __init__(self, width, length):
        self.width = width
        self.length = length

class Rectangle(Figure):
    def area(self):
        return self.width * self.length

rectangle = Rectangle(5, 3)
print(rectangle.area())
