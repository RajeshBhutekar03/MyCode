def CheckEven(No):
    return (No % 2 == 0)

def Doubles(No):
    return (No*2)

def Sum(A,B):
    return (A+B)

def filterX(Data_Helper,Data):
    Result=[]
    for No in Data:
        if (Data_Helper(No)==True):
            Result.append(No)
    return Result

def mapx(Data_Helper,Data):
    Result=[]
    for No in Data:
        value=Data_Helper(No)
        Result.append(value)
    return Result

def ReduseX(Data_Helper,Data):
    Ans=0
    for no in Data:
        Ans=Data_Helper(Ans,no)
    return Ans

def main():
    print("Enter number ")
    iSize=int(input())
    Data_Input=[]
    print("Enter number here")
    for get in range(0,iSize,1):
        iValue=int(input())
        Data_Input.append(iValue)

    Data_Filter=filterX(CheckEven,Data_Input)
    print("Print Data After filter :",Data_Filter)

    Data_Map=mapx(Doubles,Data_Filter)
    print("Print Data After Maping :",Data_Map)

    Data_Reduce=ReduseX(Sum,Data_Map)
    print("print Data After reduce :",Data_Reduce)
if __name__ == "__main__":
     main()