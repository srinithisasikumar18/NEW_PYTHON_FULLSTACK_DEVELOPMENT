class Account:
    min_bal=500  #class variable
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
    def open_account(self):
        print("Account created")
    # a=open_account()
e1=Account(101,"rahul gandhi",5000)
print(e1.__dict__)
e2=Account(102,"sonia gandhi",15000)
print(e2.__dict__)
e3=Account(103,"priyanka gandhi",25000)
print(e3.__dict__)
print(Account.__dict__)