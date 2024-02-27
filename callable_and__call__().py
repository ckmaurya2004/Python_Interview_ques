# every function and class is callable

# def func(a,b):
#     return a+b


# add = lambda x,y: x+y
# print(func(3,6))
# print(add(3,9))
# print(callable(func)) # True
# print(callable(add)) # True



# class Employee:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

# e1 = Employee(3,4)

# print(callable(Employee)) # True

# print(callable(e1)) # False


# Note => if you want to make e1 object to callable then __call__() define within class body



class Employee:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __call__(self):
        print(" Hello I am call method")


e1 = Employee(3,4)

print(callable(e1)) # True
e1() #  Hello I am call method
