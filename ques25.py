mylist = [('do',('cat','dog','donut','at','todo'))]

prefix = mylist[0][0]
len1 =  len(prefix)
output = []

for  word in mylist[0][1]:
    if prefix == word[:len1]:
        output.append(word)

print(output)
