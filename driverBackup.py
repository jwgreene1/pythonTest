#!/usr/bin/python

import sys
import time
import datetime
import logging as log
#import modules.subModule1
#from modules.subModule1 import Class1
#from modules import *

def initialize():

    print "\t\tIn initialize"

    # Open the log file
    log.basicConfig(filename='logs/driver.log', filemode='w', level=log.DEBUG, format='%(asctime)s %(message)s')

    log.info("Initializing driver")
    # Set some global vars
    # 
    print "\t\tLeaving initialize"

def main():

    print "\tIn main"

    initialize()

    log.info("### Beginning Driver Execution - %s ###" %datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))

    #log.info("sys.path: %s", sys.path)

    print "\tInstantiating Class1"
    #x = Class1()
    print "\tClass1 Done"
    #x.method1()

    log.info("### Ending Driver Execution - %s ###" %datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))

    print "\tLeaving main"

if __name__ == "__main__":
    print "Calling main"
    main()
    print "main finished"
