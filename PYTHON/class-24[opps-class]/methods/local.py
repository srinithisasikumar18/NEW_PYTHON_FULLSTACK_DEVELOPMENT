class Account:
    a=100
    def m1(self):
        self.b=200
        c=300
        print(c)
    # def m2(self):
        # print(c)--------NameError: name 'c' is not defined
a1=Account()
a1.m1()
a1.m2()
