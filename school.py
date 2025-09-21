class Person:
    def __init__(self, name: str, age: int, country: str):
        self.name = name
        self.age = age
        self.country = country

    def __str__(self):
        return f"{self.name} is {self.age} years old and is from {self.country}."
        #Should Return NAME is AGE and is from COUNTRY

class Student(Person):
    # Delete pass and add your code here
    pass

class Staff(Person):
    # Delete pass and add your code here
    pass