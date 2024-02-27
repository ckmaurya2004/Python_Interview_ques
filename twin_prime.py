# what is twin prime number jinke bich difference two ka ho (19-17 = 2,13-11 = 2)

def Isprime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i ==0:
            return False
    return True

num1 = int(input("enter first number!" ))
num2 = int(input("enter second number!" ))

if Isprime(num1) and Isprime(num2):
    if abs(num1 - num2)==2: # abs() always returns positive numbers (11-15 = 2)
        print(f"{num1} and {num2} are twin prime numbers")
    else:
        print(f"{num1} and {num2} are  not twin prime numbers")

else:
    print("number are not prime number")



