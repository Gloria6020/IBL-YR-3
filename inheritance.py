from typing import Self


class Firstname:
    def __init__(self, name):
        if not name:
            raise ValueError("NO name specified")
        self.name=name
        
class Student(Firstname):
    def__init__(self, name, course):
    super().__init__(name)
    Self.course = course
        
student = students("gloo","information science")
print(student)
    