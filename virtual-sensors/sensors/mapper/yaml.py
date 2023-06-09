import sys
import yaml
from sensors.random import Random
from sensors.faulty import Faulty
from generators.constant import Constant
from generators.uniform import Uniform
from generators.normal import Normal

class Yaml:
    def __init__(self, path):
        self.path = path
    
    def load(self):
        with open(self.path, "r") as stream:
            return [Yaml.parse_sensor(sensor_data) for sensor_data in yaml.safe_load(stream)]
    
    def parse_sensor(sensor_data):
        match sensor_data["type"]:
            case "random":
                return Random(
                    sensor_data["id"],
                    sensor_data["name"],
                    Yaml.parse_value(sensor_data["value-generator"]),
                    sensor_data["absolute-error"],
                    Yaml.parse_value(sensor_data["delay-generator"])
                )
            case "faulty":
                return Faulty(
                    sensor_data["id"],
                    Yaml.parse_sensor(sensor_data["sensor"]),
                    sensor_data["reliability"],
                    Yaml.parse_value(sensor_data["value-generator"])
                )
            case _:
                sys.exit("Unknown sensor type " + sensor_data["type"])
    
    def parse_value(value_data):
        match value_data["type"]:
            case "constant":
                return Constant(value_data["value"])
            case "uniform":
                return Uniform(value_data["lowerbound"], value_data["upperbound"])
            case "normal":
                return Normal(value_data["mean"], value_data["variance"])
            case _:
                sys.exit("Unknown generator type " + value_data["type"])