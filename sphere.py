"""Write a program that takes the radius of a sphere (a floating-point number) as input
   and outputs the sphere's diameter, circumference, surface area and volume."""

from math import pi

class Sphere:
    def __init__(self, radius):
        self.radius = float(radius)

    def getDiameter(self): 
        self.diameter = self.radius * 2
        return self.diameter     

    def getCircumference(self):
        self.circumference = 2 * pi * self.radius
        return self.circumference

    def getArea(self):
        self.area = 4 * pi * self.radius ** 2
        return self.area

    def getVolume(self):
        self.volume = 4/3 * pi * self.radius ** 3
        return self.volume 


