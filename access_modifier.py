

class Employee:
    _fname = 'kiran'
    __lname = "maurya"
    def __init__(self):
        self.name = "kiran maurya"

emp1 = Employee()
print(emp1.name)
print(emp1._fname)
print(emp1._Employee__lname)  # name mingling













