str1 = input("enter a string  ")
n = int(input("enter a count"))
ls = str1.split(" ")
dict = {}
for word in ls:
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1

word_list = []
for key in dict:
    if dict[key]>=n:
        word_list.append(key)

if len(word_list)>0:
    print(word_list)
else:
    print("No words")


