from sensors.abstract_sensor import AbstractSensor

class Faulty(AbstractSensor):
    '''
    A composite sensor which behaves differently depending on a condition
    :param condition: Condition to evaluate
    :param sensor1: Behavior when condition is satisfied
    :param sensor2: Behavior when condition is not satisfied
    '''
    def __init__(self, identifier, is_active, condition, sensor1, sensor2, delay_generator = None):
        super().__init__(identifier, is_active, delay_generator)
        self.condition = condition
        self.sensor1 = sensor1
        self.sensor2 = sensor2

    def measure(self):
        '''
        Returns a measure
        :returns: A measure
        '''
        return self.sensor1.measure() if self.condition() else self.sensor2.measure()
