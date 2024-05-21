"""Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 
"""

class rectangle(object):
    def __init__(self,l,w):
        self.lenght = l
        self.width = w

    def area(self):
        return self.lenght * self.width
    
rect_obj = rectangle(12,21)
print(rect_obj.area())
