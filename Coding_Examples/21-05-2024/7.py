"""Define a class named American which has a static method called printNationality.
"""

class American(object):
    @staticmethod
    def printNationality():
        print("American")

anAmerican = American()        # objectcreation
anAmerican.printNationality()  # this will not run if @staticmethod does not decorates the function.
# American.printNationality()  # this will run even though the @staticmethod does not decorate printNationality()