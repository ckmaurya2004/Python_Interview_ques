# 1 function is object
#
# def outer():
#     print("I am outer func ")
#
# new_outer = outer
# new_outer()

# 2 nested function

# def outer():
#     print(" I am outer function ")
#     def inner():
#         print("I am inner function")
#     return  inner()
#
# outer()

# 3 aliasing function
#
# def outer():
#     print(" I am outer function ")
#     def inner():
#         print("I am inner function")
#     return  inner
#
# out=outer() # make alias
# out()

# 4 closures in python

def outer():
    print(" I am outer function ")
    def inner():
        x = 300
        print("I am inner function")
        return x
    return  inner

inner = outer()
print(inner())



