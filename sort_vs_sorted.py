"""
 1.
   sort is the method  of list
   sorted is a build-in function that apply all iterable type objects (list.tuple,set,dictionary,string)

 
"""
list = [2,7,3,78,3,1]
list.sort()
print(list)

 # sorted and sort alwayes give output list formate

string = "kiran"
print(sorted(string))

tuple = 2,6,8,9,4
print(sorted(tuple))


"""
    sort() modified original list 
    returns None
    sorted() not modified original object 
    returns new object


"""


l1 = [4,7,3,9]
print(l1.sort()) # None

set = {2,5,7,3,5,1}
print(sorted(set))

"""
sorted()
reverse : Boolean value indicating bydefault False
key: function/expression with certain logic

"""

# add = lambda x: x*x

list_sorted = [4,7,3,9,1,0,1,67,54]
print(sorted(list_sorted, reverse=True))