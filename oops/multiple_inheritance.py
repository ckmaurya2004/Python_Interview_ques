class Employee:
    def __init__(self,name,salary,role) :
        self.name = name
        self.salary = salary
        self.role = role

    def printEmpDetail(self):
        print(f" The  Employee name is {self.name} and salary {self.salary} and role is {self.role}")

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    def printStuDetail(self):
        print(f"The students name is {self.name } and age is {self.age}")


class Person(Employee,Student):
    def personInfo(self):
        print("THis is person class")


amit = Person('amit',3000,'developer')
amit.printEmpDetail()
