def CheckEvenNumber(No):
    return (No % 2 ==0)

def Increment(No):
    return No +2

def FilterX(Arr,Function_Name):
    Result =[]
    for no in Arr:
        if (Function_Name(no)):
            Result.append(no)
            return Result

def mapx(Arr,Function_Name):
    Result=[]
    for no in Arr:
        if(Function_Name(no)):
            Result.append(no)
            return Result

def reducex(Arr):
    Sum=0
    for no in Arr:
        Sum = Sum + no
        return   Sum

def main():
    Data=[1,2,3,4,5,6,7,8,9,10]
    print("Print origanal data",Data)

    Data_Filter=list(FilterX(Data,CheckEvenNumber))
    print("Print Data after Filter",Data_Filter)

    Data_Map=list(mapx(Data,Increment))
    print("Print Data after maping",Data_Map)

    Ret=reducex(Data_Map)
    print("Print after data reduce",Ret)

if __name__ == "__main__":
    main()


