class StepCounter:
    """
    Счетчик шагов.

    Условие: Создайте класс StepCounter, который моделирует шагомер.
    Требования:

    Атрибуты: 
    - steps

    Методы: 
    - add_steps(amount) - добавляет шаги (если значение < 0,
    то игнорировать и вывести ошибку обычным принтом)
    - reset() - сбрасывает шаги в 0
    - str() - возвращает строку: 'Текущие шаги: {steps}'
    """

    def __init__(self, steps):
        self.steps = steps

    def add_steps(self, amount):
        if amount > 0:
            self.steps += amount
        else:
            print('Ни шагу назад!')

    def reset(self):
        self.steps = 0

    def __str__(self):
        return f'Текущие шаги {self.steps}'

counter = StepCounter(0)
counter.add_steps(500)
counter.add_steps(300)
counter.add_steps(-10)

print(counter)

counter.reset()
print(counter)
    