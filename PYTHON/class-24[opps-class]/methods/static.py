class Account:

    @staticmethod
    def cal_interest(p,r,t):
        return p*r*t/100
print(Account.cal_interest(1000000,3,1))