# dic = {'a': 1, 'b': 2, 'c': 3}
# print(dic)
# print(dic.get('c'))
# list1 = list(dic.values())
# print(list1)

# dic = {'a': 1, 'b': 2, 'c': 3}
# for  key in dic:
#     print(key)

# for key in dic.keys():
#     print(type(key))

# for key in dic.values():
#     print(type(key)) #int

# for key in dic.items():
#     print(type(key)) # tuple


# print(dic['c']) #3 
# print(dic.get('b')) #2

# print(dic['d']) # note=> if key does not exist so return KeyError 
# print(dic.get('d')) # note=> if key does not exist so return None 


dic = {'a': 1, 'b': 2, 'c': 3}
dic.update({'d':4})
print(dic)

# print(dic.pop('d'))
# print(dic.popitem())
print(dic)


