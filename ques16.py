# input = "a=2&b=23&name=kiran"
# output = {'a': 2, 'b':23,'name':'kiran'}

str1 = "a=2&b=23&name=kiran"
str_list = str1.split('&')
print(str_list)

list =[]
for i in str_list:
    mylist = i.split('=')
    list.append(mylist)
print(dict(list))

