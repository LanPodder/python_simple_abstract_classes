from IMotor import IMotor

class DieselMotor(IMotor):
    def startEngine(self):
        print("starting diesel engine")
    
    def stopEngine(self):
        print("stopping diesel engine")

    