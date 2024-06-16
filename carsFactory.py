from abc import ABC, abstractmethod

class CarsFactory(ABC):

    @abstractmethod
    def addBody(self):
        pass

    @abstractmethod
    def addDoors(self):
        pass

    @abstractmethod
    def paint(self):
        pass
    