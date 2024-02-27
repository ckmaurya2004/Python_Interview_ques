l1 = [1,2,3,4,7,8]
l2 = [3,6,7,4,3,2]
# for a,b in zip(l1,l2):
#     print(a,b)

# for a in l2:
#     l1.append(a)
# print(l1)

l1.extend(l2)
print(l1)
print(l2)