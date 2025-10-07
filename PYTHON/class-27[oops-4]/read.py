class Order:
    def __init__(self,ord_id,ord_name,ord_price):
        self.id=ord_id
        self.name=ord_name
        self.price=ord_price
    def add_discount(self):
        self.discount=5
    def get_price(self):
        print(self.price)
   

o1=Order(11,"mp1",10)
o1.add_discount()
o1.status="In progress"

o2=Order(12,"mp2",20)
o2.add_discount()
o3=Order(13,"mp3",30)
o3.status="Delivered"
print(o1.__dict__)
print(o2.__dict__)
print(o3.__dict__)

"""******************reading"""
print(o1.name)
o2.get_price()
print(o3.name)

'*** updating'
o3.price=45
print(o3.price)

print(o2.__dict__)
'****delete**'
del o2.price
print(o2.__dict__)