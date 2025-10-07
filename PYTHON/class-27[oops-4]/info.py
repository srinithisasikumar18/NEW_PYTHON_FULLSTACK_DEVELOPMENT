class Order:
    def __init__(self,ord_id,ord_name,ord_price):
        print("__init__ is a special function")
        # self.id=ord_id
        # self.name=ord_name
        # self.price=ord_price
o1=Order(11,"mp1",10)
o2=Order(12,"mp2",20)
o3=Order(13,"mp3",30)
print(o1.__dict__)
print(o2.__dict__)
print(o3.__dict__)