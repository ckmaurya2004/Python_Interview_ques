l = [2,45,32,616] # output =[2,9,5,13]

output = []

for item in l:
    sum1=0
    for i in str(item):
        sum1 = sum1 + int(i)
    output.append(sum1)
print(output)
        







