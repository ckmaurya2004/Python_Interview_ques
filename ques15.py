# in given string first letter must be uppercase
#  and all letter is upper to lower and lower to upper 



#*************** using string  methods *******************************

# str1 = "kIrAn"
# str2 = ""
# i = 0
# while i<len(str1):
#     if i==0:
#         str2 = str2+str1[i].upper()
#     else:
#        str2 = str2+str1[i].swapcase()
#     i+=1

# print(str2)


# **************** manually ************************************************

str1 = "kIrAn"

def func(str1):
    str2 = ""
    asc = ord(str1[0])
    if asc>=97 and asc<=122:
        str2= str2+chr(asc-32)
    else:
        str2 = str2+chr(asc)
    for i in str1[1:]:
        if ord(i)>=65 and ord(i)<=97:  # uppercase
            str2 = str2+chr(ord(i)+32)
        else:
            str2 = str2+chr(ord(i)-32)
    print(str2)


func(str1)




    






