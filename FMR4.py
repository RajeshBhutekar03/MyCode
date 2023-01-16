def CheckEven(No):
    return (No % 2 ==0)

def Doubles(No):
    return (No*2)

def filterX(Data_Helper,Data):
    Result=[]
    for No in Data:
        if(Data_Helper(No)==True):
            Result.append(No)
    return Result

def mapX(Data_Helper,Data):
    Result=[]
    for No in Data:
        value=Data_Helper(No)
        Result.append(value)
    return Result

def main():
    print("Enter number here")
    iSize =int(input())
    Data_Input=[]
    print("Print number we want enetre")
    for get in range(0,iSize,1):
        iValue=int(input())
        Data_Input.append(iValue)
    Data_Fiter=filterX(CheckEven,Data_Input)
    print("print Data after Filter :",Data_Fiter)

    Data_Map=mapX(Doubles,Data_Fiter)
    print("Data after filter :",Data_Map)

if __name__ == "__main__":
     main()