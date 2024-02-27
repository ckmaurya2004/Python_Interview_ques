"""
input-> 'abcaba'
output-> abcaabbaaa
"""

str1 = 'abcaba'

str2 =""
mydict = {}

for ch in str1: # a
    if ch not in mydict:
        mydict[ch] =1
        # print(ch)
    else:
        mydict[ch] = mydict[ch] + 1
    print(ch*mydict[ch],end="")




# print(2*'k')
