class animal(object):
    def __init__(self):
        self.str1 = "Pitbull"
class dog(object):
    def __init__(self):
        self.str2 = "WildDog"
class Derived(animal,dog):
    def __init__(self):
        animal.__init__(self)
        dog.__init__(self)
    def printStrs(self):
        print("animal is",self.str1, "\nanimal is",self.str2)
ob = Derived()
ob.printStrs()
#okk up daterd in 22-01-2022