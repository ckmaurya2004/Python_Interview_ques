class Employee:
    no_of_leaves = 4
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def func_dash(cls,string):
        return cls(* string.split('-'))
    
    @staticmethod
    def printgood():
        print("this is a static method")

kiran = Employee('kiran',300,'developer')
rita = Employee('rita',400,'designer')
ruchi = Employee.func_dash('ruchi-200-students')
print(kiran.role)
kiran.change_leaves(10)
print(Employee.no_of_leaves)
print(ruchi.name)
ruchi.printgood()
