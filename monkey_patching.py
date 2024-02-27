# monkey patching is the change to the attribute in the runtime(dynamically change the attribute)
    
class Test:
    x=3
    def __init__(self) :
        pass
    def get_data(self):
        print("this is a get data method to fetch data from database")
    def f1(self):
        self.get_data()
    def f2(self):
        self.get_data()
    
t1 = Test()
t1.f1()
t1.f2()


def new_get_data(self):
    print("this is a function of new get data")

Test.get_data = new_get_data # monkey patching 
print("aftr monkey patching")
t1.f1()
t1.f2()


a=10
print(t1.x)
Test.x = a
print(t1.x)