import random
from generators.abstract_generator import AbstractGenerator

class Constant(AbstractGenerator):
    def __init__(self, value=1.0):
        self.value = value

    def generate(self):
        return self.value
