# def avg(a,b,c):
#     return (a+b+c)/3
#
# def avg(*t):
#     return sum(t)/len(t)
#
# a = avg(3,4,5)
# print(a)
# b= avg(3,4)
# print(b)
#


# def add(*num):
#     sum1 = 0
#     for i in num:
#         sum1 = sum1+i
#     print(sum1)
def add(**num1):
    print(num1)
    sum1 = 0
    for key in num1:
        sum1 = sum1+num1[key]
    print(sum1)
#
# add(10,20)
# add(10,20,20)
add(a = 20,b=40,c=20)


