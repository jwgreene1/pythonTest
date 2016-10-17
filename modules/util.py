#!/usr/bin/python

import logging
import json

# Create logger
module_logger = logging.getLogger('driver.modules.util')


# class fileUtil:
# def __init__(self):
#     self.logger = logging.getLogger('driver.modules.util.fileUtil')
#     self.logger.info('  fileUtil.init')

def readJsonFile(filename):
    module_logger.info(u'  util.fileUtil - Reading JSON file: {0:s}'.format(filename))

    with open(filename) as data_file:
        data = json.load(data_file)

    return data
