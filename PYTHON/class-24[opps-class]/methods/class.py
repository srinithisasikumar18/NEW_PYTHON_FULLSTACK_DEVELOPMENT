class Account:
    min_bal=500
    @classmethod
    def get_min_bal(cls):
        return cls.min_bal
    @classmethod
    def update_min_bal(cls):
        cls.min_bal=600
        

print(Account.get_min_bal())
Account.update_min_bal()
print(Account.get_min_bal())
