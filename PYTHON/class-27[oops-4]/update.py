class Account:
    def __init__(self,id,name,age):
        self.eid=id
        self.name=name
        self.age=age
    def acc_bal(self):
        self.balance=5000
    def update_bal(self): #-----------------updating with the help of function
        self.update_bal=self.balance+2500

a1=Account(1,"srinithi",23)
a1.update_bal=3000 #-----------updating with the help of object
a1.acc_bal()
# a1.update_bal()
a2=Account(2,"kokila",43)
a2.acc_bal()
a3=Account(3,"sasi",50)
print(a1.__dict__)
print(a2.__dict__)