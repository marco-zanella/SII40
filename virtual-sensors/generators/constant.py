import random
from generators.abstract_generator import AbstractGenerator

class Constant(AbstractGenerator):
    '''
    A constant value generator
    :param value: Constant value to generate
    '''
    def __init__(self, value=1.0):
        self.value = value

    def generate(self):
        '''
        Returns the constant value
        :returns: The constant value
        '''
        return self.value
