# print((lambda a,b: a + b)(2,5))

# f = lambda x,y: x + y
# print(f(4,6))

def squre(x):
    return x*x

def cube(x):
    return x*x*x

func = [squre,cube]

for i in range(5):
    result = list(map(lambda x:x(i),func)) # lamba,arguments:expresion
    print(result)