data = {'jay':['male',20,40],'raj':20,'kiran':['female',40,50],'sona':[30]}

count = 0
for key,value in data.items():
    if isinstance(value, list):
        count+=1
print(count)
    