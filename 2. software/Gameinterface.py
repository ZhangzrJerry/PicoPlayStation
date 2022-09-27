from abc import ABCMeta,abstractmethod

class Gameinterface(metaclass=ABCMeta): 

    @abstractmethod
    def left(self):
        pass

    @abstractmethod
    def right(self):
        pass
    
    @abstractmethod
    def up(self):
        pass
    
    @abstractmethod
    def down(self):
        pass
    
    @abstractmethod
    def playing(self):
        pass
    