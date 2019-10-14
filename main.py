from Car import Car
from ElectroMotor import ElectroMotor
from DieselMotor import DieselMotor

if __name__ == "__main__":
    electricMotor = ElectroMotor()
    dieselMotor = DieselMotor()

    electricCar = Car(electricMotor)
    electricCar.drive()

    dieselCar = Car(dieselMotor)
    dieselCar.drive()