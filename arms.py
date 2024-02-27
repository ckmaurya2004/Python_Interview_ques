# for i in range(1,1001):
#     n = len(str(i))
#     sum1=0
#     num = i
#     i = str(i)
#     for digit in i:
#         sum1 = sum1+int(digit)**n
#     if sum1 == num:
#         print(sum1)


# using whhile loop
 
for i in range(1,1001):
    n = len(str(i))
    sum1=0
    num = i
    while(i!=0):
        digit = i%10
        sum1 = sum1 + digit**n
        i = i//10
    if sum1==num:
        print(sum1)



