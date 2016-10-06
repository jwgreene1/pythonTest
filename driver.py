#!/usr/bin/python

import sys
import time
import datetime
import logging
#import modules.subModule1
from modules.subModule1 import Class1
#from modules import *

# Create the logger
logger = logging.getLogger('driver')

def initialize():

    print "\t\tIn initialize"

    # Create the logger
    logger.setLevel(logging.DEBUG)

    # Create file handler which logs even debug messages
    fh = logging.FileHandler('logs/driver.log')
    fh.setLevel(logging.DEBUG)

    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.info('Logger initialized')

    print "\t\tLeaving initialize"

def main():

    print "\tIn main"

    initialize()

    logger.info("### Beginning Driver Execution - %s ###" %datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))

    print "\tInstantiating Class1"
    x = Class1()
    print "\tClass1 Done"
    x.method1()

    logger.info("### Ending Driver Execution - %s ###" %datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))

    print "\tLeaving main"

if __name__ == "__main__":
    print "Calling main"
    main()
    print "main finished"
