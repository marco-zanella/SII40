from time import time

class Measure:
    '''
    A measure
    :param name: Name of this measure
    :param value: Value of this measure
    :param absolute_error: Absolute error of this measure
    :param timestamp: Generation timestamp of this measure
    '''
    def __init__(self, name, value=None, absolute_error=0.0, timestamp=None):
        self.name = name
        self.value = value
        self.absolute_error = absolute_error
        self.timestamp = timestamp or time()
