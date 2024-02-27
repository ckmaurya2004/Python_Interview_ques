class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname =lname

    def printDetail(self):
        return f"{self.fname},{self.lname}"
    
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email can not set "
        return f"{self.fname}.{self.lname}@gmail.com"
    
    @email.setter
    def email(self,string):
        name = string.split("@")[0]
        self.fname = name.split('.')[0]
        self.lname = name.split('.')[1]

    @ email.deleter
    def email(self):
        self.fname = None
        self.lname = None


emp = Employee('kiran','maurya')
print(emp.printDetail())

emp.fname = "ckm"
print(emp.email)

emp.email = 'prabha.maurya@gmail.com'
print(emp.email)

del emp.email

print(emp.email)





        