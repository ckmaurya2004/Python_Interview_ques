"""
write a program for following requirements
input : 2 512
output : 8 ( 2*2 =4*2 = 8*2 = 16 ....=512) 8 time jayega  for 512

"""
 # only for 2 because result =2
#
# num = input(" enter a number ! " )
# result = 2
# count = 0
# list = num.split()  # ['2', '512']
# num1 ,num2 = list # num1 = 2,num2 = 512
# while True:
#     if result != int(num2):
#         result = result* int(num1)
#         count = count+1
#     else:
#         break
# print(count)



num = input(" enter a number [2 512] ! " )
result = int(input(" enter a number for multiply !" ))
count = 0
list = num.split()  # ['2', '512']
num1 ,num2 = list # num1 = 2,num2 = 512
while True:
    if result != int(num2):
        result = result* int(num1)
        count = count+1
    else:
        break
print(count)