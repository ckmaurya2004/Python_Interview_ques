"""
nums = [1,3,4,5]
target = 7 # add kro element jiska addtion 7 ho in case 3,4
output:[1,2] # return kro 3,4 ka index
Note-> indxes not repeatable for same value

"""

num = eval(input("enter list!" ))
target = int(input("target number! "))

output_list = []
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if (num[i]+num[j])==target  and len(output_list) == 0:
            output_list.append(i)
            output_list.append(j)
print(output_list)

