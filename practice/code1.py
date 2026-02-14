import math
class shape:
    def area(self,length = None,breath = None,radius = None):
        if radius is not None:
            return math.pi * (radius ** 2)
        else:
            return length * breath
rectange = shape()
print(rectange.area(5,7))
print(rectange.area(radius = 2.5))