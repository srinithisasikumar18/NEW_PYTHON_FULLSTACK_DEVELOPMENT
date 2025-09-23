numbers=[1,2,3,4,5,6,7,8,9,10]
even_num=list(filter(lambda n:n%2==0, numbers))
print(even_num)

#without lambda
numbers=[1,2,3,4,5,6,7,8,9,10]
#collect all even numbers in list
def verify(num):
    return num%2 ==0
even_numbers=list(filter(verify,numbers))
print(numbers)
print(even_numbers)