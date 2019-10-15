#!/usr/bin/env python

import math

class Circle:
    pi = math.pi

    def __str__(self):
        return str(self.area)

    def circle_area(self):
        self.area = self.pi * self.radius * self.radius

    def __init__(self, radius="null", diameter="null"):
        if radius == "null":
          if diameter == "null":
            self.radius = 1.0
            self.diameter = 1.0
          else:
            self.diameter = diameter
            self.radius = diameter / 2.0 
        else:
          self.radius = radius
          self.diameter = 2.0 * self.radius
        self.circle_area()

    def setDiameter(self, setdiameter):
        self.diameter = setdiameter
        self.radius = setdiameter / 2.0
        self.circle_area()

    def getArea(self):
        return self.area

    def printAll(self):
        print( "Area of this circle is ", self.getArea() )
        print( "Radius of this circle is ", self.radius )
        print( "Diameter of this circle is ", self.diameter )
