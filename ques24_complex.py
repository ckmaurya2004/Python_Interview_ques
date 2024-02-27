x = complex((not not not not True),5)
print(x)

#  not True # False
# not False # True
# not  True # False
# not False # True

# complex(True) # 1



list1 = [ 205,508,2670,120,301]
mylist1 = []


for item in list1:
    item = str(item)
    mylist = item.split('0')

    mylist1.append(''.join(mylist))
print(mylist1)


