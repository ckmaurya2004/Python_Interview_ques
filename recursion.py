import sys
print(sys.getrecursionlimit()) # by default 1000
sys.setrecursionlimit(200)
print(sys.getrecursionlimit()) # set limit 200




i=0
def demo():
    global i
    i+=1
    print("demo",i)
    demo()

# demo()