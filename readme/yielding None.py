# some_iterable = ('a','b')

# def some_func(val):
#     return "something"

# print([x  for x in some_iterable]) # ['a', 'b']
# print([(yield x) for x in some_iterable])
    

def some_func(x):
    if x==3:
        return ["wtf"]
    else:
        for i in range(x): # yield from range(x)
            yield i         #

print(list(some_func(3)))