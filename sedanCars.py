from carsFactory import CarsFactory

class SedanCars(CarsFactory):

    def __init__(self):
        self._paintColor: None

    def addBody(self):
        print("Method addBody from Sedan")

    def addDoors(self):
        print("Method addDoors from Sedan")

    def paint(self, color):
        self._paintColor = color
        print(f"sedan painted, color: {self._paintColor}")
