from abc import ABC, abstractmethod
from generators.uniform import Uniform

class AbstractSensor(ABC):
    def __init__(self, identifier, delay_generator=None):
        self.identifier = identifier
        self.delay_generator = delay_generator or Uniform(500, 1500)

    @abstractmethod
    def measure(self):
        pass
