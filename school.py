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

    def __str__(self):
        return f"{self.name} works as a {self.position} in the {self.department} department."
    #Should Return: NAME works as a POSITION in the DEPARTMENT department. 