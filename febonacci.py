n = int(input(" enter  number of terms "))
first = 0
second = 1
if n<=0:
    print("Please enter positive number ")

elif n==1:
    print("febonacci series is :",)
    print(first)

else:
    for i in range(n):
        print("febonacci series is :")
        print(first)
        temp = first
        first = second
        second = temp+first

 