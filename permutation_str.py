str1 = input("enter a string!" )

permu =[]
for i in range(0,len(str1)):
    for j in range(i+1,len(str1)+1):
        permu.append(str1[i:j])

print(permu)
