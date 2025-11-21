import order
print(dir(order))


from order import price,order as ord
print(type(ord))
print(type(price))
print(ord())
print(price)