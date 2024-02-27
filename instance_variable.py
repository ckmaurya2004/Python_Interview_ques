class Test():
    def __init__(self) :
        self.a = 2
    def func(self):
        self.b=2

t = Test()
t.func()
t.c=3
print(t.__dict__)
        