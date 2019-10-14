from IMotor import IMotor
from ITurbocharge import ITurbocharge

class TurboChargedGasolineMotor(IMotor, ITurbocharge):
    def __init__(self):
        pass

    def turbocharge(self):
        print("turbocharging gasoline motor")

    def startEngine(self):
        print("starting gasoline motor")
        self.turbocharge()

    def stopEngine(self):
        print("stopping gasoline motor")