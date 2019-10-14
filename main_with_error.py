from Car import Car
from ElectroMotor import ElectroMotor
from DieselMotor import DieselMotor
from NotAMotor import NotAMotor

if __name__ == "__main__":
    electricMotor = ElectroMotor()
    dieselMotor = DieselMotor()
    notAMotor = NotAMotor()

    electricCar = Car(electricMotor)
    electricCar.drive()

    dieselCar = Car(dieselMotor)
    dieselCar.drive()

    notWorkingcar = Car(notAMotor)
    notWorkingcar.drive() #throws error