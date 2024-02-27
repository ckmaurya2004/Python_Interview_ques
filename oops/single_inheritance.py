class person:
    name = 'rohan'

class Employee(person):
    def printDetail(self):
        self.name ='kiran'
        print(self.name)

emp = Employee()
print(emp.name)
emp.printDetail()