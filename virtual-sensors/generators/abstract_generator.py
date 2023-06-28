from abc import ABC, abstractmethod

class AbstractGenerator(ABC):
    '''
    A generator for values
    '''
    @abstractmethod
    def generate(self):
        '''
        Generates a vaule
        :returns: A new value
        '''
        pass
