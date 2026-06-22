from re import *

def password(st):
    """
    Проверка пароля.

    1. >= 8 символов
    2. Хотя бы одна заглавная буква
    3. Хотя бы одна строчная буква
    4. Хотя бы одна цифра
    """
    
    if len(st) < 8:
        return False
    if not search(r'[A-Z]', st):
        return False
    if not search(r'[a-z]', st):
        return False
    if not search(r'[0-9]', st):
        return False
    return True

print(password(input()))