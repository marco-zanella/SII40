from sensors.abstract_sensor import AbstractSensor
from measure import Measure

class Random(AbstractSensor):
    '''
    Sensor producing values from a given distribution
    :param value_generator: Generator of values
    :param absolute_error: Absolute error of this sensor
    '''
    def __init__(self, identifier, is_active, name, value_generator, absolute_error = 0.5, delay_generator=None):
        super().__init__(identifier, is_active, delay_generator)
        self.name = name
        self.value_generator = value_generator
        self.absolute_error = absolute_error

    def measure(self):
        '''
        Returns a measure
        :returns: A measure
        '''
        return Measure(self.name, self.value_generator.generate(), self.absolute_error)
