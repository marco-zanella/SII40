from sensors.abstract_sensor import AbstractSensor

class Faulty(AbstractSensor):
    def __init__(self, identifier, condition, sensor1, sensor2, delay_generator = None):
        super().__init__(identifier, delay_generator)
        self.condition = condition
        self.sensor1 = sensor1
        self.sensor2 = sensor2

    def measure(self):
        return self.sensor1.measure() if self.condition() else self.sensor2.measure()
