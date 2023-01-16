#Fuction accpeting nothing abd return nothing
def Demo1():
    print("inside deno1")

#Function accepting one and return nothing
def Demo2(No):
    print("Inside Demo2 :",No)

#Function accepting one and return one
def Demo3(No1):
    print("Inside Demo3:",No1)
    return No1+2

#Function accepting two and return two
def Demo4(num1,num2):
    print("inside Demo4 ")
    Add=num1+num2
    return Add

#Function accepting two and return two
def Demo5(ivalu1,ivalu2):
    print("Inside Demo4")
    Add=ivalu1+ivalu2
    Sub=ivalu1-ivalu2
    return Add,Sub

def main():
    Demo1()
    Demo2("hello")
    Ans=Demo3(20)
    print("From Demo3:",Ans)
    Ans1=Demo4(10,11)
    print("From Demo4 :",Ans1)
    Ans2=Demo5(11,10)
    print("from demo5 :",Ans2)


if __name__ == "__main__":
        main()