"""
write a program to sort characters and numbers so that first alphabet and then number are printed

input:A7R1B3
output :ABR137

"""

str1 = "A7R1B3"
alphabet = []
number =[]

for ch in str1:
    if ch.isalpha():
        alphabet.append(ch)
    else:
        number.append(ch)

final_list = sorted(alphabet)+sorted(number)
print(''.join(final_list))


