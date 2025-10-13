class Account:
    min_bal=500
    @classmethod
    def get_min_bal(cls):
        return cls.min_bal
print(Account.get_min_bal())