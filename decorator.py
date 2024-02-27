def extra_info(marks):
    def gread(num):
        print("Gread Here ")
        a = marks(num)
        print(a)
        if a>5.0:
            print("pass")
        else:
            print("fail")
    return  gread


@extra_info
def marks(num):
    sum =0
    avg = 0
    for item in num:
        sum = sum+item
        avg = sum/len(num)
    return avg


marks([2,4,5,6,7])