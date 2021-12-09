import sys
import inspect
import logging
# Import logging config
from logs import utils_log_config, server_log_config, client_log_config

if sys.argv[0].find('client'):
    LOG = logging.getLogger('client_logger')
elif sys.argv[0].find('server'):
    LOG = logging.getLogger('server_logger')
else:
    LOG = logging.getLogger('utils_logger')


def log_deco(func):
    def decorated(*args, **kwargs):
        result = func(*args, **kwargs)
        frame = inspect.currentframe()
        LOG.debug(
            f'FUNCTION: {func.__name__};\n'
            f'Парраметры функции - ({args}, {kwargs})\n'
            f'Вызвана функцией: {inspect.getouterframes(frame)[-1][-2][0].split()}\n'
            f'Модуль из которого вызвана функция: {inspect.getouterframes(frame)[-1][1].split("/")[-1]}\n')
        return result
    return decorated

