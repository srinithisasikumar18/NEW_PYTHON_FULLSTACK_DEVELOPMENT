class Test:
    a=100
    def m1(self):
        print(Test.a)
        print(self.a)
    @classmethod
    def m2(cls):
        print(Test.a)
        print(cls.a)
a1=Test()
a1.m1()
print(Test.a)
print(a1.a)