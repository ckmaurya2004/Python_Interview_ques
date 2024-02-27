class Employee:
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def printDetail(self):
        return f"{self.name} ,{self.salary} ,{self.role}"
    
    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self) :
        return f"Employee('{self.name}',{self.salary},'{self.role}')"
    
    def __str__(self):
       return f" The Employee('{self.name}',{self.salary},'{self.role}')"


kiran = Employee('kiran',400,'Developer')
shikha = Employee('shikha',200,'Instructor')
print(kiran+shikha)
print(kiran)