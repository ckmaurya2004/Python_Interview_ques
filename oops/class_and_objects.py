class Employee:
    no_of_leaves = 4
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    
kiran = Employee('kiran',300,'developer')
rita = Employee('rita',400,'designer')
print(kiran.role)
print(Employee.no_of_leaves)
