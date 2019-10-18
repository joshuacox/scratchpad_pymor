#!/usr/bin/env python

import math

class Circle(object):
    pi = math.pi

    def __repr__(self):
        return f'Circle(self.radius)'

    def circle_area(self):
        self.area = self.pi * self.radius * self.radius

    def __init__(self, radius=1):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    def printAll(self):
        print( "Area of this circle is ", self.area )
        print( "Radius of this circle is ", self.radius )
        print( "Diameter of this circle is ", self.diameter )
