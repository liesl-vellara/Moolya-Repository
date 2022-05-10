# learning about class

# to write the code later, and not add any values, we use Pass

# a class is used to create methods
# some examples of methods are .upper(), .lower() etc
class KoolKids:
    # the contructor for the class KoolKids
    def __init__(self,x, y):
        print("This is the KoolKids project")
        # the constructor will identify which arguments needed to be added to the method
        self.x = x
        self.y = y

    # a function inside a class is called a method
    # forming the method
    def divison(self):
        # self is used because we add methods at the end of an object
        div = self.x/ self.y
        print(div)


# now giving the object name
ob = KoolKids(12, 2)
ob.divison()