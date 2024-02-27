class Dad:
    def printDadInfo(self):
        print("Hello I am Dad class")

class Son(Dad):
    def printSonInfo(self):
        print("Hello I am Son class")

class Child(Son):
    def printChildInfo(self):
        print("Hello I am Child class")


arnav = Dad()
arpit = Son()
sivam = Child()

sivam.printDadInfo()
sivam.printSonInfo()
sivam.printChildInfo()







