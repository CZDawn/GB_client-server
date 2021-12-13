import sys
import os
import logging
sys.path.append('../')
from common.veriables import LOGGING_LEVEL

FORMATTER = logging.Formatter('%(asctime)s %(levelname)-10s\n%(filename)s %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'utils.log')

LOG_FILE = logging.FileHandler(PATH, encoding='utf8')
LOG_FILE.setFormatter(FORMATTER)

LOGGER = logging.getLogger('utils_logger')
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)