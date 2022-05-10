


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'{self.name} is only {self.age} years old')

# now creating a class and inhertiting the pet
class Dodge(Pet):
    def sound(self):
        print('bork')

class Cat(Pet):
    # the argument passed in the class will easily inherit the pet's properties
    def sound(self):
        print('ahhhhhhhhhhhhhh')

# now lets try this
mischief = Dodge("Mischief", "9")
pubs = Cat("Pubs", "1")

mischief.sound()
