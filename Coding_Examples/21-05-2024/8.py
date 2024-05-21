"""Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 
"""

class Circle(object):
    @staticmethod
    def area_of_circle(r):
        area = 3.14*r**2
        print(area)

circleObj = Circle()
circleObj.area_of_circle(4)

print('-'*100)

class Circle_1(object):
    def __init__(self,r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
cir_obj = Circle_1(4)
print(cir_obj.area())