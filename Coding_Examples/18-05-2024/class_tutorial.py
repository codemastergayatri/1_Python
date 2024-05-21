class Person(object):                                                       #1
     """A simple class."""                            # docstring           
     species = "Homo Sapiens"                         # class attribute     #2
     def __init__(self, name):                        # special method      #3
         """This is the initializer. It's a special
         method (see below).
         """
         self.name = name                             # instance attribute
     def __str__(self):                               # special method      #4
         """This method is run when Python tries
         to cast the object to a string. Return
         this string when using print(), etc.
         """
         return self.name
     def rename(self, renamed):                       # regular method      #5
         """Reassign and print the name attribute."""
         self.name = renamed
         print("Now my name is {}".format(self.name))

##########################################################################################################################

myobj = Person("gayatri")                                                   #6
myobj.__init__("gayatri")
myobj.__str__()
myobj.rename("gayatri")                                                     #7