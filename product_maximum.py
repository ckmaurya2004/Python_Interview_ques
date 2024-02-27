"""
input array:[5,3,1,4,3,7,6,9,2]
maximum product pair: (7,9)
or
input array:[0,-2,-1,-4,-8,7,-8,8]
maximum product pair: (-8,-8)

"""

def max_product(arr):
    a_len = len(arr)
    if a_len<2:
        print("Not Find Max Product")
        return
    a = arr[0]
    b = arr[1]
    for i in range(0,a_len):
        for j in range(i+1,a_len):
            if (arr[i]*arr[j])>(a*b):
                a = arr[i]
                b = arr[j]
    return a,b



arr = eval(input("enter a array!" ))
print("maximaum product is",max_product(arr))