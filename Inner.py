

def Hello():
    print("Inside Hello")
    # This is inner function
    def Demo():
        print("Inside Demo")
        Demo()

Hello()
