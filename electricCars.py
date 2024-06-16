from carsFactory import CarsFactory

class ElectricCars(CarsFactory):

    def __init__(self):
        self._paintColor: None

    def addBody(self):
        print("Method addBody from Electric")

    def addDoors(self):
        print("Method addDoors from Electric")

    def paint(self, color):
        self._paintColor = color
        print(f"sedan painted, color: {self._paintColor}")
