class Account:
    branchname="sbi"
    def __init__(self,id):
        self.id=id
        Account.parentName="sbi-ss"
    def bankloc(self):
        Account.loc="Marathahalli"
    @classmethod
    def updatebranch(cls):
        cls.mainbranch="bengaluru"
    @staticmethod
    def tax():
        Account.tax=11
a1=Account(101)
a1=Account(102)
print(Account.__dict__)
a1.bankloc()
a1.updatebranch()
a1.tax()
print(Account.__dict__)

