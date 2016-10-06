#!/usr/bin/python

import time
import logging

# Create logger
module_logger = logging.getLogger('modules.subModule1')

class Class1:
    def __init__(self):
        self.logger = logging.getLogger('modules.subModule1.Class1')
        self.logger.info('\t\tClass1.init')
        print "\t\tClass1.init"
        #x = 1

    def method1(self):
        self.logger.info("\tsubModule1.method1")

module_logger.info("\tsubModule1 default code")

if __name__ == "__main__":
    print "subModule1 called as script"
    module_logger.info("\tsubModule1 default code")
