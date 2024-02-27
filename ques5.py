# input :"a3b2c2"
# output:"aaabbcc"

str1 = input("enter string ")
output = ""
for char in str1:
    if char.isalpha():
        var = char
    else:
        num = int(char)
        output = output+(var*num)
print(output)


# output :"3a2b2c"
# input:"aaabbcc"


# str1 = input("enter string ")
# output = ""
# for char in str1:
#     if char.isnumeric():
#         num = int(char)
#     else:
#         var  = char
#         output = output+(var*num)
# print(output)

