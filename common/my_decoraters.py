import datetime
import inspect
from datetime import datetime
from functools import wraps


def log(func):
    """
    Декаратор log записывает в файл debug.log
    информацию о времени вызова функции, ее параметрах, а так же
    информацию о том из какой функции она была вызвана.
    :param func:
    """
    @wraps(func)
    def log_write(*args, **kwargs):
        spam_func = inspect.stack()[1][3]
        with open('debug.log', 'a') as f_n:
            f_n.writelines("%s --- Функции %s %s с параметрами: %s, %s\n"
                           % (datetime.now(), func.__name__, ''.join(list('вызвана из функции ' + spam_func)), args, kwargs))

        return func(*args, **kwargs)

    return log_write
