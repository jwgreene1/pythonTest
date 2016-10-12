#!/usr/bin/python

import time
import logging
import json
from pprint import pprint

# Create logger
module_logger = logging.getLogger('driver.modules.subModule1')

class Class1:
    def __init__(self):
        self.logger = logging.getLogger('driver.modules.subModule1.Class1')
        self.logger.info('  Class1.init')

    def readJsonFile(self, filename):
        self.logger.info(u'  subModule1.method1 - Reading JSON file: {0:s}'.format(filename))

        with open(filename) as data_file:
            data = json.load(data_file)

        return data

    def printData(self, data):
        self.logger.info("data: %s", data)

    def parseData(self, data):

        for segment in data.get('segments'):
           print("segment:", segment)

if __name__ == '__main__':
    print('subModule1 called as script')
    module_logger.info('  subModule1 default code')
