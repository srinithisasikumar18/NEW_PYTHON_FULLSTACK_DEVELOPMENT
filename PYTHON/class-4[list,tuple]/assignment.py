# ERRORS IN PYTHON

# SYNTAX_ERROR---
if True
    print("hi") #--------SyntaxError: expected ':'----

# INDENTATION_ERROR
if True:
print("hi") #----------IndentationError: expected an indented block after 'if' statement------

# # NAME_ERROR
print(a) #---------------NameError: name 'a' is not defined-------------

# # VALUE ERROR
age1=int(input("enter the name"))
age2=int(input("enter the name"))
print(age1)
print(age2) #------------ValueError: invalid literal for int() with base 10: ' srinthi'-----------

# TYPE_ERROR
age=20
print("i am" + age) #---------TypeError: can only concatenate str (not "int") to str----------

# INDEX_ERROR
number=[1,2,3,4]
print(number[4]) #--------IndexError: list index out of range-------

# ATTRIBUTE_ERROR 
name="srinithi"
s=name.push()
print(s) #----------AttributeError: 'str' object has no attribute 'push'---------

# KEY_ERROR
emp={
    1:"srinithi",
    2:"madhu",
    3:"lalitha"
}
print(emp[4]) #------------KeyError: 4-----------