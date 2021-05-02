class Dog:
    # self is the object being called
    def __init__(self,name,age):  # special object :  allows us to initialize the objeto, when we call --object_name = Dog()--, this method is called
        self.name = name  # created an attribute
        self.age = age
        print(name)

    def bark(self): # bark is a method of this class
        print("bark")
    
    def add(self,x): 
        return x+1
    def get_age(self):
        print(self.age)
    def set_age(self,age):
        self.age = age
 
d1 = Dog("Dog1",2)   # d is a instance of the class Dog
d2 = Dog("Dog2",3)
d1.bark()
a=d1.add(3)

d2.get_age()

d1.set_age(34)
print(d1.age)