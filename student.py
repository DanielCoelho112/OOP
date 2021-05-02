class Student():
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade # 0 - 100
    
    def get_grade(self):
        return self.grade

class Course():
    def __init__(self,name,max_students):
        self.name = name
        self.max_students=max_students
        self.students = []
    
    def add_student(self,student): # student can be anything, in our case will be other object
        if len(self.students) < self.max_students:
            self.students.append(student)
            print("True")
            return True
        print("False")
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

s1 = Student("Tim",19,95)
s2 = Student("danc",22,100)
s3 = Student("Jane",18,70)

course = Course("science",2)

course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.students) # both are students objects

print(course.students[1].name)

print(course.get_average_grade())