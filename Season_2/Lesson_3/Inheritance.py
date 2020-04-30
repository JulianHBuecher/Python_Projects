# Usage of inheritance in classes
# Every single class created inherit from the base class object

class Person():
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print("Hello, " + self.name)
    def __str__(self):
        return self.name

# Class Student inherit from Class Person
class Student(Person):
    def __init__(self, name, school):
        # Derive data from the inherited class
        super().__init__(name)
        self.school = school
    def sing_school_song(self):
        print("Ode to " + self.school)
    def say_hello(self):
        # Let the parent do some work
        # But this is not automatically the case.
        # When we want to call the parent function we have to say this explicitly to the inherited class
        super().say_hello()
        # Add some new functionality
        print("I'm tired!")
    def __str__(self):
        return f"{self.name} attends at {self.school}"

student1 = Student("Julian","Harvard")
student1.say_hello()
student1.sing_school_song()
print(student1)

# Checking of instances
print(f"Is this a student? {isinstance(student1, Student)}")
print(f"Is this student a person? {isinstance(student1, Person)}")
print(f"Is a student a subcalss of person? {issubclass(Student, Person)}")