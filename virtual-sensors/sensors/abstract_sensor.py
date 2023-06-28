from abc import ABC, abstractmethod
from generators.uniform import Uniform

class AbstractSensor(ABC):
    '''
    A sensor
    :param identifier: Unique identifier of this sensor
    :param is_active: Whether this sensor is active
    :param delay_generator: Generator of delay
    '''
    def __init__(self, identifier, is_active=True, delay_generator=None):
        self.identifier = identifier
        self.is_active = is_active
        self.delay_generator = delay_generator or Uniform(500, 1500)

    @abstractmethod
    def measure(self):
        '''
        Returns a measure
        :returns: A measure
        '''
        pass
