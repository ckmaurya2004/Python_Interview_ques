import  random
import  string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
punc = string.punctuation
all = lower+upper+punc

length = int(input("enter length! " ))
list_password = random.sample(all,length) # always return list ['2','a','%']
pasword = ''.join(list_password)
print(pasword)