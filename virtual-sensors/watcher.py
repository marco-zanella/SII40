import time
import json

class Watcher:
    def __init__(self, sensor, client, topic,):
        self.sensor = sensor
        self.client = client
        self.topic = topic

    def main_loop(self, iterations = None):
        step = 0
        while iterations is None or step < iterations:
            measure = self.sensor.measure()
            payload = json.dumps(measure.__dict__)
            self.client.publish(topic = self.topic, payload = payload)
            time.sleep(self.sensor.delay_generator.generate() / 1000.0)
            step += 1
