from carsFactory import CarsFactory

class Pickup(CarsFactory):

    def __init__(self):
        self._paintColor: None

    def addBody(self):
        print("Method addBody from Pickup")

    def addDoors(self):
        print("Method addDoors from Pickup")

    def paint(self, color):
        self._paintColor = color
        print(f"sedan painted, color: {self._paintColor}")