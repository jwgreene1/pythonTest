from voluptuous import Schema, Required, All, Length, Range

schema = Schema({
    Required('segments'): [],
    Required('x1'): All(int, Range(min=-128, max=128)),
    Required('y1'): All(int, Range(min=-128, max=128)),
    Required('z1'): All(int, Range(min=-128, max=128)),
    Required('x2'): All(int, Range(min=-128, max=128)),
    Required('y2'): All(int, Range(min=-128, max=128)),
    Required('z2'): All(int, Range(min=-128, max=128)),
    Required('blockType'): All(int, Range(min=0, max=128)),
    Required('blockData'): All(int, Range(min=0, max=128))

})

class validate:

    def __init__(self):
        print("New validate")

    def validateData(self, data):
        schema(data)
