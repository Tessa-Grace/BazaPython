def brackets(line):
    """
    Проверка сбалансированных скобок

    Условие: Дана строка, состоящая из символов: ()[]{}
    Нужно проверить, являются ли скобки корректно сбалансированными.
    Правила:
    1. Каждая открывающая скобка должна иметь соответствующую закрывающую
    2. Скобки должны закрываться в правильном порядке
    """

    sp = []
    for i in line:
        if i in '([{':
            sp.append(i)
        else:
            if len(sp) == 0: return False
            top = sp.pop()
            if (top == '(' and i != ')') or \
                (top == '[' and i != ']') or \
                    (top == '{' and i != '}'):
                    return False
    return len(sp) == 0
    

res = brackets(input())
print(res)