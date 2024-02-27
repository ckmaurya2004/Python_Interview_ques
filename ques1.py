# str1 = "sky is blue" # blue is sky
# ls = str1.split()
# print(ls)
# ls1 = ls[::-1]
# print(ls1)
# print(" ".join(ls1))

#   or
# print(" ".join(str1.split()[::-1]))


# list = [1,2,2,3,3,4,5,5,6,6,] # [1,4]
# new_list = []
# for item in list:
#     if list.count(item) == 1:
#         new_list.append(item)
# print(new_list)

# or 

# print([item for item in list if list.count(item) == 1])


mystr = "a,a,a,b,b,c,c,c" # a:3,b:2,c:3

mylist = mystr.split(",")

# visited = []
# for ch in mylist:
#     if ch not in visited:
#         print(f"{ch}:{mylist.count(ch)}",end=",")
#         visited.append(ch)

#   or

visited = []
final_list = []
for ch in mylist:
    if ch not in visited:
        final_list.append(f"{ch}:{mylist.count(ch)}")
        visited.append(ch)
# print(final_list)
print(",".join(final_list))

