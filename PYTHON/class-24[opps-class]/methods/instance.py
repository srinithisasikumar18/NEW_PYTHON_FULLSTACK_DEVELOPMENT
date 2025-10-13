class Account:
    def set_account_id(self,id):
        self.acc_id=id
    def get_account_id(self):
        return self.acc_id 
a1=Account()
a2=Account()


a1.set_account_id(1001)
a2.set_account_id(1002)
print(a1.get_account_id())
print(a2.get_account_id())