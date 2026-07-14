import time
from functools import wraps


def retry(attempts):
    """
    retry- декоратор
    
    В случае любой ошибки ждет 1 секунду и пробует еще 1 раз запустить функцию.
    Можно добавить кол-во попыток.
    После каждой неудачи sleep * 1.5
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = 1
            for attempt in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == attempt - 1:
                        raise
                    time.sleep(delay)
                    delay = delay * 1.5
        return wrapper
    return decorator
