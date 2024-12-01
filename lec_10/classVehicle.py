from vehicle import vehicle

class car(vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model) 
        self.doors = doors
    def display(self):
        return f"{super().display()} , Doors: {self.doors}"
    
class plane(vehicle):
    def __init__(self, make, model, wings):
        super().__init__(make, model)
        self.wings = wings
    def display(self):
        return f"{super().display()}, the lenght of wings: {self.wings} meters"
    
class boat(vehicle):
    def __init__(self, make, model,lenght):
        super().__init__(make, model)
        self.lenght = lenght
    def display(self):
        return f"{super().display()} , the lenght of the boat {self.lenght} meters"
    
class raceCar(car):
    def __init__(self, make, model, doors, topSpeed):
        super().__init__(make, model, doors)
        self.topSpeed = topSpeed
    def display(self):
        return f"{super().display()}, the top speed is {self.topSpeed} km/h"
    
if __name__ == "__main__":

    car = car("BMW", "x7", 4)
    print("\ncar", car.display())

    plane = plane("Boeing", "740", 60)
    print ("\nplane" , plane.display())

    boat = boat("Yamaha","example model", 20)
    print("\nboat", boat.display())

    raceCar = raceCar("Ferrari", "F1",2,350)
    print("\nrace car", raceCar.display())