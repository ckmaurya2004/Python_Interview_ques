# 53 = 110010 iska reverse
# 001101 =13

def changeads(num):
    b = bin(num)
    b1 = b[2:len(b)]
    b2= ""
    for bit in b1:
        if bit == '0':
            b2 = b2+'1'
        else:
            b2 = b2+'0'
    sum1 = 0
    for i in range(len(b2)):
        sum1 =sum1+(int(b2[i])*(2**(len(b2)-(i+1))))
    print(sum1)


num = int(input("enter a number!" ))

changeads(num) #50
    