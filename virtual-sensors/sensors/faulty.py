import random
from sensors.abstract_sensor import AbstractSensor
from generators.abstract_generator import AbstractGenerator
from generators.constant import Constant

class Faulty(AbstractSensor):
    '''
    A sensor which may output a wrong value
    :param sensor: Actual sensor
    :param reliability: Probability of the sensor of producing the correct value
    :param value_generator: Generator of wrong values
    '''
    def __init__(self, identifier, is_active, sensor, reliability=0.8, value_generator=None):
        super().__init__(identifier, is_active, sensor.delay_generator)
        self.sensor = sensor
        self.reliability = reliability
        self.value_generator = value_generator if isinstance(value_generator, AbstractGenerator) else Constant(value_generator)

    def measure(self):
        '''
        Returns a measure
        :returns: A measure
        '''
        measure = self.sensor.measure()
        if random.random() > self.reliability:
            measure.value = self.value_generator.generate()
        return measure
