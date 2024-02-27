name = input(" enter your name")
count = 1
def print_name(myname):
    global count
    if count<=10:
        print(myname)
        count = count + 1
        print_name(myname)
    



print_name(name)
