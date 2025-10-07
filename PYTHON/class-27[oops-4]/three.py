class Order:
    def __init__(self,ord_id,ord_name,ord_price):
        self.id=ord_id
        self.name=ord_name
        self.price=ord_price
    def add_discount(self):
        self.discount=5
    @classmethod
    def check_avail(cls):
        self.avail=True
    #it is not possible to create a instance variable with "class method"
o1=Order(11,"mp1",10)
o1.add_discount()
o1.check_avail()

o2=Order(12,"mp2",20)
o2.add_discount()
o3=Order(13,"mp3",30)
print(o1.__dict__)
print(o2.__dict__)
print(o3.__dict__)