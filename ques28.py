# guess the output

l = [[2,1] for j in range(2)]
# print(l) # [[2, 1], [2, 1]]

var = 0
for i in range(2):
    var = var+l[i][i]
print(var)

# output is 3