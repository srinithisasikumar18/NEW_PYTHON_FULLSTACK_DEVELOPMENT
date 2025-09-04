def outer():
    print("outer")
    def inner():
        print("inner")
    
outer()
inner() #------NameError: name 'inner' is not defined. Did you mean: 'iter'?