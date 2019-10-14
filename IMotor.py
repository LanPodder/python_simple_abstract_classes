import abc

class IMotor(abc.ABC):
    @abc.abstractmethod
    def startEngine(self):
        pass

    @abc.abstractmethod
    def stopEngine(self):
        pass

