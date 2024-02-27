class SomeClass:
    some_var = 15
    some_list = [5]
    another_list = [5]
    def __init__(self,x):
        self.some_var = x+1 # reasign  [5, 510]
        self.some_list =self.some_list+[x] # increment  [5, 420, 500, 510]
        self.another_list+=[x]

some_obj = SomeClass(420)
print(some_obj.some_var)
print(some_obj.some_list)
print(some_obj.another_list)

another_obj = SomeClass(500)
print(another_obj.some_var)
print(another_obj.some_list)
print(another_obj.another_list)


new_another_obj = SomeClass(510)
print(new_another_obj.some_var)
print(new_another_obj.some_list)
print(new_another_obj.another_list)
