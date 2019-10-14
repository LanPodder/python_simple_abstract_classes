from Car import Car
from ElectroMotor import ElectroMotor
from DieselMotor import DieselMotor
from TurboChargedGasolineMotor import TurboChargedGasolineMotor

if __name__ == "__main__":
    electricMotor = ElectroMotor()
    dieselMotor = DieselMotor()

    electricCar = Car(electricMotor)
    electricCar.drive()

    dieselCar = Car(dieselMotor)
    dieselCar.drive()

    turboChargedMotor = TurboChargedGasolineMotor()

    gasolineCar = Car(turboChargedMotor)
    gasolineCar.drive()

    #turboChargedMotor.turbocharge() #works aswell, no type definition