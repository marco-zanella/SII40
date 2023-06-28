import random
from generators.abstract_generator import AbstractGenerator

class Uniform(AbstractGenerator):
    '''
    Generates values from a uniform distribution
    :param lowerbound: Lowerbound of the distribution
    :param upperbound: Upperbound of the distrbution
    '''
    def __init__(self, lowerbound=0.0, upperbound=1.0):
        self.lowerbound = lowerbound
        self.upperbound = upperbound

    def generate(self):
        '''
        Returns a random value from a uniform distribution
        :returns: A random value
        '''
        return random.uniform(self.lowerbound, self.upperbound)
