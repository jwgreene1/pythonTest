#!/usr/bin/python

import time
import logging
import json
from pprint import pprint

# Create logger
module_logger = logging.getLogger('driver.modules.util')

class fileUtil:
    def __init__(self):
        self.logger = logging.getLogger('driver.modules.util.fileUtil')
        self.logger.info('  Class1.init')

    def readJsonFile(self, filename):
        self.logger.info(u'  util.fileUtil - Reading JSON file: {0:s}'.format(filename))

        with open(filename) as data_file:
            data = json.load(data_file)

        return data

    def printData(self, data):
        self.logger.info("data: %s", data)

    def parseData(self, data):

        for segment in data.get('segments'):
            print("segment:", segment)

if __name__ == '__main__':
    print('util called as script')
    module_logger.info('  util default code')
