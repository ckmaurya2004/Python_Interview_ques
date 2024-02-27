str1 = input("enter a string ! ") # KIRAN
upper_str = ""
for ch in str1:
    lower = ord(ch)
    if lower>64 and lower<91:
        upper_str = upper_str+chr(lower+32)
    else:
        upper_str = upper_str+chr(lower)

print("lower case string is :",upper_str)




