class Car:
    def __init__(self, motor):
        self.motor = motor

    def drive(self):
        self.motor.startEngine()
        print("driving")
        self.motor.stopEngine()