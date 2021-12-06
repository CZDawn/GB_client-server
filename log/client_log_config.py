import sys
import os
import logging
sys.path.append('../')
from common.variables import LOGGING_LEVEL

FORMATTER = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)s %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'client.log')

LOG_FILE = logging.FileHandler(PATH, encoding='utf8')
LOG_FILE.setFormatter(FORMATTER)

LOGGER = logging.getLogger('client')
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)


if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')
