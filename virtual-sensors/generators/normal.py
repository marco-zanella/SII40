import random
from generators.abstract_generator import AbstractGenerator

class Normal(AbstractGenerator):
    def __init__(self, mean=0.0, variance=1.0):
        self.mean = mean
        self.variance = variance

    def generate(self):
        return random.gauss(self.mean, self.variance)
