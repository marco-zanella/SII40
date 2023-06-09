from multiprocessing import Process

class WatchersPool:
    def __init__(self, sensors):
        self.sensors = sensors
    
    def watcher_adapter(watcher):
        try:
            watcher.main_loop()
        except KeyboardInterrupt:
            pass
    
    def run(self):
        sensor_processes = []
        for sensor in self.sensors:
            sensor_process = Process(target=WatchersPool.watcher_adapter, args=(sensor,))
            sensor_process.start()
            sensor_processes.append(sensor_process)
        try:
            for sensor_process in sensor_processes:
                sensor_process.join()
        except KeyboardInterrupt:
            for sensor_process in sensor_processes:
                sensor_process.terminate()
                sensor_process.join()