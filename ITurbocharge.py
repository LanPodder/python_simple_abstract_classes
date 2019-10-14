import abc

class ITurbocharge(abc.ABC):
    @abc.abstractmethod
    def turbocharge(self):
        pass