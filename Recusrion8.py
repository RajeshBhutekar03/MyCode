
def Add(No):
    Ans=0
    if(No>=0):
        Ans=Ans+No
        No=No-1
        Add(No)
    return Ans
Ret=Add(4)


print("Result is :",Ret)
