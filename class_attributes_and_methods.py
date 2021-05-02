class Person:
    number_of_people = 0  # class attributes, is defined to the class!!, its de same for all instances

    def __init__(self,name):
        self.name = name
        Person.add_person()
        
    @classmethod # meaning that this method is a class method, class methods acts on the class, and not on the instances
    def number_of_people_(cls):
        return cls.number_of_people # cls is class
    @classmethod
    def add_person(cls):
        cls.number_of_people+=1

    
p1 = Person("tim")
p2 = Person("gil")

print(p1.number_of_people)
print(p2.number_of_people)
#print(Person.number_of_people)

#Person.number_of_people = 9

print(p1.number_of_people)
print(p2.number_of_people)
#print(Person.number_of_people)


print(Person.number_of_people_())