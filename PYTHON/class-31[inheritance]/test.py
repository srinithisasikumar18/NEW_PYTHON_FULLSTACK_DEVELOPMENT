class Account:
    count=0
    def __init__(self,id,name):
        self.id=id
        self.name=name
        Account.count+=1
    @classmethod
    def obj_created(cls):
        return cls.count

Account(101, "Srinithi")
Account(102, "Kokila")
Account(103, "sasi")
print(Account.obj_created())



print("================================================")
class Amount:
    counter=0
    def __init__(self,id,name):
        Amount.counter=Amount.counter+1
Amount(101,"s")
Amount(102,"r")
Amount(103,"i")
Amount(104,"k")
print("no of objects created",Amount.counter)

