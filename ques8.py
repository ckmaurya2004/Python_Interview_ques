"""
isme hmm 4 input lenge a,b,s,t
a = length hoga #4
b =  length hoga # 4
s = string hoga  a ka mtlb 4 digit ka "abcd"
t = list hoga b length ka ['abcd', 'bcd', 'accd','ebd']
ab ak ak leter remove karenge s ka aur check karenge bcha hua substring  t me match kr raha h ki  nhi
remove a = 'bcd' bcha ab check t me h ha hai to count ko 1 se increment kr do 
fir a ko same position pr insert krdo aur remove  kro next later

"""

def equalization(a,b,s,t):
    str_list = []
    count = 0
    for ch in s:
        str_list.append(ch)

    for i in range(a):
        char = str_list.pop(i)
        for word in t:
            if ''.join(str_list)==word:
                count = count+1
        str_list.insert(i, char)
    return count


# print(equalization(5,4,'abcde',['bcde','aace','abde','abce']))

str_length = int(input("enter a length of string!" ))
list_length = int(input("enter a length of list!" ))
str1 = input("enter a string! " ) 
list = eval(input("enter a list!"))

print(equalization(str_length,list_length,str1,list))