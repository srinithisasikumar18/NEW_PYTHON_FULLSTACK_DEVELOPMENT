class Account:
    min_bal=500
    def __init__(self,id,name,amount):
        self.acc_id=id 
        self.acc_name=name
        self.acc_bal=amount
    def open_acc(self):
        print("Acc opened")
    def deposit(self,amount):
        self.acc_bal=self.acc_bal+amount
    def withdrawal(self,amount):
        self.acc_bal=self.acc_bal-amount
    def get_bal(self):
        return self.acc_bal-self.min_bal
    @classmethod
    def update_min_bal(cls,amount):
        cls.min_bal=amount
Account.update_min_bal(600)
a1=Account(101,"rahul",5000)
a1.deposit(500)
a1.deposit(1500)
a1.withdrawal(50)
print(a1.get_bal())
a2=Account(102,"sonia",15000)
a2.deposit(150)
print(a2.get_bal())
a3=Account(103,"priyanka",25000)
a3.withdrawal(15000)
print(a3.get_bal())
# print(a1.__dict__)
# print(a2.__dict__)
# print(a3.__dict__)