def Outer():
    print("Inside Outer")
    # This is inner function
    def Inner():
        print("Inside Inner")

        return Inner()


ret=Outer()

print(type(ret))
print(id(ret))
ret