from IMotor import IMotor

class ElectroMotor(IMotor):
    def startEngine(self):
        print("starting electric engine")
    
    def stopEngine(self):
        print("stopping electric engine")

    