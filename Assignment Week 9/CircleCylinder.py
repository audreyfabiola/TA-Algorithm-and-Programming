from math import pi

class Circle:
    def __init__(self, radius = 1.0, color = "red"):
        self.__radius = radius
        self.__color = color

    def getRadius(self):
        return self.__radius 

    def setRadius(self, radius):
        self.__radius = radius

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def toString(self):
        return f"Radius: {self.getRadius()}, Color: {self.getColor()}"

    def getArea(self):
        return (self.getRadius() ** 2) * pi
    
class Cylinder(Circle):
    def __init__(self, radius, color, height = 1.0):
        super().__init__(radius, color)
        self.__height = height

    def getHeight(self):
        return self.__height 
    
    def setHeight(self, height):
        self.__height = height
    
    def toString(self):
        return f"Radius: {self.getRadius()}, Color = {self.getColor()}, Height: {self.getHeight()}"

    def getVolume(self):
        return self.getArea() * self.getHeight()



    