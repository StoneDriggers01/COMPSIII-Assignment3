class Person:
    def __init__(self, name: str, age: int, country: str):
        self.name = name
        self.age = age
        self.country = country

    def __str__(self):
        return f"{self.name} is {self.age} years old and is from {self.country}."
        #Should Return: NAME is AGE and is from COUNTRY.

class Student(Person):
    def __init__(self, name: str, age: int, country: str, major: str, gpa: float):
        super().__init__(name, age, country)
        self.major = major
        self.gpa = gpa
    def study(self):
        return f"{self.name} is studying {self.major} with a current GPA of {self.gpa}."

class Staff(Person):
    def __init__(self, name: str, age: int, country: str, position: str, department: str):
        super().__init__(name, age, country)
        self.position = position
        self.department = department
    def work(self):
        return f"{self.name} works as a {self.position} in the {self.department} department."
    #Should Return: NAME works as a POSITION in the DEPARTMENT department. 

person_1 = Person("Manny", 33, "USA")
student_1 = Student("Tammy", 19, "Vietnam", "Computer Science", 3.54)
staff_1 = Staff("Brittney", 36, "Canada", "Neuroscientist", "Biology")

print("School Info")
print(person_1.__str__())
print(student_1.study())
print(staff_1.work())