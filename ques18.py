"""
input-> = ['123498ki45ra78n','34mau6789rya','7317ck689mau899rya']
output => int-> [1234984578,346789,7317689899]
output = > str-> [kiran,maurya,ckmaurya]

"""

l1  = ['123498ki45ra78n','34mau6789rya','7317ck689mau899rya']
int_l2 =[]
str_l3 = []

for i in l1:
    int_var = ""
    str_var = ""
    for j in i:
        if j.isdigit():
            int_var = int_var + j
        else:
            str_var = str_var + j   
    
    int_l2.append(int_var)
    str_l3.append(str_var)

print(int_l2)
print(str_l3)

