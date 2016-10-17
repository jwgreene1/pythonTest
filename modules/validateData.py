import logging
from voluptuous import Schema, Required as req, All, Length, Range, error, Any

# Create logger
module_logger = logging.getLogger('driver.modules.validateData')

schemaWallSegment = ({
    req('x1'): All(int, Range(min=-128, max=128)),
    req('y1'): All(int, Range(min=-128, max=128)),
    req('z1'): All(int, Range(min=-128, max=128)),
    req('x2'): All(int, Range(min=-128, max=128)),
    req('y2'): All(int, Range(min=-128, max=128)),
    req('z2'): All(int, Range(min=-128, max=128)),
    req('blockType'): All(int, Range(min=0, max=128)),
    req('blockData'): All(int, Range(min=0, max=10))
})

schemaWall = Schema({
    req('segments'): [schemaWallSegment],
    req('direction'): Any('N', 'S', 'E', 'W')
})


class validateData:

    def __init__(self):
        self.logger = logging.getLogger('driver.modules.validateData.validateData')
        self.logger.info('  validateData.init')

    def validateWall(self, data):
        try:
            print('  validating schemaWall: ', schemaWall(data))
            self.logger.info('  validating schemaWall: ', schemaWall(data))

        except error.MultipleInvalid as e:
            print('Error validating wall data: ', e)
            self.logger.error('Error validating wall data: ', e)
