"""

input=> {'orange':'fruit','potato':'vegitable','banana':'fruit'}

output => {'fruit':['orange','banana'],'vegitable':['potato']}

"""

dict1 =  {'orange':'fruit','potato':'vegitable','banana':'fruit'}

new_dict = {}

for key in dict1:
    if dict1[key] not in new_dict:
        new_dict[dict1[key]] = [key]
    else:
        new_dict[dict1[key]].append(key)


print(new_dict)