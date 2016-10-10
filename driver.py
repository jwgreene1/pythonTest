#!/usr/bin/python

import sys
import time
import datetime
import logging
import modules.subModule1

# Create the logger
logger = logging.getLogger('driver')

def initialize():

    print "    In initialize"

    # Create the logger
    logger.setLevel(logging.DEBUG)

    # Create file handler which logs even debug messages
    fh = logging.FileHandler('logs/driver.log')
    fh.setLevel(logging.DEBUG)

    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)", "%Y-%m-%d %H:%M:%S")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.info('Logger initialized')

    print "    Leaving initialize"

def main():

    print "  In main"

    initialize()

    logger.info("### Beginning Driver Execution - %s ###" %datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))

    print "  Instantiating Class1"
    x = modules.subModule1.Class1()
    print "  Class1 Done"
    x.method1()

    logger.info("### Ending Driver Execution - %s ###" %datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))

    print "  Leaving main"

if __name__ == "__main__":
    print "Calling main"
    main()
    print "main finished"
