def Multption(No1,No2):
    Ans=0
    Ans=No1*No2
    return Ans

def Decoreted_Function(Function_Name):
    def Inner(A,B):
        if(A<B):
            A,B=B,A
            output= Function_Name(A,B)
            return output
        return Inner()


def main():
 Value1=int(input("Enter first number:"))
 Value2=int(input("Enter  second number  :"))

 New_Function=Decoreted_Function(Multption())
 Ret=New_Function(Value1,Value2)
 print(":",Ret)

 if __name__=="__main__":
     main()
