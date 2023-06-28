import random
from generators.abstract_generator import AbstractGenerator

class Normal(AbstractGenerator):
    '''
    Generates values from a normal distribution
    :param mean: Mean of the distribution
    :param variabnce: Variance of the distribution
    '''
    def __init__(self, mean=0.0, variance=1.0):
        self.mean = mean
        self.variance = variance

    def generate(self):
        '''
        Returns a random value from a normal distribution
        :returns: A random value
        '''
        return random.gauss(self.mean, self.variance)
