"""
input => "a$5djpglk34jpo/'[[;.43l;p[7,8l89.0kjkl89l;l;l"
output=> []
"""

str1 = "a$5djpglk34jpo/'[[;.43l;p[7,8l89.0kjkl89l;l;l"
temp = ""
data = []
for ch in str1:
    if ch.isdigit() or (ch == '.' and '.' not in temp):
       temp = temp+ch
    elif len(temp)!=0:
        data.append(eval(temp))
        temp = ""

data.sort()
print(data)
