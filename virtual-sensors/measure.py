from time import time

class Measure:
    def __init__(self, name, value=None, absolute_error=0.0, timestamp=None):
        self.name = name
        self.value = value
        self.absolute_error = absolute_error
        self.timestamp = timestamp or time()
