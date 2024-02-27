def isprime(number):
    for i in range(2,number):
            return False
    return True
def primeGenerator(n):
    num = 2
    while n:
        if isprime(num):
            yield num
            n= n-1
        num+=1
    return 
    
pn = primeGenerator(10)
for i in pn:
    print(i,end=" ")

