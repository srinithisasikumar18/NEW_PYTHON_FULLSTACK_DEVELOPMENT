class Account:
    Count=0
    def increment_used(self):
        Account.Count=Account.Count+1
a1=Account()
a2=Account()
a3=Account()
a1.increment_used()
a2.increment_used()
a3.increment_used()
print(Account.Count)

print("------ANOTHER WAY-------")
class Account:
    no_of_obj_created=0
    def __init__(self):
        Account.no_of_obj_created=Account.no_of_obj_created+1
    @classmethod
    def used_no_of_obj(cls):
        return cls.no_of_obj_created
a1=Account()
a2=Account()
a3=Account()
a4=Account()
a5=Account()
print(Account.no_of_obj_created)
print(Account.used_no_of_obj())