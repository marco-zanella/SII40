import os
import sys
import configparser
from sensors.mapper.yaml import Yaml as SensorsMapper
from watchers_pool import WatchersPool

# Refactoring
from paho.mqtt.client import Client
from watcher import Watcher
# end refactoring

# Reads command line arguments
config_path = "config.ini"
if len(sys.argv) >= 2:
    config_path = sys.argv[1]
if not os.path.isfile(config_path):
    sys.exit(f"Usage: {sys.argv[0]} <path to config file>")


# Reads configuration and sensors
print(f"Reading configuration from {config_path}...")
config = configparser.ConfigParser()
config.sections()
config.read(config_path)
print("Reading virtual sensors from " + config["Sensors"]["path"] + "...")
sensors_mapper = SensorsMapper(config["Sensors"]["path"])
sensors = sensors_mapper.load()
print(f"Found {len(sensors)} sensors")
active_sensors = [sensor for sensor in sensors_mapper.load() if sensor.is_active]
print(f"Found {len(active_sensors)} active sensors")


# Connects to MQTT server and build watchers
print(f"Connecting to MQTT broker with id {config['MQTT']['id']}...")
client = Client(client_id = config["MQTT"]["id"])
if config["MQTT"]["username"] and config["MQTT"]["password"]:
    client.username_pw_set(config["MQTT"]["username"], config["MQTT"]["password"])
client.connect(config["MQTT"]["host"], port=int(config["MQTT"]["port"]))
watchers = [Watcher(sensor, client, "sensors/" + sensor.identifier) for sensor in active_sensors]


# Spawn processes
print("Starting virtual sensors...")
sensors_pool = WatchersPool(watchers)
sensors_pool.run()
print("Terminating...")
