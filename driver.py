#!/usr/bin/python

import sys
import time
import datetime
import logging
import modules.util
from modules.validateData import validateData

# Create the logger
logger = logging.getLogger('driver')

def initialize():

    # Create the logger
    logger.setLevel(logging.DEBUG)

    # Create file handler which logs even debug messages
    fh = logging.FileHandler('logs/driver.log')
    fh.setLevel(logging.DEBUG)

    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)',
                                  '%Y-%m-%d %H:%M:%S')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.info('Logger initialized')

def main():

    initialize()

    logger.info('### Beginning Driver Execution - %s ###' % datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))

    # x = modules.util.fileUtil()

    file = 'data/testWall.json'

    # data = x.readJsonFile(file)
    data = modules.util.readJsonFile(file)

    v = validateData()
    v.validateWall(data)

    logger.info('### Ending Driver Execution - %s ###' % datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    sys.exit(main())
