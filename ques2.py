# input = "python is easy"
# output = "nohtyp si ysae"

# str1 = input("enter a string: ")
# list = str1.split()
# l1 = []
# for i in list:
#     l1.append((i[::-1]))
# print(l1)
# print(" ".join(l1))


# print duplicate

# input= ['hello',20,5,8,20,5,6,7]
# output = [20,5]

# ls =['hello',20,5,8,20,5,6,7]
# visited = []
# for i in ls:
#     if (ls.count(i)>1) and i not in visited:
#         visited.append(i)
# print(visited)


# write a program  to count number of items having a list as value

data = {'jay':['male',23,2000],'kiran':30,'divya':['female',30],'ram':[20],'sita':[20]}

#  l = [2,4,5]
#  isinstance(l,list)  return True if l is list type other wise return False

# count = 0
# for item in data:
#     if isinstance(data[item],list):
#         count += 1

# print(count)



# write a program to count number of vowels in a string..

str1 = input("enter a string ! ")
count = 0
vowel = ['a','e','i','o','u']

for char in str1:
    if char in vowel:
        count = count + 1
print(count)
