# write a program perfect number (6 = 1,2,3,6 but 6 excluding 1+2+3 = 6)

num = int(input("enter number!" ))

def perfect(num):
    sum1= 0
    for i in range(1,num):
        if num%i==0:
            sum1 = sum1+i
    if sum1 == num:
        print("enterd number  is perfect")
    else:
        print("enter number is not perfect ")

perfect(num)