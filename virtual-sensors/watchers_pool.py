from multiprocessing import Process

class WatchersPool:
    '''
    A set of concurrent watches
    :param sensors: List og sensors to simulate
    '''
    def __init__(self, sensors):
        self.sensors = sensors
    
    def watcher_adapter(watcher):
        '''
        Starts a watcher
        :param watcher: watcher to start
        '''
        try:
            watcher.main_loop()
        except KeyboardInterrupt:
            pass
    
    def run(self):
        '''
        Concurrently run set of sensors
        '''
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