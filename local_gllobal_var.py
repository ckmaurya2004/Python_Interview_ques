x=5
def f1():
    x =10 # local variable
    print(x)
f1()
print(x)


x=5
def f2():
    global x
    x =10 # global variable
    print(x)
f2()
print(x)

x=5
def func():
    x =10 # local variable
    d =globals() # return a dictionary
    d['x'] = 100
    print(x,d['x'])
func()
print(x)
