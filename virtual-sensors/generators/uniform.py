import random
from generators.abstract_generator import AbstractGenerator

class Uniform(AbstractGenerator):
    def __init__(self, lowerbound=0.0, upperbound=1.0):
        self.lowerbound = lowerbound
        self.upperbound = upperbound

    def generate(self):
        return random.uniform(self.lowerbound, self.upperbound)
