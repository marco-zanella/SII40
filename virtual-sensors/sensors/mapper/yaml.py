import sys
import yaml
from sensors.random import Random
from sensors.faulty import Faulty
from generators.constant import Constant
from generators.uniform import Uniform
from generators.normal import Normal

class Yaml:
    '''
    Read sensors from a YAML file
    :params path: Path of the YAML file
    '''
    def __init__(self, path):
        self.path = path
    
    def load(self):
        '''
        Reads sensors
        :returns: List of sensors
        '''
        with open(self.path, "r") as stream:
            return [Yaml.parse_sensor(sensor_data) for sensor_data in yaml.safe_load(stream)]
    
    def parse_sensor(sensor_data):
        '''
        Converts data into a sensor
        :param sensor_data: Content of the YAML file
        :returns: A sensor
        '''
        match sensor_data["type"]:
            case "random":
                return Random(
                    sensor_data["id"],
                    sensor_data["active"],
                    sensor_data["name"],
                    Yaml.parse_value(sensor_data["value-generator"]),
                    sensor_data["absolute-error"],
                    Yaml.parse_value(sensor_data["delay-generator"])
                )
            case "faulty":
                return Faulty(
                    sensor_data["id"],
                    sensor_data["active"],
                    Yaml.parse_sensor(sensor_data["sensor"]),
                    sensor_data["reliability"],
                    Yaml.parse_value(sensor_data["value-generator"])
                )
            case _:
                sys.exit("Unknown sensor type " + sensor_data["type"])
    
    def parse_value(value_data):
        '''
        Reads a generator
        :param value_data: Content of the YAML file
        :returns: A generator
        '''
        match value_data["type"]:
            case "constant":
                return Constant(value_data["value"])
            case "uniform":
                return Uniform(value_data["lowerbound"], value_data["upperbound"])
            case "normal":
                return Normal(value_data["mean"], value_data["variance"])
            case _:
                sys.exit("Unknown generator type " + value_data["type"])