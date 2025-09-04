def outer():
    print("outer")
    def inner():
        print("inner")
    inner()
outer()