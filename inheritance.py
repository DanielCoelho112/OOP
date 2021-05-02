
# allow us to use a already existent class, and define only the different methods

class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("I dont now what to say")

class Dog(Pet):  # I am using the upper class Pet
    def speak(self):
        print("bark")

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age) # supper stands the class that we inherit from
        self.color = color
    def speak(self):
        print("meow")
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Fish(Pet):
    pass


# Dog and Pet are the child classes, their methods are low methods, the Pet methods are up methdos


p = Pet('tim',19)
p.show()

c = Cat('bill',34,'red')
c.show()  # c inherite the methods of the class Pet
c.speak()

d = Dog("nikk",11)
d.speak()

f =Fish("bubbles",2)
f.speak()